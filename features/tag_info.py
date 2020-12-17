from pyspark.sql import SparkSession
from pyspark.sql.functions import array, array_intersect, col, expr, lit, size, split, when


def tag_info_df(spark):
    # Create lists of programming languages and platforms
    language_list = ["django", "php"]
    language_list_col = array(*[lit(x) for x in language_list])
    platform_list = ["windows", "linux", "maccie"]
    platform_list_col = array(*[lit(x) for x in platform_list])

    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_Tags"]) \
        .withColumn("_Tags", expr("substring(_Tags, 2, length(_Tags) - 2)")) \
        .withColumn("_Tags", split(col("_Tags"), "><")) \
        .withColumn("number_of_tags", when(size("_Tags") < 0, 0).otherwise(size("_Tags"))) \
        .withColumn("language_tag", array_intersect("_Tags", language_list_col)) \
        .withColumn("platform_tag", array_intersect("_Tags", platform_list_col)) \
        .withColumn("language_tag", size("language_tag") > 0) \
        .withColumn("platform_tag", size("platform_tag") > 0) \
        .drop("_Tags")

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    tag_info_df(spark).show()
