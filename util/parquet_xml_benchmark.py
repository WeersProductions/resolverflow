from pyspark.sql import SparkSession
import time


def benchmark_file(spark, xml_file, parquet_file):
    """
    Benchmark a parquet file versus the xml version.

    Args:
        xml_file (string: File path
        parquet_file (string): File path

    Returns:
        Tuple of floats: First element is the time xml took to load, second is the parquet load time.
    """
    # XML time
    xml_file = spark.read.format("xml").options(rowTag="row").load(xml_file)
    start_time = time.time()
    _ = xml_file.count()
    xml_time = time.time() - start_time

    # Parquet time
    parquet_file = spark.read.parquet(parquet_file)
    start_time = time.time()
    _ = parquet_file.count()
    parquet_time = time.time() - start_time

    return (xml_time, parquet_time)


def benchmark(spark, files):
    """
    Run a benchmark using multiple input files.

    Args:
        spark : Spark context, used to load the xml and parquet files.
        files [(<xml_file_path, parquet_file_path>), (<xml_file_path, parquet_file_path>)]: List of tuples that contain the xml and parquet version of a file.

    Returns:
        float: Average percentage of the parquet loading time versus xml loading time.
    """
    total_average_percentage = 0
    for file in files:
        xml_time, parquet_time = benchmark_file(spark, file[0], file[1])
        total_average_percentage = parquet_time / xml_time
        print(file, ": ", parquet_time, ", ", xml_time, ": ", parquet_time / xml_time)

    return total_average_percentage / len(files)


if __name__ == "__main__":
    """
    Run using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=20 --conf spark.yarn.maxAppAttempts=1 --packages com.databricks:spark-xml_2.11:0.11.0 util/parquet_xml_benchmark.py
    """
    files = [("StackOverflow/PostHistory.xml", "StackOverflow/PostHistory.parquet"),
        ("StackOverflow/Posts.xml", "StackOverflow/Posts.parquet"),
        ("StackOverflow/Users.xml", "StackOverflow/Users.parquet")]
    user = "/user/***REMOVED***/"

    spark = SparkSession.builder.getOrCreate()
    files = [(user + file[0], user + file[1]) for file in files]

    results = benchmark(spark, files)
    print("benchmark result: ", results)
