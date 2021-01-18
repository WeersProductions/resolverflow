import pickle
from sys import argv
from pyspark.sql import SparkSession
import numpy as np


if __name__ == "__main__":
    """
    Run using: spark-submit --name dreamteam_pickle util/parquet_file_to_pickle.py "StackOverflow/scatter_points.parquet" 2> /dev/null
    """
    print("Converting parquet file to pickle.")
    spark = SparkSession.builder.getOrCreate()

    if len(argv) >= 2:
        print("Converting %s" % argv[1])
        df = spark.read.parquet(argv[1])

        if len(argv) > 2:
            target = argv[2]
        else:
            target = argv[1][:-8] + ".pickle" # Remove .parquet add .pickle

        all_data = np.array(df.collect())
        pickle_data = {
            "column_names": df.columns,
            "data_points": all_data
        }

        pickle.dump(pickle_data, open(target, "wb"))
        print("Saved at %s!" % target)
    else:
        print("Please provide an input .parquet file.")
