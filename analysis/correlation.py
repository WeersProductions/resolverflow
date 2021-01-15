from pyspark.sql import SparkSession, Row
from pyspark.ml.stat import Correlation
from pyspark.ml.feature import VectorAssembler


def load_feature_data(spark):
    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = feature_data.drop("_Text")
    return feature_data


def calc_correlation_label(spark, feature_columns, label_column):
  result = []
  for feature_column in feature_columns:
    corr = calc_correlation(spark, [label_column, feature_column])
    corr_value = corr.toArray()[1][0].item() # .item() is used to go to a python native type instead of numpy.
    print("Correlation between ", label_column, " and ", feature_column, ": ", corr_value)
    result.append([label_column, feature_column, corr_value])

  rdd = spark.sparkContext.parallelize(result)
  mapping = rdd.map(lambda x: Row(label=x[0], feature=x[1], correlation=x[2]))
  df = spark.createDataFrame(mapping)
  df.show()
  df.write.mode("overwrite").parquet("StackOverflow/pair_correlation.parquet")


def calc_correlation(spark, feature_columns):
    """
    Calculates the Spearman Correlation Coefficient
    """
    feature_data = load_feature_data(spark)
    print("-- Calculating correlation --")
    print("Features: ", feature_columns)
    vector_col = "features"
    assembler = VectorAssembler(inputCols=feature_columns, outputCol=vector_col)
    df_vector = assembler.transform(feature_data).select(vector_col)
    corr_mat = Correlation.corr(df_vector, vector_col, "spearman").head()
    print("-- Done calculating correlation -- ")
    return corr_mat[0]


if __name__ == "__main__":
    print("Starting correlation analysis.")
    spark = SparkSession.builder.getOrCreate()
    calc_correlation_label(spark, ["title_contains_questionmark", "#title_characters", "#characters", "#punctuation_characters", "punctuation_ratio", "#lines", "average_line_length", "#words", "average_word_length", "creation_seconds", "#tags", "contains_language_tag", "contains_platform_tag", "user_age", "posts_amount", "answered_posts_amount"], "has_answer")