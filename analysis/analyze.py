from pyspark.sql import SparkSession
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler


def load_feature_data(spark):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.drop('_CreationDate')
    return feature_data


def calc_correlation(spark):
    """

    Example result:
    Starting analysis.
    DenseMatrix([[ 1.        , -0.02928137,  0.1439355 ,  0.99713413,  0.01726689,
              -0.04217593, -0.01772163,  0.35603309, -0.19260691],
             [-0.02928137,  1.        ,  0.20510788, -0.03353036, -0.01087837,
              -0.02527855,  0.00950739,  0.02436108,  0.05474339],
             [ 0.1439355 ,  0.20510788,  1.        ,  0.14287865,  0.08616968,
              -0.03689131,  0.00262839,  0.07985796, -0.01802226],
             [ 0.99713413, -0.03353036,  0.14287865,  1.        ,  0.01809543,
              -0.04080357, -0.01824413,  0.35537495, -0.19835699],
             [ 0.01726689, -0.01087837,  0.08616968,  0.01809543,  1.        ,
               0.0438001 ,  0.0758663 ,  0.01669125, -0.00117598],
             [-0.04217593, -0.02527855, -0.03689131, -0.04080357,  0.0438001 ,
               1.        , -0.02133353, -0.0556705 , -0.00313233],
             [-0.01772163,  0.00950739,  0.00262839, -0.01824413,  0.0758663 ,
              -0.02133353,  1.        , -0.00302532,  0.00215611],
             [ 0.35603309,  0.02436108,  0.07985796,  0.35537495,  0.01669125,
              -0.0556705 , -0.00302532,  1.        ,  0.01096396],
             [-0.19260691,  0.05474339, -0.01802226, -0.19835699, -0.00117598,
              -0.00313233,  0.00215611,  0.01096396,  1.        ]])
    """
    feature_data = load_feature_data(spark)
    vector_col = "features"
    assembler = VectorAssembler(inputCols=feature_data.columns, outputCol=vector_col)
    df_vector = assembler.transform(feature_data).select(vector_col)
    corr_mat = Correlation.corr(df_vector, vector_col).head()
    print(str(corr_mat[0]))


if __name__ == "__main__":
    """
    Run using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --name dreamteam analysis/analyze.py 2> /dev/null
    """

    print("Starting analysis.")
    spark = SparkSession.builder.getOrCreate()
    calc_correlation(spark)
