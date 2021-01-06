from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, size, split


def text_features_df(spark):
    """ Extract features from the text of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id,
            number_of_characters,
            number_of_interpunction_characters,
            number_of_words,
            number_of_lines,
            interpunction_ratio,
            average_word_length,
            average_line_length
        ]
    """
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_Id', '_Text', '_PostHistoryTypeId']) \
        .filter(col('_PostHistoryTypeId') == 1) \
        .withColumn('number_of_characters', length(col('_Text'))) \
        .withColumn('number_of_interpunction_characters', size(split(col('_Text'), r'[-\[\]{}()*+?.,\\^$|#]')) - 1) \
        .withColumn('interpunction_ratio', col('number_of_interpunction_characters') / col('number_of_characters')) \
        .withColumn('number_of_lines', size(split(col('_Text'), r'\n'))) \
        .withColumn('average_line_length', col('number_of_characters') / col('number_of_lines')) \
        .withColumn('number_of_words', size(split(col('_Text'), r'\s'))) \
        .withColumn('average_word_length', col('number_of_characters') / col('number_of_words')) \
        .drop('_Text', '_PostHistoryTypeId')
    # TODO drop any more useless columns
    return df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    text_features_df(spark).show()
