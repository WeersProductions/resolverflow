from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length

spark = SparkSession.builder.getOrCreate()

def title_features_df():
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id","_Title"]) \
        .dropna() \
        .withColumn('contains_questionmark', col("_Title").contains('?')) \
        .withColumn('title_length', length(col("_Title")))

    return df