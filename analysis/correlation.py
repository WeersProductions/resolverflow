from pyspark.sql import SparkSession, Row
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler
from pyspark.sql.functions import mean as _mean, col, stddev, abs, when
from pyspark.sql.types import BooleanType


def filter_outliers(dataframe, exclude_columns):
    """
    For every feature, except those in exclude_columns, set all outliers to NULL.
    """
    for column in dataframe.columns:
        if column in exclude_columns:
            continue
        # Exclude boolean types.
        if dataframe.schema[column].dataType == BooleanType():
            continue
        stats = dataframe \
            .select(_mean(col(column)).alias('mean'), stddev(col(column)).alias('std')) \
            .collect()
        mean = stats[0]['mean']
        std = stats[0]['std']
        print("mean: %s; std: %s" % (str(mean), str(std)))
        count_before = dataframe.filter(col(column).isNull()).count()
        dataframe = dataframe.withColumn(column, when(abs((col(column) - mean) / std) < 2, col(column)).otherwise(None))
        print("Deleted %s entries because of z-score for %s." % (str(dataframe.filter(col(column).isNull()).count() - count_before), column))
    return dataframe


def load_feature_data(spark):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = filter_outliers(feature_data, ["_Id"])
    return feature_data


def calc_correlation_label(spark, feature_columns, label_column):
    result = []
    feature_data = load_feature_data(spark)
    for feature_column in feature_columns:
        columns = [label_column, feature_column]
        df = feature_data.select(columns).dropna()
        sample_count = df.count()
        corr = calc_correlation(columns, df)
        corr_value = corr.toArray()[1][0].item()  # .item() is used to go to a python native type instead of numpy.
        print("Correlation between ", label_column, " and ", feature_column, ": ", corr_value, "; sample count: ",
              sample_count)
        result.append([label_column, feature_column, corr_value])

    rdd = spark.sparkContext.parallelize(result)
    mapping = rdd.map(lambda x: Row(label=x[0], feature=x[1], correlation=x[2]))
    df = spark.createDataFrame(mapping)
    df.show()
    df.write.mode("overwrite").parquet("StackOverflow/pair_correlation.parquet")


def calc_correlation(feature_columns, feature_data):
    """
    Calculates the Spearman Correlation Coefficient
    """
    print("-- Calculating correlation --")
    print("Features: ", feature_columns)
    vector_col = "features"
    assembler = VectorAssembler(inputCols=feature_columns, outputCol=vector_col)
    df_vector = assembler.transform(feature_data).select(vector_col)
    corr_mat = Correlation.corr(df_vector, vector_col, "spearman").head()
    print("-- Done calculating correlation -- ")
    return corr_mat[0]


if __name__ == "__main__":
    """
    Run using:  spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --conf spark.yarn.maxAppAttempts=1 --name dreamteam analysis/correlation.py 2> /dev/null
    """
    print("Starting correlation analysis.")
    spark = SparkSession.builder.getOrCreate()
    calc_correlation_label(spark, ['title_contains_questionmark', '#title_characters', 'creation_seconds', '#tags', 'contains_language_tag', 'contains_platform_tag', 'user_age', '#posts', '#answered_posts', '#characters', '#punctuation_characters', 'punctuation_ratio', '#lines', 'average_line_length', '#words', 'average_word_length', '#codeblocks', '#html_blocks', '#headings', '#referencelist', '#quotes', '#themebreaks', '#codespans', '#references', '#links', '#inline_images', '#mail_addresses', '#emphasis', '#strong'], "has_answer")
