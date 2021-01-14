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
    print("Model summary: ", treeModel)
    print("Full model: ", treeModel.toDebugString)
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
