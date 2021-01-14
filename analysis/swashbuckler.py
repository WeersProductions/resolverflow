from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, max
from pyspark.sql.types import IntegerType


INTEGER_FEATURES = ["title_number_of_characters", "number_of_characters", "number_of_interpunction_characters",
                    "number_of_lines", "number_of_words", "number_of_tags", "posts_amount", "answered_posts_amount"]
FLOAT_FEATURES = ["interpunction_ratio", "average_line_length", "average_word_length", "user_age", "creation_seconds"]
BOOLEAN_FEATURES = []


def mass_apply(dataframe, **functions):
    """
    Takes a dataframe of a single column, and creates a new column for every function given

    Args:
        dataframe: single-column dataframe to be processed
        **functions: all functions that are to be applied, with as key the column to be applied on

    Returns:
        dataframe with one extra column for every function that was given as input with its results
    """

    return dataframe.agg(**functions)


def create_parquet_files(spark_session):
    """
    Create a histogram for each feature

    Args:
        spark_session: dataframe to be processed

    Returns:
        dataframe
    """

    all_features = spark_session.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    all_features = all_features.filter(all_features["is_question"])

    all_results = []

    for feature in INTEGER_FEATURES + FLOAT_FEATURES:
        original_feature = feature
        if feature in FLOAT_FEATURES:
            # Bucketize each float feature into "${feature}_bucket_index" columns
            feature += '_bucket_index'
            window = Window.partitionBy(original_feature) \
                .rowsBetween(Window.unboundedPreceding, Window.unboundedFollowing)

            all_features = all_features.withColumn(feature,
                                    (col(original_feature) / max(col(original_feature)).over(window) * 100000)
                                    .cast(IntegerType()))  # TODO: fine-tune the bucket count

        for resolved in [True, False]:
            new_file = all_features.filter(col('has_answer') == resolved) \
                .select(feature) \
                .groupBy(feature).count()

            filename = original_feature + '_1' if resolved else original_feature + '_0'
            new_file.write.mode('overwrite')\
                .parquet('/user/***REMOVED***/StackOverflow/swashbuckler/output_' + filename + '.parquet')

    return all_results


if __name__ == "__main__":
    print("Creating histogram plots")
    spark = SparkSession.builder.getOrCreate()

    create_parquet_files(spark)
