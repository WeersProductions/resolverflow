from pyspark.sql import SparkSession
from pyspark.sql.functions import array, array_intersect, col, expr, lit, size, split, when


def tag_info_df(spark):
    """ Extract features from the tags of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [(post)_Id, number_of_tags, contains_language_tag, contains_platform_tag]
    """
    language_list = ["django", "php"]
    language_list_col = array(*[lit(x) for x in language_list])
    platform_list = ["windows", "linux", "maccie"]
    platform_list_col = array(*[lit(x) for x in platform_list])

    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Tags"]) \
        .withColumn("_Tags", expr("substring(_Tags, 2, length(_Tags) - 2)")) \
        .withColumn("_Tags", split(col("_Tags"), "><")) \
        .withColumn("number_of_tags", when(size("_Tags") < 0, 0).otherwise(size("_Tags"))) \
        .withColumn("contains_language_tag", array_intersect("_Tags", language_list_col)) \
        .withColumn("contains_platform_tag", array_intersect("_Tags", platform_list_col)) \
        .withColumn("contains_language_tag", size("contains_language_tag") > 0) \
        .withColumn("contains_platform_tag", size("contains_platform_tag") > 0) \
        .drop("_Tags")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    tag_info_df(spark).show()
