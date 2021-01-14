from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, udf, split, size, array_join, regexp_replace
import re

spark = SparkSession.builder.getOrCreate()


# Preprocessing

def text_preprocess():
    text = None
    # e.g. to lowercase
    return text


# Features

# --- REGEX ---
# Patterns from two sources. Alterations made by us.
# - Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later) Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b) Copyright 2004 Manfred Stienstra (the original version)
# - Marko. A markdown parser with high extensibility. Author: Frost Ming <mianghong@gmail.com>

# Inline elements:
# These are noted in order of precedence.
NOIMG = r'(?<!\!)'
BRACKETED = r'\[([^\]]*)\]'
LINK_START_RE = NOIMG + BRACKETED
IMAGE_START_RE = r'\!' + BRACKETED
LINK_END_RE = re.compile(r'''\(\s*(?:(<[^<>]*>)\s*(?:('[^']*'|"[^"]*")\s*)?\))?''', re.DOTALL | re.UNICODE)
REFERENCE_END_RE = re.compile(r'\s?' + BRACKETED, re.DOTALL | re.UNICODE)

# `e=f()` or ``e=f("`")``
CODESPAN_RE = r'(?:(?<!\\)((?:\\{2})+)(?=`+)|(?<!\\)(`+)(.+?)(?<!`)\2(?!`))'
# \<
ESCAPE_RE = r'\\(.)'
# [Google][3]
REFERENCE_RE = LINK_START_RE + REFERENCE_END_RE
# [text](url) or [text](<url>) or [text](url "title")
LINK_RE = LINK_START_RE + LINK_END_RE
# ![alttxt](http://x.com/) or ![alttxt](<http://x.com/>)
IMAGE_LINK_RE = IMAGE_START_RE + LINK_END_RE # image link
# ![alt text][2]
IMAGE_REFERENCE_RE = IMAGE_START_RE + REFERENCE_END_RE  # image ref
# [Google]
REFERENCE_RE = LINK_START_RE # short ref
# ![ref]
IMAGE_REFERENCE_RE = IMAGE_START_RE # short image ref
# <http://www.123.com>
AUTOLINK_RE = r'<((?:[Ff]|[Hh][Tt])[Tt][Pp][Ss]?://[^<>]*)>'
# <me@example.com>
AUTOMAIL_RE = r'<([^<> !]*@[^@<> ]*)>'
# two spaces at end of line
LINE_BREAK_RE = r'  \n'
# <...>
HTML_RE = r'(<([a-zA-Z/][^<>]*|!--(?:(?!<!--|-->).)*--)>)' #TODO this now finds start tags, end tags, and self-closing tags. Change that a start+end tag pair count as 1.
ENTITY_RE = r'(&(?:\#[0-9]+|\#x[0-9a-fA-F]+|[a-zA-Z0-9]+);)' # ampersands in HTML
# stand-alone * or _
NOT_STRONG_RE = r'((^|\s)(\*|_)(\s|$))' #TODO check if these need attention, it seems they are just ignored
# Asterisks
# ***strongem*** or ***em*strong**
EM_STRONG_RE = re.compile(r'(\*)\1{2}(.+?)\1(.*?)\1{2}', re.DOTALL | re.UNICODE)
# ***strong**em*
STRONG_EM_RE = re.compile(r'(\*)\1{2}(.+?)\1{2}(.*?)\1', re.DOTALL | re.UNICODE)
# **strong*em***
STRONG_EM3_RE = re.compile(r'(\*)\1(?!\1)([^*]+?)\1(?!\1)(.+?)\1{3}', re.DOTALL | re.UNICODE)
# **strong**
STRONG_RE = re.compile(r'(\*{2})(.+?)\1', re.DOTALL | re.UNICODE)
# *emphasis*
EMPHASIS_RE = re.compile(r'(\*)([^\*]+)\1', re.DOTALL | re.UNICODE)
# Underscores
# ___strongem___ or ___em_strong__
EM_STRONG2_RE = re.compile(r'(_{3})(.+?)\1', re.DOTALL | re.UNICODE)
# __strong__
STRONG2_RE = re.compile(r'(_{2})(.+?)\1', re.DOTALL | re.UNICODE)
# _emphasis_
EMPHASIS2_RE = re.compile(r'(_)([^_]+)\1', re.DOTALL | re.UNICODE)



# Precedence: you start with the highest number = highest priority

# Block elements:
    # 1
    # Paragraph
    # 2
    # 3
    # 4
    # CodeBlock
    # 5
    # HTMLBlock
    # SetextHeading
    # ListItem
    # LinkRefDef
    # BlankLine
    # Document = virtual
    # 6
    # Quote
    # Heading
    # List
    # 7
    # FencedCode
    # 8
    # ThematicBreak

# Replaces formatted text that has already been processed
FILLER = 'x'


def text_formatting(spark):
    count_formatting_udf = udf(lambda text: count_formatting(text))
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_Id', '_Text', '_PostHistoryTypeId']) \
        .filter(col('_PostHistoryTypeId') == 2) \
        .withColumn('processed_text', split(col('_Text'), CODESPAN_RE)) \
        .withColumn('#codespans', size(col('processed_text')) - 1) \
        .withColumn('processed_text', array_join(col('processed_text'), FILLER)) \
        .withColumn('processed_text', regexp_replace(col('processed_text'), ESCAPE_RE, FILLER))
    return df
        # .withColumn('text_length', length(col('_Text'))) \
        # .withColumn('formatting', count_formatting_udf(col('_Text')))



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
