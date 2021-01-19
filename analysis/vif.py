"""
Based on: https://github.com/BhaskarBiswas/PySpark-Codes/blob/master/Automated_VIF_Spark.py
"""
from copy import deepcopy

from pyspark.sql import SparkSession

from pyspark.sql.functions import col
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator


def calc_feature_pair_vifs(spark, features):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = feature_data.select(*features)

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
            print("pair - " + feature_data.columns[i] + " - " + feature_data.columns[j] + ": " + str(vif))


def calc_one_out_vifs(spark, features):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])

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
        print("without - " + feature + ": " + str(vif))


if __name__ == "__main__":
    print("Starting vif analysis.")
    testing_features = ['#characters', '#punctuation_characters', 'punctuation_ratio', '#lines']
    global_spark = SparkSession.builder.getOrCreate()
    calc_feature_pair_vifs(global_spark, testing_features)
    calc_one_out_vifs(global_spark, testing_features)
