from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length

def title_features_df(spark):
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Title"]) \
        .dropna() \
        .withColumn('contains_questionmark', col("_Title").contains('?')) \
        .withColumn('title_length', length(col("_Title"))) \
        .drop("_Title")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    title_features_df(spark).show()
