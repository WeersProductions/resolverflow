import pickle
import subprocess
from sys import argv

import numpy as np
from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
    Run this locally (not with --deploy-mode cluster). This will create a pickle file.
    To run: spark-submit StackOverflow/analysis/parquet_to_pickle.py INPUT_DIR 2> /dev/null
    To copy data to local machine: scp sXXXXXXX@ctitXXX.ewi.utwente.nl:output.pickle ./analysis/local/data
    Replace INPUT_DIR with the input path where the input .parquet files can be found
    """

    print("Converting .parquet to .pickle")
    spark = SparkSession.builder.getOrCreate()

    cmd = 'hdfs dfs -ls ' + argv[1]
    files = subprocess.check_output(cmd, shell=True).strip().split('\n')
    files.pop(0)

    for file_listing in files:
        file_name = file_listing.split('/')[-1]
        parquet_file = spark.read.parquet(argv[1] + file_name)
        all_data = np.array(parquet_file.collect())
        pickle_data = {
            "column_names": parquet_file.columns,
            "data_points": all_data
        }

        pickle.dump(pickle_data, open(file_name[:-8] + ".pickle", "wb"))
