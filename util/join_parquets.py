import sys
from pyspark.sql import SparkSession
from pyspark.sql.functions import col


def join_parquets(spark, *parquet_files):
    """
    Join multiple parquets files together on the '_Id' column.
    Args:
        parquet_files: list of strings referring to .parquet files.

    Returns:
        dataframe: all .parquet files joined into a single dataframe.
    """
    result = None
    for parquet_file in parquet_files:
        df = spark.read.parquet(parquet_file)
        if result is None:
            result = df
        else:
            result = result.join(df, "_Id")

    return result


if __name__ == "__main__":
    """
    Run using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --conf spark.yarn.maxAppAttempts=1 --name dreamteam util/join_parquets.py --file "StackOverflow/output_stackoverflow.parquet" 2> /dev/null
    """
    spark = SparkSession.builder.getOrCreate()
    merged = join_parquets(spark, "/user/***REMOVED***/StackOverflow/output_stackoverflow2.parquet", "/user/***REMOVED***/StackOverflow/output_stackoverflow_textformatting_ratiosgood.parquet")
    if len(sys.argv) > 2 and sys.argv[1] == '--file':
        merged.write.mode("overwrite").parquet(sys.argv[2])
    else:
        merged.show()
