from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp
from pyspark.sql.types import LongType


def user_age_df(spark):
    df_posts = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_CreationDate", "_OwnerUserId"]) \
        .withColumnRenamed("_CreationDate", "_PostCreationDate")
    df_users = spark.read.parquet("/user/***REMOVED***/StackOverflow/Users.parquet") \
        .select(["_AccountId", "_CreationDate"]) \
        .withColumnRenamed("_CreationDate", "_UserCreationDate")
    df = df_posts \
        .join(df_users, df_posts["_OwnerUserId"] == df_users["_AccountId"]) \
        .withColumn('age', to_timestamp(col('_PostCreationDate')).cast(LongType()) - to_timestamp(col('_UserCreationDate')).cast(LongType())) \
        .select(["_Id", "age"])

    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    user_age_df(spark).show()
