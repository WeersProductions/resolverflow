"""
Based on: https://github.com/BhaskarBiswas/PySpark-Codes/blob/master/Automated_VIF_Spark.py
"""
from copy import deepcopy

from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.sql.types import IntegerType


def calc_feature_pair_vifs(spark, features, boolean_features):
    """ Calculate the VIF for each pairwise combination of features

        Args:
            spark (SparkSession): used to run queries and commands
            features: list of names of all features of which pairwise combinations the VIF is calculated

        Prints:
            VIF of each pairwise combination
    """
    feature_data = spark.read.parquet("/user/s*******/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = feature_data.select(*features)

    for boolean_feature in boolean_features:
        feature_data = feature_data.withColumn(boolean_feature, col(boolean_feature).cast(IntegerType()))

    for i in range(len(feature_data.columns) - 1):
        for j in range(i + 1, len(feature_data.columns)):
            df = feature_data.select(col(feature_data.columns[i]).alias('raw_feature'),
                                     col(feature_data.columns[j]).alias('label')).dropna()
            assembler = VectorAssembler(inputCols=['raw_feature'], outputCol='feature', handleInvalid='skip')
            df = assembler.transform(df)
            linear_regression = LinearRegression(featuresCol='feature', labelCol='label')
            linear_regression_model = linear_regression.fit(df)
            prediction = linear_regression_model.transform(df)
            evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='label')
            r_squared = evaluator.evaluate(prediction, {evaluator.metricName: "r2"})
            vif = 1 / (1 - r_squared)
            print("pair " + feature_data.columns[i] + " - " + feature_data.columns[j] + ": " + str(vif))


def calc_one_out_vifs(spark, features, boolean_features):
    """ Calculate the VIF for each 'leave-one-out' combination of features.

        Example:
            Original feature list:
                [A, B, C, D]
            VIF is calculated for:
                [   B, C, D]
                [A,    C, D]
                [A, B,    D]
                [A, B, C   ]

        Args:
            spark (SparkSession): used to run queries and commands
            features: list of names of all features of which 'leave-one-out' combinations the VIF is calculated

        Prints:
            VIF of each 'leave-one-out' combination
    """
    feature_data = spark.read.parquet("/user/s*******/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])

    for boolean_feature in boolean_features:
        feature_data = feature_data.withColumn(boolean_feature, col(boolean_feature).cast(IntegerType()))

    for feature_index, feature in enumerate(features):
        current_features = deepcopy(features)
        del current_features[feature_index]
        df = feature_data.select(*current_features).dropna()
        assembler = VectorAssembler(inputCols=current_features[:-1], outputCol='feature', handleInvalid='skip')
        df = assembler.transform(df)
        linear_regression = LinearRegression(featuresCol='feature', labelCol=current_features[-1])
        linear_regression_model = linear_regression.fit(df)
        prediction = linear_regression_model.transform(df)
        evaluator = RegressionEvaluator(predictionCol='prediction', labelCol=current_features[-1])
        r_squared = evaluator.evaluate(prediction, {evaluator.metricName: "r2"})
        vif = 1 / (1 - r_squared)
        print("without " + feature + ": " + str(vif))


if __name__ == "__main__":
    print("Starting vif analysis.")
    testing_features = ['#codeblocks', '#codespans', '#title_characters', 'average_line_length', 'average_word_length', 'contains_language_tag', 'contains_platform_tag', 'title_contains_questionmark']
    boolean_features = ['contains_language_tag', 'contains_platform_tag', 'title_contains_questionmark']
    global_spark = SparkSession.builder.getOrCreate()
    calc_feature_pair_vifs(global_spark, testing_features, boolean_features)
    calc_one_out_vifs(global_spark, testing_features, boolean_features)
