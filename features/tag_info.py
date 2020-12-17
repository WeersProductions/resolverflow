from pyspark.sql import SparkSession
from pyspark.sql.functions import expr, split, size, array_intersect, when, array, lit

spark = SparkSession.builder.getOrCreate()


def tag_info():
    # A list of all programming languages
    language_list = ["django", "php"]

    # Create a column list of programming languages
    language_list_col = array(*[lit(x) for x in language_list])

    # A list of all platforms
    platform_list = ["windows", "linux", "maccie"]

    # Create a column list of programming languages
    platform_list_col = array(*[lit(x) for x in platform_list])

    # Get the right columns from the dataset
    df1 = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet").select(["_Id", "_Tags"])

    # Remove first and last character from tag String
    df2 = df1.withColumn("_Tags", expr("substring(_Tags, 2, length(_Tags) - 2)"))

    # Split the tag String
    df3 = df2.withColumn("_Tags", split(df2["_Tags"], "><"))

    # Get the number of tags
    df4 = df3.withColumn("number_of_tags", when(size("_Tags") < 0, 0).otherwise(size("_Tags")))

    # Match the tags with the list of languages
    df5 = df4.withColumn("language_tag", array_intersect("_Tags", language_list_col))

    # Match the tags with the list of platforms
    df6 = df5.withColumn("platform_tag", array_intersect("_Tags", platform_list_col))

    # Check if the tags contain any languages
    df7 = df6.withColumn("language_tag", size("language_tag") > 0)

    # Check if the tags contain any platforms
    df8 = df7.withColumn("platform_tag", size("platform_tag") > 0)

    df9 = df8.drop("_Tags")

    return df9
