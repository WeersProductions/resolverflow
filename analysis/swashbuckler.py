from pyspark.sql import SparkSession
from pyspark.sql.functions import col, mean as _mean, stddev, abs, when, round

INTEGER_FEATURES = ['#title_characters', '#characters', '#punctuation_characters', '#lines', '#words', '#tags',
                    '#posts', '#answered_posts', '#codeblocks', '#html_blocks', '#headings', '#referencelist',
                    '#quotes', '#themebreaks', '#codespans', '#references', '#links', '#inline_images',
                    '#mail_addresses', '#emphasis', '#strong', '#codelines']
FLOAT_FEATURES = ['punctuation_ratio', 'average_line_length', 'average_word_length',  # 'user_age', 'creation_seconds',
                  'codeline_ratio', 'codeblock_ratio', 'heading_ratio', 'themebreak_ratio', 'codespan_ratio',
                  'emphasis_ratio', 'strong_ratio']
BOOLEAN_FEATURES = ['title_contains_questionmark', 'contains_language_tag', 'contains_platform_tag']


def create_parquet_files(spark_session):
    """
    Create a histogram for each feature

    Args:
        spark_session: dataframe to be processed

    Returns:
        dataframe
    """
    all_features = spark_session.read.parquet('/user/s*******/StackOverflow/output_stackoverflow.parquet')
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
                                                   when(abs((col(feature) - mean) / std) < 3,
                                                        col(feature)).otherwise(-1))

        if feature in FLOAT_FEATURES:
            # Bucketize each float feature into rounded number buckets
            all_features = all_features.withColumn(feature, round(col(feature), 2))

        for resolved in [True, False]:
            new_file = all_features.filter(col('has_answer') == resolved) \
                .select(feature) \
                .groupBy(feature).count()

            filename = feature + '_1' if resolved else feature + '_0'
            new_file.write.mode('overwrite') \
                .parquet('/user/s*******/StackOverflow/swashbuckler/output_' + filename + '.parquet')

    return all_results


if __name__ == '__main__':
    spark = SparkSession.builder.getOrCreate()
    create_parquet_files(spark)
