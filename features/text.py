from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, split, size, array_join, regexp_replace
import regex


def text_formatting(spark):
    """ Extract formatting features from the text of a post

    Args:
        spark (SparkSession): used to run queries and commands

    Returns:
        DataFrame: With columns [
            (post)_Id,
            #codelines,
            #html_blocks,
            #headings,
            #referencelist,
            #quotes,
            #codeblocks,
            #themebreaks,
            #codespans,
            #references,
            #links,
            #inline_images,
            #mail_addresses,
            #emphasis,
            #strong
        ]
    """
    # Replaces formatted text that has already been processed
    FILLER = 'x'
    # Parser helper column
    COLNAME = 'processed_text'
    COL = col(COLNAME)

    # Data loading
    post_history_df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_PostId', '_Text', '_PostHistoryTypeId']) \
        .filter(col('_PostHistoryTypeId') == 2) \
        .drop('_PostHistoryTypeId')
    post_df = spark.read.parquet('/user/***REMOVED***/StackOverflow/Posts.parquet') \
        .select(['_Id', '_PostTypeId']) \
        .filter(col('_PostTypeId') == 1) \
        .drop("_PostTypeId")
    df = post_history_df.join(post_df, post_df['_Id'] == post_history_df['_PostId'])

    # Count lines and words of the formatted text
    df = df.withColumn('#lines', size(split(col('_Text'), r'\n'))) \
        .withColumn('#words', size(split(col('_Text'), r'\s+')))

    # BLOCK ELEMENTS
    # Count code lines
    df = df.withColumn(COLNAME, split(col('_Text'), regex.CODE_BLOCK_RE)) \
        .withColumn('#codelines', size(COL) - 1) \
        .withColumn('codeline_ratio', col('#codelines') / col('#lines')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count HTML blocks
    df = df.withColumn(COLNAME, split(COL, regex.HTML_BLOCK_RE)) \
        .withColumn('#html_blocks', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # # Count headings (1/2)
    df = df.withColumn(COLNAME, split(COL, regex.SETEXT_HEADING_RE)) \
        .withColumn('#headings', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count reference list
    df = df.withColumn(COLNAME, split(COL, regex.REFERENCE_LIST_RE)) \
        .withColumn('#referencelist', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count quotes
    df = df.withColumn(COLNAME, split(COL, regex.QUOTE_RE)) \
        .withColumn('#quotes', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count headings (2/2)
    df = df.withColumn(COLNAME, split(COL, regex.HEADING_RE)) \
        .withColumn('#headings', size(COL) - 1 + col('#headings')) \
        .withColumn('heading_ratio', col('#headings') / col('#lines')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count code blocks
    df = df.withColumn(COLNAME, split(COL, regex.FENCED_CODE_RE)) \
        .withColumn('#codeblocks', size(COL) - 1) \
        .withColumn('codeblock_ratio', col('#codeblocks') / col('#lines')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count thematic break
    df = df.withColumn(COLNAME, split(COL, regex.THEME_BREAK_RE)) \
        .withColumn('#themebreaks', size(COL) - 1) \
        .withColumn('themebreak_ratio', col('#themebreaks') / col('#lines')) \
        .withColumn(COLNAME, array_join(COL, FILLER))

    # INLINE ELEMENTS
    # Count codespans
    df = df.withColumn(COLNAME, split(COL, regex.CODESPAN_RE)) \
        .withColumn('#codespans', size(COL) - 1) \
        .withColumn('codespan_ratio', col('#codespans') / col('#words')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Remove markdown escapes
    df = df.withColumn(COLNAME, regexp_replace(COL, regex.ESCAPE_RE, FILLER))
    # Count references (1/2)
    df = df.withColumn(COLNAME, split(COL, regex.REFERENCE_RE)) \
        .withColumn('#references', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count links (1/2)
    df = df.withColumn(COLNAME, split(COL, regex.LINK_RE)) \
        .withColumn('#links', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count inline images
    df = df.withColumn(COLNAME, split(COL, regex.INLINE_IMAGE_RE)) \
        .withColumn('#inline_images', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # # Count references (2/2)
    df = df.withColumn(COLNAME, split(COL, regex.SHORT_REFERENCE_RE)) \
        .withColumn('#references', size(COL) - 1 + col('#references')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count links (2/2)
    df = df.withColumn(COLNAME, split(COL, regex.AUTOLINK_RE)) \
        .withColumn('#links', size(COL) - 1 + col('#links')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    # Count mails
    df = df.withColumn(COLNAME, split(COL, regex.AUTOMAIL_RE)) \
        .withColumn('#mail_addresses', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
        
    # Remove line breaks, html, stand-alone * or _
    df = df.withColumn(COLNAME, regexp_replace(COL, regex.LINE_BREAK_RE, FILLER))
    df = df.withColumn(COLNAME, regexp_replace(COL, regex.HTML_RE, FILLER))
    df = df.withColumn(COLNAME, regexp_replace(COL, regex.NOT_STRONG_RE, FILLER))
    # Count strong & emphasis
    df = df.withColumn(COLNAME, split(COL, regex.EM_STRONG_RE)) \
        .withColumn('#emphasis', size(COL) - 1) \
        .withColumn('#strong', size(COL) - 1) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.STRONG_EM_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.STRONG_EM3_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.STRONG_RE)) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.EMPHASIS_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.EM_STRONG2_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.STRONG2_RE)) \
        .withColumn('#strong', size(COL) - 1 + col('#strong')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn(COLNAME, split(COL, regex.EMPHASIS2_RE)) \
        .withColumn('#emphasis', size(COL) - 1 + col('#emphasis')) \
        .withColumn(COLNAME, array_join(COL, FILLER))
    df = df.withColumn('emphasis_ratio', col('#emphasis') / col('#words')) \
        .withColumn('strong_ratio', col('#strong') / col('#words'))

    # Remove unnecessary columns, including parser helper column
    df = df.drop('_Text', '_PostHistoryTypeId', '_PostId', '#lines', '#words', COLNAME)
    return df
