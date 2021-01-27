from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean as _mean, stddev, abs, when
from pyspark.sql.types import IntegerType

INTEGER_FEATURES = ['#title_characters', '#characters', '#punctuation_characters', '#lines', '#words', '#tags',
                    '#posts', '#answered_posts', '#codeblocks', '#html_blocks', '#headings', '#referencelist',
                    '#quotes', '#themebreaks', '#codespans', '#references', '#links', '#inline_images',
                    '#mail_addresses', '#emphasis', '#strong']
FLOAT_FEATURES = ['punctuation_ratio', 'average_line_length', 'average_word_length', 'user_age', 'creation_seconds']
BOOLEAN_FEATURES = ['title_contains_questionmark', 'contains_language_tag', 'contains_platform_tag']


def create_parquet_files(spark_session):
    """
    Create a histogram for each feature

    Args:
        spark_session: dataframe to be processed

    Returns:
        dataframe
    """
    all_features = spark_session.read.parquet('/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet')
    all_features = all_features.filter(all_features['is_question'])

    all_results = []

    for feature in INTEGER_FEATURES + FLOAT_FEATURES + BOOLEAN_FEATURES:

        # Replace all outliers with z-score above 2 with -1, unless they're boolean
        if feature not in BOOLEAN_FEATURES:
            stats = all_features \
                .select(_mean(col(feature)).alias('mean'), stddev(col(feature)).alias('std')) \
                .collect()
            mean = stats[0]['mean']
            std = stats[0]['std']

            all_features = all_features.withColumn(feature,
                                                   when(abs((col(feature) - mean) / std) < 2,
                                                        col(feature)).otherwise(-1))

        original_feature = feature
        if feature in FLOAT_FEATURES:
            # Bucketize each float feature into '${feature}_bucket_index' columns
            feature += '_bucket_index'
            column_max = all_features.agg({original_feature: 'max'}).collect()[0][0]
            all_features = all_features.withColumn(feature,
                                                   ((col(original_feature) / column_max) * 1000).cast(IntegerType()))

        for resolved in [True, False]:
            new_file = all_features.filter(col('has_answer') == resolved) \
                .select(feature) \
                .groupBy(feature).count()

            filename = original_feature + '_1' if resolved else original_feature + '_0'
            new_file.write.mode('overwrite') \
                .parquet('/user/***REMOVED***/StackOverflow/swashbuckler/output_' + filename + '.parquet')

    return all_results


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()
    create_parquet_files(spark)
