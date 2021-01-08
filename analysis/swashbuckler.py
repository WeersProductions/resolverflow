from pyspark.sql import SparkSession
# bucketby


PLOT_GRAPHS = False
DEBUG = False

if PLOT_GRAPHS:
    import matplotlib.pyplot as plt


def mass_apply(dataframe, *functions):
    """
    Takes a dataframe of a single column, and creates a new column for every function given

    Args:
        dataframe: single-column dataframe to be processed
        *functions: all functions that are to be applied

    Returns:
        dataframe with one extra column for every function that was given as input with its results
    """

    result = dataframe

    for func in functions:
        result.flatMap(func)  # no way dat dit werkt, maar ik bedoel het goed

    return result


def bucketize(dataframe, bucket_size=100):
    # Weet niet zeker of deze functie veel toe gaat voegen aangezien het een enkele function call zou moeten zijn

    return dataframe.bucketBy(bucket_size, dataframe.columns[0])


def create_plots(spark):
    """
        Create a histogram for each feature

        Args:
            dataframe: single-column dataframe to be processed
            *functions: all functions that are to be applied

        Returns:
            dataframe with one extra column for every function that was given as input with its results
        """

    integer_features = ["title_number_of_characters", "number_of_characters", "number_of_interpunction_characters",
                       "number_of_lines", "number_of_words", "number_of_tags", "posts_amount", "answered_posts_amount"]
    float_features = ["interpunction_ratio", "average_line_length", "average_word_length", "creation_seconds",
                         "user_age"]
    boolean_features = []

    all_features = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    all_features = all_features.filter(all_features["is_question"])

    for feature in integer_features:
        for resolved in [True, False]:
            feature_data = None
            if resolved:
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
                if resolved:
                    label_name = 'resolved'
                else:
                    label_name = 'not resolved'
                plt.hist(range(len(histogram)), len(histogram), weights=histogram, alpha=0.5, label=label_name)

        if PLOT_GRAPHS:
            plt.savefig('histogram_' + feature + '.png')

        # For testing
        break


if __name__ == "__main__":
    print("Creating histogram plots")
    spark = SparkSession.builder.getOrCreate()
    create_plots(spark)
