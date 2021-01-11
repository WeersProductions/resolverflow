from pyspark.sql import SparkSession
from pyspark.sql.functions import col, length, udf
import marko
from collections import Counter

spark = SparkSession.builder.getOrCreate()


# Preprocessing

def text_preprocess():
    text = None
    # e.g. to lowercase
    return text


# Features


def text_length_and_formatting(spark):
    count_formatting_udf = udf(lambda text: count_formatting(text))
    df = spark.read.parquet("/user/***REMOVED***/StackOverflow/PostHistory.parquet") \
        .select(['_Id', '_Text', '_PostHistoryTypeId']) \
        .filter(col('_PostHistoryTypeId') == 6) \
        .withColumn('text_length', length(col('_Text'))) \
        .withColumn('formatting', count_formatting_udf(col('_Text')))
        # .withColumn('has_rules', col('_Text').contains('---')) \
    # TODO: for has rules, check it's succeeded by whitespace, and whether it's not part of code or quotes
    return df

def count_formatting(text):
    ''' Parses the text as Markdown and returns count of each formatting type '''

    def get_children_types(elem):
        ''' For a markdown parse tree node, get the types of its children '''
        if hasattr(elem, 'children'):
            children = elem.children
        else:
            children = []
        
        if type(children) == list:      # Children
            result = Counter([get_format_type(child) for child in children])
            for child in children:
                result += get_children_types(child)
        elif type(children) != str:     # Single child
            result = Counter([get_format_type(children)])
        else:                           # No children
            result = Counter()
        return result

    def get_format_type(elem):
        ''' For a markdown parse tree node get its formatting type '''
        return elem.__class__.__name__

    if text is not None:
        string_text = text.encode("utf8")
    else:
        string_text = ""
        
    md_tree = marko.parse(string_text)
    md_types = get_children_types(md_tree)
    return dict(md_types).__str__()


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
