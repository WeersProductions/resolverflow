from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max

PLOT_GRAPHS = False
DEBUG = False

if PLOT_GRAPHS:
    import matplotlib.pyplot as plt

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


def bucketize(dataframe, bucket_size=100):
    # Weet niet zeker of deze functie veel toe gaat voegen aangezien het een enkele function call zou moeten zijn

    return dataframe.bucketBy(bucket_size, dataframe.columns[0])


def create_plots(spark_session):
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
        original_feature = feature
        if feature in FLOAT_FEATURES:
            # Bucketize each float feature into "${feature}_bucket_index" columns
            feature += '_bucket_index'
            all_features.withColumn(feature, int(col(original_feature) / max(col(original_feature))))

        for resolved in [True, False]:
            feature_data = all_features.filter(all_features["has_answer"] is resolved) \
                .select(feature) \
                .groupBy(feature).count() \
                .orderBy(feature)

            # Retrieve the counts, which is small data
            values = [row[0] for row in feature_data.select('feature')]
            counts = [row[0] for row in feature_data.select('count')]

            # Add zero counts to empty values
            histogram = [counts[values.index(i)] if i in values else 0 for i in range(max(values))]

            if DEBUG:
                # For testing
                print(histogram)

            if PLOT_GRAPHS:
                # Plot the histogram
                label_name = 'Resolved' if resolved else 'Not resolved'
                plt.hist(range(len(histogram)), len(histogram), weights=histogram, alpha=0.5, label=label_name)

        if PLOT_GRAPHS:
            plt.savefig('histogram_' + original_feature + '.png')


if __name__ == "__main__":
    print("Creating histogram plots")
    spark = SparkSession.builder.getOrCreate()
    create_plots(spark)
