from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def count_total(dataset):
    print("total: %s" % dataset.count())


def count_unresolved(dataset):
    print("unresolved: %s" % dataset.filter(col("has_answer")).count())


if __name__ == "__main__":
    """
    Run using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --conf spark.yarn.maxAppAttempts=1 --name dreamteam util/count_resolved.py 2> /dev/null
    """
    spark = SparkSession.builder.getOrCreate()

    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    count_total(df)
    count_unresolved(df)
