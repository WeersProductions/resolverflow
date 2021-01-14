"""
Based on: https://github.com/BhaskarBiswas/PySpark-Codes/blob/master/Automated_VIF_Spark.py
"""
from pyspark.sql import SparkSession

from pyspark.ml.regression import LinearRegression
from pyspark.ml.evaluation import RegressionEvaluator


def calc_feature_pair_vifs(spark):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    # Drop columns that are not a feature
    feature_data = feature_data.drop("_Id", "_Text", "is_question", "is_answered")
    # Drop columns that don't correlate with our label
    feature_data = feature_data.drop("number_of_lines")

    # For testing
    feature_data = feature_data.select("user_age", "posts_amount", "title_number_of_characters")

    for i in range(len(feature_data.columns) - 1):
        for j in range(i + 1, len(feature_data.columns)):
            df = feature_data.rdd.map(lambda x: [x[i], x[j]]).toDF(['feature', 'label'])
            linear_regression = LinearRegression(featuresCol='feature', labelCol='label')
            linear_regression_model = linear_regression.fit(df)
            prediction = linear_regression_model.transform(df)
            evaluator = RegressionEvaluator(predictionCol='prediction', labelCol='label')
            r_squared = evaluator.evaluate(prediction, {evaluator.metricName: "r2"})
            vif = 1 / (1 - r_squared)
            print(feature_data.columns[i] + " - " + feature_data.columns[j] + ": " + vif)


if __name__ == "__main__":
    print("Starting vif analysis.")
    spark = SparkSession.builder.getOrCreate()
    calc_feature_pair_vifs(spark)
