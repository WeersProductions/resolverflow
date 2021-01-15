from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length


def title_features_df(spark):
    """
    Extract features from the title

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id, title_contains_questionmark,
            title_number_of_characters
        ]
    """
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(["_PostId", "_Text", "_PostHistoryTypeId"]) \
        .filter(col('_PostHistoryTypeId') == 1) \
        .dropna() \
        .withColumn('title_contains_questionmark', col("_Text").contains('?')) \
        .withColumn('title_number_of_characters', length(col("_Text"))) \
        .drop("_Text", "_PostHistoryTypeId") \
        .withColumnRenamed("_PostId", "_Id")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    title_features_df(spark).show()
