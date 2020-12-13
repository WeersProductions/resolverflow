from pyspark.sql import SparkSession
from pyspark.sql.functions import explode

spark = SparkSession.builder.getOrCreate()

def Convert(source, destination, row_element):
    df = spark.read.format("xml").options(rowTag=row_element).load(source)
    df.write.parquet(destination)


# To do in pyspark, start with: pyspark --packages com.databricks:spark-xml_2.11:0.11.0
Convert("Badges.xml", "Badges.parquet", "row")