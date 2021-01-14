import pickle
from sys import argv

import numpy as np
from pyspark.sql import SparkSession

if __name__ == "__main__":
    """
    Run this locally (not with --deploy-mode cluster). This will create a pickle file.
    To run: spark-submit StackOverflow/analysis/parque_to_pickle.py INPUT OUTPUT 2> /dev/null
    To copy data to local machine: scp sXXXXXXX@ctitXXX.ewi.utwente.nl:output.pickle ./analysis/local/data
    Replace INPUT with the input path where the input .parquet file can be found, and OUTPUT with the desired pickle
    filename (without an extension)
    """

    print("Converting .parquet to .pickle")
    spark = SparkSession.builder.getOrCreate()
    parquet_file = spark.read.parquet(argv[1])
    all_data = np.array(parquet_file.collect())
    pickle_data = {
        "column_names": parquet_file.columns,
        "data_points": all_data
    }

    pickle.dump(pickle_data, open(argv[2] + ".pickle", "wb"))
