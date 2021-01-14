from pyspark.sql import SparkSession
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler

# Decision tree
from pyspark.sql.functions import col
from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier, RandomForestClassifier, GBTClassifier
from pyspark.ml.regression import DecisionTreeRegressor
from pyspark.ml.feature import StringIndexer, VectorIndexer, IndexToString
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, RegressionEvaluator


def load_feature_data(spark):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = feature_data.drop("_Text")
    return feature_data


def calc_correlation(spark):
    """
    Calculates the Pearson Correlation Coefficient

    TODO: this currently calculates a corr matrix between every feature.
    Would be nice if we first calculate correlation between every feature and the label. We can drop some features after this.

    Example result:
    ['_Id', 'contains_questionmark', 'title_length', 'HasAnswer', '_PostHistoryTypeId', 'number_of_characters', 'number_of_interpunction_characters', 'interpunction_ratio', 'number_of_lines', 'average_line_length', 'number_of_words', 'average_word_length', 'creation_seconds', 'number_of_tags', 'contains_language_tag', 'contains_platform_tag', 'age', 'posts_amount', 'IsQuestion']
    DenseMatrix([[  1.00000000e+00,  -3.23648297e-02,   1.36629899e-01,
               -1.94351632e-01,              nan,   2.20971673e-02,
               -6.43364684e-02,  -7.79819884e-02,  -2.84092244e-03,
                2.21063239e-02,   1.41078529e-02,   1.28598260e-03,
                9.97103954e-01,   1.80844989e-02,   3.25580493e-02,
               -6.52822255e-02,   3.62689766e-01,  -1.82437362e-01,
                           nan],
             [ -3.23648297e-02,   1.00000000e+00,   2.07046487e-01,
                4.16470609e-02,              nan,  -7.25951761e-04,
                5.07786229e-03,   5.85491689e-03,   2.77075708e-04,
               -7.27358292e-04,   1.20871645e-04,  -1.21060492e-03,
               -3.65967532e-02,  -1.07925451e-02,  -3.79321324e-04,
               -3.63010816e-03,   2.69849299e-02,   5.71539737e-02,
                           nan],
             [  1.36629899e-01,   2.07046487e-01,   1.00000000e+00,
               -4.03369767e-02,              nan,   2.87322590e-03,
               -6.66192943e-03,  -8.17773729e-03,  -1.00853930e-03,
                2.87628941e-03,   1.88385649e-03,  -4.16745085e-04,
                1.35612346e-01,   8.64241451e-02,  -1.58040521e-02,
                2.43823586e-02,   7.88967451e-02,  -1.49647350e-02,
                           nan],
             [ -1.94351632e-01,   4.16470609e-02,  -4.03369767e-02,
                1.00000000e+00,              nan,  -4.21452094e-03,
                1.50102344e-02,   1.79410239e-02,   6.84993494e-04,
               -4.21480835e-03,  -1.70406510e-03,  -2.02358099e-03,
               -1.96640740e-01,  -4.26913537e-03,   7.01465993e-02,
               -3.12794957e-02,  -1.26410604e-02,   1.11902271e-01,
                           nan],
             [             nan,              nan,              nan,
                           nan,   1.00000000e+00,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan],
             [  2.20971673e-02,  -7.25951761e-04,   2.87322590e-03,
               -4.21452094e-03,              nan,   1.00000000e+00,
                3.51495566e-01,   6.81855464e-02,   1.93821494e-03,
                9.99993205e-01,   8.88606137e-01,   1.31968517e-02,
                2.20005964e-02,   6.94228070e-05,   5.07397936e-04,
               -1.28448322e-03,   8.28429000e-03,  -4.42951040e-03,
                           nan],
             [ -6.43364684e-02,   5.07786229e-03,  -6.66192943e-03,
                1.50102344e-02,              nan,   3.51495566e-01,
                1.00000000e+00,   8.82023939e-01,   1.90760064e-03,
                3.51489161e-01,   2.70235726e-01,   1.04250036e-01,
               -6.53932741e-02,  -2.47505006e-03,  -3.96491021e-03,
                2.10525109e-03,  -2.38999581e-02,   1.44543207e-02,
                           nan],
             [ -7.79819884e-02,   5.85491689e-03,  -8.17773729e-03,
                1.79410239e-02,              nan,   6.81855464e-02,
                8.82023939e-01,   1.00000000e+00,   1.72594997e-03,
                6.81823006e-02,   3.55072988e-02,   7.69486398e-02,
               -7.92360119e-02,  -2.47590558e-03,  -4.84524536e-03,
                2.65022259e-03,  -2.87892037e-02,   1.75612876e-02,
                           nan],
             [ -2.84092244e-03,   2.77075708e-04,  -1.00853930e-03,
                6.84993494e-04,              nan,   1.93821494e-03,
                1.90760064e-03,   1.72594997e-03,   1.00000000e+00,
               -1.36547468e-03,   2.95619045e-03,  -1.66108245e-03,
               -3.22863670e-03,   2.72838426e-04,   1.58672258e-03,
                7.46106080e-04,  -1.02576817e-03,   1.30524624e-03,
                           nan],
             [  2.21063239e-02,  -7.27358292e-04,   2.87628941e-03,
               -4.21480835e-03,              nan,   9.99993205e-01,
                3.51489161e-01,   6.81823006e-02,  -1.36547468e-03,
                1.00000000e+00,   8.88595744e-01,   1.32015875e-02,
                2.20107171e-02,   6.83581617e-05,   5.02158398e-04,
               -1.28811911e-03,   8.28726080e-03,  -4.43347549e-03,
                           nan],
             [  1.41078529e-02,   1.20871645e-04,   1.88385649e-03,
               -1.70406510e-03,              nan,   8.88606137e-01,
                2.70235726e-01,   3.55072988e-02,   2.95619045e-03,
                8.88595744e-01,   1.00000000e+00,  -3.74130345e-01,
                1.36362652e-02,  -2.75775777e-04,   6.13867206e-05,
               -1.37872541e-03,   5.63599384e-03,  -1.50477215e-03,
                           nan],
             [  1.28598260e-03,  -1.21060492e-03,  -4.16745085e-04,
               -2.02358099e-03,              nan,   1.31968517e-02,
                1.04250036e-01,   7.69486398e-02,  -1.66108245e-03,
                1.32015875e-02,  -3.74130345e-01,   1.00000000e+00,
                1.92128907e-03,   7.90916515e-04,   8.19145394e-04,
                1.50968987e-03,  -3.13012169e-04,  -2.49162738e-03,
                           nan],
             [  9.97103954e-01,  -3.65967532e-02,   1.35612346e-01,
               -1.96640740e-01,              nan,   2.20005964e-02,
               -6.53932741e-02,  -7.92360119e-02,  -3.22863670e-03,
                2.20107171e-02,   1.36362652e-02,   1.92128907e-03,
                1.00000000e+00,   1.89194489e-02,   3.32342637e-02,
               -6.23211546e-02,   3.61973801e-01,  -1.88036054e-01,
                           nan],
             [  1.80844989e-02,  -1.07925451e-02,   8.64241451e-02,
               -4.26913537e-03,              nan,   6.94228070e-05,
               -2.47505006e-03,  -2.47590558e-03,   2.72838426e-04,
                6.83581617e-05,  -2.75775777e-04,   7.90916515e-04,
                1.89194489e-02,   1.00000000e+00,   1.98270937e-01,
                1.35266977e-01,   1.74938227e-02,  -7.66032362e-05,
                           nan],
             [  3.25580493e-02,  -3.79321324e-04,  -1.58040521e-02,
                7.01465993e-02,              nan,   5.07397936e-04,
               -3.96491021e-03,  -4.84524536e-03,   1.58672258e-03,
                5.02158398e-04,   6.13867206e-05,   8.19145394e-04,
                3.32342637e-02,   1.98270937e-01,   1.00000000e+00,
               -1.40205092e-01,  -5.38021784e-02,   5.58124325e-04,
                           nan],
             [ -6.52822255e-02,  -3.63010816e-03,   2.43823586e-02,
               -3.12794957e-02,              nan,  -1.28448322e-03,
                2.10525109e-03,   2.65022259e-03,   7.46106080e-04,
               -1.28811911e-03,  -1.37872541e-03,   1.50968987e-03,
               -6.23211546e-02,   1.35266977e-01,  -1.40205092e-01,
                1.00000000e+00,  -2.67746676e-02,  -2.93093008e-03,
                           nan],
             [  3.62689766e-01,   2.69849299e-02,   7.88967451e-02,
               -1.26410604e-02,              nan,   8.28429000e-03,
               -2.38999581e-02,  -2.87892037e-02,  -1.02576817e-03,
                8.28726080e-03,   5.63599384e-03,  -3.13012169e-04,
                3.61973801e-01,   1.74938227e-02,  -5.38021784e-02,
               -2.67746676e-02,   1.00000000e+00,   1.72441098e-02,
                           nan],
             [ -1.82437362e-01,   5.71539737e-02,  -1.49647350e-02,
                1.11902271e-01,              nan,  -4.42951040e-03,
                1.44543207e-02,   1.75612876e-02,   1.30524624e-03,
               -4.43347549e-03,  -1.50477215e-03,  -2.49162738e-03,
               -1.88036054e-01,  -7.66032362e-05,   5.58124325e-04,
               -2.93093008e-03,   1.72441098e-02,   1.00000000e+00,
                           nan],
             [             nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                           nan,              nan,              nan,
                1.00000000e+00]])
    """
    feature_data = load_feature_data(spark)
    print("-- Calculating correlation --")
    print(feature_data.columns)
    vector_col = "features"
    assembler = VectorAssembler(inputCols=feature_data.columns, outputCol=vector_col)
    df_vector = assembler.transform(feature_data).select(vector_col)
    corr_mat = Correlation.corr(df_vector, vector_col, "spearman").head()
    print(str(corr_mat[0]))


def ExtractFeatureImp(featureImp, dataset, featuresCol):
    """
    From an index based importance list, to a feature label based importance list.
    """
    list_extract = []
    for i in dataset.schema[featuresCol].metadata["ml_attr"]["attrs"]:
        list_extract = list_extract + dataset.schema[featuresCol].metadata["ml_attr"]["attrs"][i]
    result = []
    for index, feature in enumerate(list_extract):
      result.append((feature, featureImp[index]))
    result.sort(key=lambda x: x[1])
    return result


def get_and_prepare_data(spark, original_label_col, label_col, feature_col_names, vector_col):
    feature_data = load_feature_data(spark)
    feature_data = feature_data.withColumnRenamed(original_label_col, label_col)
    feature_data = feature_data.withColumn(label_col, col(label_col).cast("integer"))
    assembler = VectorAssembler(inputCols=feature_col_names, outputCol=vector_col)
    data = assembler.transform(feature_data).select(label_col, vector_col)

    return data


def get_pipeline(data, label_col, vector_col, model):
    """
    Creates a pipeline that converts labels and includes the model step. Also returns the index of the model step.

    Args:
        data ([type]): [description]
        label_col ([type]): [description]
        vector_col ([type]): [description]
        model ([type]): [description]

    Returns:
        tuple(<stages>, Number): (<stages>, <model_index>)
    """
    labelIndexer = StringIndexer(inputCol=label_col, outputCol="indexedLabel").fit(data)
    featureIndexer = VectorIndexer(inputCol=vector_col, outputCol="indexedFeatures", maxCategories=4).fit(data)
    # Convert indexed labels back to original labels.
    labelConverter = IndexToString(inputCol="prediction", outputCol="predictedLabel",labels=labelIndexer.labels)

    return ([labelIndexer, featureIndexer, model, labelConverter], 2)


def print_evaluate(evaluator, predictions, vector_col, model, pipeline_model_index):
    test_value = evaluator.evaluate(predictions)
    test_name = evaluator.getMetricName()
    print("%s = %g " % (test_name, test_value))
    treeModel = model.stages[pipeline_model_index]
    print("model_summary", treeModel)
    print_feature_importance(treeModel, predictions, vector_col)


def decision_tree_regressor(spark):
    print("-- Calculating Decision Tree regressor --")
    # Create two columns, 'label' and 'features'. Label is true or false, features is a vector of values.
    original_label_col = "has_answer"
    label_col = "label"
    vector_col = "features"
    feature_col_names = ["title_contains_questionmark", "title_number_of_characters", "creation_seconds", "number_of_tags", "contains_language_tag", "contains_platform_tag", "user_age", "posts_amount", "answered_posts_amount"]

    data = get_and_prepare_data(spark, original_label_col, label_col, feature_col_names, vector_col)
    (trainingData, testData) = data.randomSplit([0.8, 0.2])

    dt = DecisionTreeRegressor(labelCol="indexedLabel", featuresCol="indexedFeatures")
    stages, pipeline_model_idx = get_pipeline(data, label_col, vector_col, dt)
    pipeline = Pipeline(stages=stages)
    model = pipeline.fit(trainingData)
    predictions = model.transform(testData)
    # For debugging purposes, show some of the predictions and their original labels.
    predictions.select("predictedLabel", "label", "features").show(5)

    evaluator = RegressionEvaluator(labelCol="indexedLabel", predictionCol="prediction", metricName="mae")
    print_evaluate(evaluator, predictions, vector_col, model, pipeline_model_idx)


def print_feature_importance(model, prediction_df, feature_col):
    """
    Calculate the importance score of each feature.

    Args:
        model: trained model
        prediction_df: transformed dataframe based on the model
        feature_col: name of the column that contains vectors for each feature
    """
    feature_importances = model.featureImportances
    print("feature_importance", feature_importances)
    feature_importance_info = ExtractFeatureImp(feature_importances, prediction_df, feature_col)
    print("feature_importance_info", feature_importance_info)


if __name__ == "__main__":
    """
    Run using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --name dreamteam analysis/analyze.py 2> /dev/null
    """

    print("Starting analysis.")
    spark = SparkSession.builder.getOrCreate()
    # calc_correlation(spark)

    # Train a model and print feature importance.
    decision_tree_regressor(spark)
