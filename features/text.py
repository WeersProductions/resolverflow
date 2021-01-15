from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, split, size, array_join, regexp_replace
from regex import *

spark = SparkSession.builder.getOrCreate()



def text_formatting(spark):
    # Replaces formatted text that has already been processed
    FILLER = 'x'
    
    # Load and filter
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_PostId', '_Text', '_PostHistoryTypeId']) \
        .withColumnRenamed('_PostId', '_Id') \
        .filter(col('_PostHistoryTypeId') == 2)
    # Count codespans
    df = df.withColumn('processed_text', split(col('_Text'), CODESPAN_RE)) \
        .withColumn('#codespans', size(col('processed_text')) - 1) \
        .withColumn('processed_text', array_join(col('processed_text'), FILLER))
    # Remove markdown escapes
    df = df.withColumn('processed_text', regexp_replace(col('processed_text'), ESCAPE_RE, FILLER))
    # Count inline images
    df = df.withColumn('processed_text', split(col('processed_text'), INLINE_IMAGE_RE)) \
        .withColumn('#inline_images', size(col('processed_text')) - 1) \
        .withColumn('processed_text', array_join(col('processed_text'), FILLER))
    # Remove parser helper column
    df = df.drop('processed_text')
    return df



def has_underline():
    return False

def has_strike():
    return False

def has_greetings():
    return False


def has_examples():
    ''' Mentions 'example', 'foo', 'bar', 'hello world', 'Alice', 'Bob'.
        But this might be mentioned in other ways that do not signify a user-given
        example. E.g. such keyword could be provided by default in someone's dataset. '''
    return False


def ratio_newlines():
    return 0.0


def ratio_code():
    return 0.0


def no_edits():
    ''' Number of edits. Also interesting could be ratio of edits in a timeframe.
        Or treat it as a timeseries. '''
    return 0


# More advanced stuff

def ratio_typos():
    ''' Measure of quality of spelling and/or grammar. '''
    return 0.0


def text_understandability():
    ''' Take an existing NLP measure for readability. It can be very simple, using
        the average sentence length or word length. '''
    return 0.0
