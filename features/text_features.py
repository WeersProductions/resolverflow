from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, size, split, when, regexp_replace
import regex


def text_features_df(spark):
    """ Extract features from the text of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id,
            #characters,
            #punctuation_characters,
            #words,
            #lines,
            punctuation_ratio,
            average_word_length,
            average_line_length
        ]
    """
    # Replaces formatted text that has already been processed
    FILLER = ''
    # Parser helper column
    COLNAME = 'processed_text'
    COL = col(COLNAME)
    
    # Data loading
    post_history_df = spark.read.parquet("/user/s*******/StackOverflow/PostHistory.parquet") \
        .select(['_PostId', '_Text', '_PostHistoryTypeId']) \
        .filter(col('_PostHistoryTypeId') == 2) \
        .drop('_PostHistoryTypeId')
    post_df = spark.read.parquet('/user/s*******/StackOverflow/Posts.parquet') \
        .select(['_Id', '_PostTypeId']) \
        .filter(col('_PostTypeId') == 1) \
        .drop("_PostTypeId")
    df = post_history_df.join(post_df, post_df['_Id'] == post_history_df['_PostId'])

    # Remove code snippets from the Markdown formatted text
    df = df.withColumn(COLNAME, regexp_replace(col('_Text'), regex.CODE_BLOCK_RE, FILLER)) \
        .withColumn(COLNAME, regexp_replace(COL, regex.HTML_BLOCK_RE, FILLER)) \
        .withColumn(COLNAME, regexp_replace(COL, regex.FENCED_CODE_RE, FILLER)) \
        .withColumn(COLNAME, regexp_replace(COL, regex.ESCAPE_RE, FILLER)) \
        .withColumn(COLNAME, regexp_replace(COL, regex.HTML_RE, FILLER))

    # Calculate features
    df = df.withColumn('#characters', length(COL)) \
        .withColumn('#punctuation_characters', size(split(COL, r'[-\[\]{}()*+?.,\\^$|#]')) - 1) \
        .withColumn('punctuation_ratio', col('#punctuation_characters') / col('#characters')) \
        .withColumn('#lines', size(split(COL, r'\n'))) \
        .withColumn('average_line_length', col('#characters') / col('#lines')) \
        .withColumn('#words', size(split(COL, r'\s+'))) \
        .withColumn('average_word_length', col('#characters') / col('#words'))

    # Remove unnecessary columns, including parser helper column
    df = df.drop('_Text', '_PostHistoryTypeId', '_PostId', COLNAME)
    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    text_features_df(spark).show()
