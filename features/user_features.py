from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, sum
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


def user_question_amount(spark):
    """
    Calculate the amount of questions a user has made before a post is created.
    """
    df_posts = spark.read.parquet("/user/***REMOVED***/StackOverflow/Posts.parquet") \
        .select(["_Id", "_OwnerUserId", "_CreationDate"]) \
        .withColumn('CreationTimestamp', to_timestamp(col("_CreationDate")).cast(LongType())) \
        .drop("_CreationDate")
    # Renaming columns for self join.
    df_post_count = df_posts
    for c in df_posts.columns:
        df_post_count = df_post_count if c == '_OwnerUserId' else df_post_count.withColumnRenamed(c, 'x_{cl}'.format(cl=c))

    result = df_posts.join(df_post_count, '_OwnerUserId')
    # Count the amount of posts before this post was made.
    result = result.withColumn('posts_amount', when(col('CreationTimestamp') < col('x_CreationTimestamp'), 1).otherwise(0)).groupBy(['_Id', 'CreationTimestamp']).agg(sum('posts_amount').alias('posts_amount'))
    result = result.drop("CreationTimestamp")
    return result


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    # user_age_df(spark).show()
    user_question_amount(spark).show()
