from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# If true, the original data is modified before writing back to disk.
apply_filters = True

spark = SparkSession.builder.getOrCreate()

"""
    filter: if filter is provided, this is executed before writing to parquet.
    Example: Convert("/user/s*******/StackOverflow/Posts.xml", "/user/s*******/StackOverflow/Posts.parquet", "row", col("_PostTypeId") == 1)
"""


def Convert(source, destination, row_element, filter):
    df = spark.read.format("xml").options(rowTag=row_element).load(source)
    if apply_filters and filter is not None:
        df = df.filter(filter)
    df.write.parquet(destination)


if __name__ == "__main__":
    # To do in pyspark, start with: pyspark --packages com.databricks:spark-xml_2.11:0.11.0
    # To run with submit: spark-submit --packages com.databricks:spark-xml_2.11:0.11.0 convertDataSet.py
    Convert("/user/s*******/StackOverflow/Badges.xml", "/user/s*******/StackOverflow/Badges.parquet", "row")
    Convert("/user/s*******/StackOverflow/Comments.xml", "/user/s*******/StackOverflow/Comments.parquet", "row")
    Convert("/user/s*******/StackOverflow/PostHistory.xml", "/user/s*******/StackOverflow/PostHistory.parquet", "row")
    Convert("/user/s*******/StackOverflow/PostLinks.xml", "/user/s*******/StackOverflow/PostLinks.parquet", "row")
    Convert("/user/s*******/StackOverflow/Posts.xml", "/user/s*******/StackOverflow/Posts.parquet", "row")
    Convert("/user/s*******/StackOverflow/Tags.xml", "/user/s*******/StackOverflow/Tags.parquet", "row")
    Convert("/user/s*******/StackOverflow/Users.xml", "/user/s*******/StackOverflow/Users.parquet", "row")
    Convert("/user/s*******/StackOverflow/Votes.xml", "/user/s*******/StackOverflow/Votes.parquet", "row")
    pass
