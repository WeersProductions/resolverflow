from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col


def post_answered(spark):
    """
    Return a dataframe that only contains post ids and whether they are answered or not.
    :return: dataframe
    """

    df = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_AcceptedAnswerId']) \
        .withColumn('HasAnswer', when(col("_AcceptedAnswerId").isNotNull(), True).otherwise(False)) \
        .drop("_AcceptedAnswerId")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    post_answered(spark).show()
