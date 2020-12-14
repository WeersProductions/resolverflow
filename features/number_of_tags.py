# TODO: we should probably also use this file to check whether the tags contain platform and/or programming language.
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

def number_of_tags_df():
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet").select(["_Id","_Tags"]).dropna()
    # Split tags.
    df.show()