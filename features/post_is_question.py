from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col


def post_is_question_df(spark):
    """
    Return a dataframe that only contains post ids and whether they are answered or not.
    :return: dataframe
    """

    df = spark.read.parquet('/user/s*******/StackOverflow/Posts.parquet') \
        .select(['_Id', '_PostTypeId']) \
        .withColumn('is_question', when(col("_PostTypeId") == 1, True).otherwise(False)) \
        .drop("_PostTypeId")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    post_is_question_df(spark).show()
