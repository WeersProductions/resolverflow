from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, udf, split, size, array_join
# import marko
# from collections import Counter

spark = SparkSession.builder.getOrCreate()


# Preprocessing

def text_preprocess():
    text = None
    # e.g. to lowercase
    return text


# Features

# --- REGEX ---
# Patterns from two sources:
# - Copyright 2007, 2008 The Python Markdown Project (v. 1.7 and later) Copyright 2004, 2005, 2006 Yuri Takhteyev (v. 0.2-1.6b) Copyright 2004 Manfred Stienstra (the original version)
# - Marko. A markdown parser with high extensibility. Author: Frost Ming <mianghong@gmail.com>
EMPHASIS_RE = r'(\*)([^\*]+)\1'
CODESPAN_RE = r'(?:(?<!\\)((?:\\{2})+)(?=`+)|(?<!\\)(`+)(.+?)(?<!`)\2(?!`))'
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
        .withColumn('processed_text', array_join(col('processed_text'), FILLER))
    return df
        # .withColumn('text_length', length(col('_Text'))) \
        # .withColumn('formatting', count_formatting_udf(col('_Text')))



# def count_formatting(text):
#     ''' Parses the text as Markdown and returns count of each formatting type '''

#     def get_children_types(elem):
#         ''' For a markdown parse tree node, get the types of its children '''
#         if hasattr(elem, 'children'):
#             children = elem.children
#         else:
#             children = []
        
#         if type(children) == list:      # Children
#             result = Counter([get_format_type(child) for child in children])
#             for child in children:
#                 result += get_children_types(child)
#         elif type(children) != str:     # Single child
#             result = Counter([get_format_type(children)])
#         else:                           # No children
#             result = Counter()
#         return result

#     def get_format_type(elem):
#         ''' For a markdown parse tree node get its formatting type '''
#         return elem.__class__.__name__

#     if text is not None:
#         string_text = text.encode("utf8")
#     else:
#         string_text = ""
        
#     md_tree = marko.parse(string_text)
#     md_types = get_children_types(md_tree)
#     return dict(md_types).__str__()


def has_bold():
    return False


def has_italic():
    return False


def has_underline():
    return False


def has_headers():
    return False


def has_strike():
    return False


def has_bulletlists():
    return False


def has_numlists():
    return False


def has_links():
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
