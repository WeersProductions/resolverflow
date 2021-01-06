from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length


def title_features_df(spark):
    """ Extract features from the title

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id, title_contains_questionmark,
            title_number_of_characters
        ]
    """
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Title"]) \
        .dropna() \
        .withColumn('title_contains_questionmark', col("_Title").contains('?')) \
        .withColumn('title_number_of_characters', length(col("_Title"))) \
        .drop("_Title")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    title_features_df(spark).show()
