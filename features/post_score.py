from pyspark.sql import SparkSession


def post_score(spark):
    """
    Return a dataframe that only contains post ids and their score
    :return: dataframe
    """

    df = spark.read.parquet('/user/s*******/StackOverflow/Posts.parquet') \
        .select(['_Id', '_Score']) \
        .dropna()

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    post_score(spark).show()
