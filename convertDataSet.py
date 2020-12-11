from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder.getOrCreate()

# Create DF, which loads schema.
postsDF = spark.read.format("xml").load("/data/stackoverflow/posts.zip")
# Write DataFrame for later use.
postsDF.write.parquet("stackoverflow/posts.parquet")