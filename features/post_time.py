from datetime import datetime

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()


def post_time():
    """
    Add a column `creation_seconds` to a given dataframe that indicates the amount of seconds since UNIX zero time that
    the post was created
    :return: dataframe
    """

    df = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_CreationDate']) \
        .dropna() \
        .withColumn('creation_seconds', datetime.strptime(col('_CreationDate'), '%Y-%m-%dT%H:%M:%S.%f').strftime('%s'))

    return df
