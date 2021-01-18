from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, split, size, array_join, regexp_replace
from regex import *

spark = SparkSession.builder.getOrCreate()


def text_formatting(spark):
    # Replaces formatted text that has already been processed
    FILLER = 'x'
    # Parser helper column
    COLNAME = 'processed_text'
    COL =  col(COLNAME)
    
    # Load and filter
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_PostId', '_Text', '_PostHistoryTypeId']) \
        .withColumnRenamed('_PostId', '_Id') \
        .filter(col('_PostHistoryTypeId') == 2)
    
    # BLOCK ELEMENTS
    # Count code blocks (1/2)
    df = df.withColumn(COLNAME, split(col('_Text'), CODE_BLOCK_RE)) \
        .withColumn('#codeblocks', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count HTML blocks
    df = df.withColumn(COLNAME, split(COL, HTML_BLOCK_RE)) \
        .withColumn('#html_blocks', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # # Count headings (1/2)
    df = df.withColumn(COLNAME, split(COL, SETEXT_HEADING_RE)) \
        .withColumn('#headings', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count reference list
    df = df.withColumn(COLNAME, split(COL, REFERENCE_LIST_RE)) \
        .withColumn('#referencelist', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count quotes
    df = df.withColumn(COLNAME, split(col('_Text'), QUOTE_RE)) \
        .withColumn('#quotes', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count headings (2/2)
    df = df.withColumn(COLNAME, split(COL, HEADING_RE)) \
        .withColumn('#headings', size(COL) - 1 + col('#headings')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count code blocks (2/2)
    df = df.withColumn(COLNAME, split(COL, FENCED_CODE_RE)) \
        .withColumn('#codeblocks', size(COL) - 1 + col('#codeblocks')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count thematic break
    df = df.withColumn(COLNAME, split(COL, THEME_BREAK_RE)) \
        .withColumn('#themebreaks', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    
    # INLINE ELEMENTS
    # Count codespans
    df = df.withColumn(COLNAME, split(COL, CODESPAN_RE)) \
        .withColumn('#codespans', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Remove markdown escapes
    df = df.withColumn(COLNAME, regexp_replace(COL, ESCAPE_RE, FILLER))
    # Count references (1/2)
    df = df.withColumn(COLNAME, split(COL, REFERENCE_RE)) \
        .withColumn('#references', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count links (1/2)
    df = df.withColumn(COLNAME, split(COL, LINK_RE)) \
        .withColumn('#links', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count inline images
    df = df.withColumn(COLNAME, split(COL, INLINE_IMAGE_RE)) \
        .withColumn('#inline_images', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # # Count references (2/2)
    df = df.withColumn(COLNAME, split(COL, SHORT_REFERENCE_RE)) \
        .withColumn('#references', size(COL) - 1 + col('#references')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count links (2/2)
    df = df.withColumn(COLNAME, split(COL, AUTOLINK_RE)) \
        .withColumn('#links', size(COL) - 1 + col('#links')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count mails
    df = df.withColumn(COLNAME, split(COL, AUTOMAIL_RE)) \
        .withColumn('#mail_addresses', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Remove line breaks, html, stand-alone * or _
    df = df.withColumn(COLNAME, regexp_replace(COL, LINE_BREAK_RE, FILLER))
    df = df.withColumn(COLNAME, regexp_replace(COL, HTML_RE, FILLER))
    df = df.withColumn(COLNAME, regexp_replace(COL, NOT_STRONG_RE, FILLER))
    # Count strong & emphasis
    df = df.withColumn(COLNAME, split(COL, EM_STRONG_RE)) \
        .withColumn('#emphasis', size(COL) - 1) \
        .withColumn('#strong', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, STRONG_EM_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, STRONG_EM3_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, STRONG_RE)) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, EMPHASIS_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, EM_STRONG2_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, STRONG2_RE)) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, EMPHASIS2_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    
    # Remove parser helper column
    df = df.drop(COLNAME)
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
