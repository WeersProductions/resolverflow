from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()


def Convert(source, destination, row_element):
    df = spark.read.format("xml").options(rowTag=row_element).load(source) \
            .filter(col("_PostTypeId") == 1)
    df.write.parquet(destination)


# To do in pyspark, start with: pyspark --packages com.databricks:spark-xml_2.11:0.11.0
# To run with submit: spark-submit --packages com.databricks:spark-xml_2.11:0.11.0 convertDataSet.py
Convert("/user/***REMOVED***/StackOverflow/Badges.xml", "/user/***REMOVED***/StackOverflow/Badges.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/Comments.xml", "/user/***REMOVED***/StackOverflow/Comments.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/PostHistory.xml", "/user/***REMOVED***/StackOverflow/PostHistory.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/PostLinks.xml", "/user/***REMOVED***/StackOverflow/PostLinks.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/Posts.xml", "/user/***REMOVED***/StackOverflow/Posts.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/Tags.xml", "/user/***REMOVED***/StackOverflow/Tags.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/Users.xml", "/user/***REMOVED***/StackOverflow/Users.parquet", "row")
Convert("/user/***REMOVED***/StackOverflow/Votes.xml", "/user/***REMOVED***/StackOverflow/Votes.parquet", "row")
