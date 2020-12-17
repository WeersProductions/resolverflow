from pyspark.sql.functions import col, to_timestamp
from pyspark.sql import SparkSession
from pyspark.sql.types import LongType


def post_time(spark):
    """
    Add a column `creation_seconds` to a given dataframe that indicates the amount of seconds since UNIX zero time that
    the post was created
    :return: dataframe
    """

    df = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_CreationDate']) \
        .dropna() \
        .withColumn('creation_seconds', to_timestamp(col('_CreationDate')).cast(LongType())) \
        .drop('_CreationDate')

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    post_time(spark).show()
