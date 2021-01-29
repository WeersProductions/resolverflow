from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col


def post_answered_df(spark):
    """
    Checks whether a post is answered or not.

    Returns:
        DataFrame: With columns [
            (post)_Id, has_answer
        ]
    """

    df = spark.read.parquet('/user/s*******/StackOverflow/Posts.parquet') \
        .select(['_Id', '_AcceptedAnswerId']) \
        .withColumn('has_answer', when(col("_AcceptedAnswerId").isNotNull(), True).otherwise(False)) \
        .drop("_AcceptedAnswerId")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    post_answered_df(spark).show()
