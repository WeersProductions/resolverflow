from pyspark.sql import SparkSession, Window
from pyspark.sql.functions import col, max
from pyspark.sql.types import IntegerType

PLOT_GRAPHS = False

if PLOT_GRAPHS:
    pass

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


def create_parquet(spark_session):
    """
    Create a histogram for each feature

    Args:
        spark_session: dataframe to be processed

    Returns:
        dataframe
    """

    all_features = spark_session.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    all_features = all_features.filter(all_features["is_question"])

    for feature in INTEGER_FEATURES + FLOAT_FEATURES:
        if feature in FLOAT_FEATURES:
            # Bucketize each float feature into "${feature}_bucket_index" columns
            original_feature = feature
            feature += '_bucket_index'
            window = Window.partitionBy(original_feature).rowsBetween(Window.unboundedPreceding,
                                                                      Window.unboundedFollowing)
            all_features.withColumn(feature,
                                    (col(original_feature) / max(col(original_feature)).over(window) * 100000)
                                    .cast(IntegerType()))
            # TODO: fine-tune the bucket count (read: how high can we go?)

        # FIXME: dit moet niet meer per feature zijn ofzo want het moet gedumpt worden naar een parqet bestand
        for resolved in [True, False]:
            feature_data = all_features.filter(col('has_answer') == resolved) \
                .select(feature) \
                .groupBy(feature).count()
            # .orderBy(feature)

        #     # Retrieve the counts, which is small data
        #     values = [row[0] for row in feature_data.select('feature')]
        #     counts = [row[0] for row in feature_data.select('count')]
        #
        #     # Add zero counts to empty values
        #     histogram = [counts[values.index(i)] if i in values else 0 for i in range(max(values))]
        #
        #     if PLOT_GRAPHS:
        #         # Plot the histogram
        #         label_name = 'Resolved' if resolved else 'Not resolved'
        #         plt.hist(range(len(histogram)), len(histogram), weights=histogram, alpha=0.5, label=label_name)
        #
        # if PLOT_GRAPHS:
        #     plt.savefig('histogram_' + feature + '.png')

    return feature_data


if __name__ == "__main__":
    print("Creating histogram plots")
    spark = SparkSession.builder.getOrCreate()

    features = create_parquet(spark)
    features.write.mode("overwrite").parquet("/user/***REMOVED***/StackOverflow/bucketed_features.parquet")
