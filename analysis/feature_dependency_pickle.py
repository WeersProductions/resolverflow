import pickle
from pyspark.sql import SparkSession
import numpy as np

# Run this locally (not with --deploy-mode cluster). This will create a pickle file.
# To run: spark-submit StackOverflow/analysis/feature_dependency_pickle.py 2> /dev/null
# To copy data to local machine: scp ***REMOVED***@ctit016.ewi.utwente.nl:scatter_points.pickle ./analysis/local/data
if __name__ == "__main__":
    print("Converting .parquet to .pickle")
    spark = SparkSession.builder.getOrCreate()
    scatter_points_parquet = spark.read.parquet('/user/***REMOVED***/StackOverflow/scatter_points.parquet')
    scatter_points = np.array(scatter_points_parquet.collect())
    pickle_data = {
        "column_names": scatter_points_parquet.columns,
        "scatter_points": scatter_points
    }
    pickle.dump(pickle_data, open("scatter_points.pickle", "wb"))
