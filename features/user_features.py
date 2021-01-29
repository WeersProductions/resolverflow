from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, when, sum, count
from pyspark.sql.types import LongType


def user_age_df(spark):
    """
    Calculate the age of the user when he made a post.

    Args:
        spark ([type]): [description]

    Returns:
        DataFrame: With columns [
            (post)_Id, user_age
        ]
    """
    df_posts = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_CreationDate', '_OwnerUserId']) \
        .withColumnRenamed('_CreationDate', '_PostCreationDate')
    df_users = spark.read.parquet('/user/***REMOVED***/StackOverflow/Users.parquet') \
        .select(['_Id', '_CreationDate']) \
        .withColumnRenamed('_CreationDate', '_UserCreationDate') \
        .withColumnRenamed('_Id', 'UserId')
    df = df_posts \
        .join(df_users, df_posts["_OwnerUserId"] == df_users["UserId"]) \
        .withColumn("user_age", to_timestamp(col("_PostCreationDate")).cast(LongType()) - to_timestamp(
        col("_UserCreationDate")).cast(LongType())) \
        .select(["_Id", "user_age"])

    return df


def user_question_amount(spark):
    """
    Calculate the amount of questions a user has made and how many have been answered before a post is created.

    Returns:
        DataFrame: With columns [
            (post)_Id, #posts, #answered_posts
        ]
    """
    df_posts = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_OwnerUserId', '_CreationDate', '_AcceptedAnswerId', '_PostTypeId']) \
        .where(col('_PostTypeId') == 1) \
        .withColumn('CreationTimestamp', to_timestamp(col('_CreationDate')).cast(LongType())) \
        .drop('_CreationDate', '_PostTypeId')

    # Renaming columns for self join.
    df_post_count = df_posts
    for c in df_posts.columns:
        df_post_count = df_post_count if c == '_OwnerUserId' else df_post_count.withColumnRenamed(c,
                                                                                                  'x_{cl}'.format(cl=c))

    result = df_posts.join(df_post_count, '_OwnerUserId')
    # Count the amount of posts before this post was made.
    result = result.withColumn('#posts',
                               when(col('CreationTimestamp') < col('x_CreationTimestamp'), 1).otherwise(0)).groupBy(
        ['_Id', '_OwnerUserId', 'CreationTimestamp']).agg(sum('#posts').alias('#posts'))
    # Count the amount of answered posts before this post was made
    result = result.join(df_post_count, '_OwnerUserId')
    result = result.withColumn('#answered_posts', when(
        (col('CreationTimestamp') < col('x_CreationTimestamp')) & col('x__AcceptedAnswerId').isNotNull(), 1).otherwise(
        0)).groupBy(['_Id', 'CreationTimestamp', '#posts']).agg(sum('#answered_posts').alias('#answered_posts'))
    result = result.drop('CreationTimestamp')

    return result


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()
    user_question_amount(spark).show()
