from pyspark.sql import SparkSession
from pyspark.ml.feature import QuantileDiscretizer
from pyspark.sql.functions import mean, col

feature_list = ["title_number_of_characters", "number_of_characters", "number_of_punctuation_characters", "punctuation_ratio", "number_of_lines", "average_line_length", "number_of_words", "average_word_length", "creation_seconds", "number_of_tags", "user_age", "posts_amount", "answered_posts_amount"]


def do_quantile_discretizer(input_data, result_data, column, prefix="buckets_", num_buckets=100):
    discretizer = QuantileDiscretizer(inputCol=column, outputCol=prefix+column, numBuckets=num_buckets)
    fittedBucketer = discretizer.fit(input_data)
    return fittedBucketer.transform(result_data)


def create_scatter_data(spark):
    """
    Example result:
    +---------+--------------------------+--------------------+----------------------------------+--------------------+---------------+-------------------+------------------+-------------------+--------------------+--------------+--------------------+------------------+---------------------+
    |bucket_id|title_number_of_characters|number_of_characters|number_of_punctuation_characters| punctuation_ratio|number_of_lines|average_line_length|   number_of_words|average_word_length|    creation_seconds|number_of_tags|            user_age|      posts_amount|answered_posts_amount|
    +---------+--------------------------+--------------------+----------------------------------+--------------------+---------------+-------------------+------------------+-------------------+--------------------+--------------+--------------------+------------------+---------------------+
    |      8.0|                      29.0|                27.0|                              null|0.015393144123488375|           null|               27.0|              10.0|  4.818926516237462| 1.310644258174288E9|          null|   1845.465446527012|               7.0|                  7.0|
    |     67.0|        130.72050898203594|                null|                              null|                null|           null|               null|              null|  7.003953447563475|1.4848171300671287E9|          null| 6.270216069961038E7|              null|                 null|
    |     70.0|                      null|                null|                              null|                null|           null|               null|              null|  7.205092731578897|1.4931689215688035E9|          null| 6.960859664398558E7|              null|                 null|
    |      0.0|        17.497501517769578|   16.04816853068229|                              null|                null|           null|  16.04775147928994|1.9470618690137198| 3.9966473134191585|1.2406733831840944E9|          null| -257194.00374809327|              null|                 null|
    |     69.0|                      null|                null|                              null|                null|           null|               null|              null|  7.168333686760245| 1.490330667798275E9|          null| 6.710362413774221E7|              null|                 null|
    |      7.0|                      28.0|                26.0|                              null|0.014818346249348111|           null|               26.0|               9.0|  4.762189611083758|1.3063228149140913E9|          null|  1339.7596895664951|               6.0|                  6.0|
    |     88.0|                      null|                null|                              null|                null|           null|               null|              null| 10.893822137819571| 1.564386662575428E9|          null|1.3726113646067417E8|              null|                 null|
    |     49.0|                      70.0|                68.0|                              null| 0.13447332867666137|           null|               68.0|              null|   6.25370848851429|1.4342209895875616E9|          null|3.0083243362954747E7|              null|                 null|
    |     98.0|                      null|                null|                              null|                null|           null|               null|              null|               null|1.6019076826758382E9|          null|2.5467942271986854E8|              null|                 null|
    |     29.0|                      50.0|                48.0|                              null|0.029330829880030603|           null|               48.0|              null|  5.600222949624345|1.3801895861563144E9|          null|   7604745.331296191| 34.48468030986241|   47.944905968095405|
    |     64.0|         97.87874477731354|  105.29671694764862|                              null|                null|           null|  104.9034430427772|              null|  6.815880366330549|  1.47558157493134E9|          null|  5.58595427309031E7|              null|                 null|
    |     75.0|                      null|                null|                              null|                null|           null|               null|              null|  7.584038308333003|1.5092667201273463E9|          null|   8.3250650217123E7|              null|                 null|
    |     47.0|                      68.0|                66.0|                              null| 0.07696478628966687|           null|               66.0|              null|  6.200056985828145|1.4287787418907015E9|          null| 2.728734131906132E7|338.44167047010495|                 null|
    |     42.0|                      63.0|                61.0|                              null| 0.05130004188688255|           null|               61.0|              null|  6.002393682361784|1.4148687181166136E9|          null| 2.074362568229739E7|117.65915454791798|                 null|
    |     44.0|                      65.0|                63.0|                              null| 0.05855529692273072|           null|               63.0|              null|  6.119510164081105|1.4206320222042236E9|          null|2.3248727781680703E7|157.80565421224605|                 null|
    |     35.0|                      56.0|                54.0|                              null| 0.03686504200645072|           null|               54.0|              null|  5.752172894761704|1.3956831331700466E9|          null|1.3022972872835359E7| 55.94470300907792|    120.2903456233859|
    |     62.0|         89.96670030272452|     92.421612569571|                              null|                null|           null|  92.42160484705187|              null|  6.750606021982057|1.4697340256527202E9|          null| 5.188425194938666E7|              null|                 null|
    |     96.0|                      null|                null|                              null|                null|           null|               null|              null|               null| 1.594849027310336E9|          null| 2.122316657777215E8|              null|                 null|
    |     18.0|                      39.0|                37.0|                              null| 0.02083624635651833|           null|               37.0|              null| 5.2559385305721555| 1.348119435017028E9|          null|  1456240.6388011896|              17.0|                 18.0|
    |     80.0|                      null|                null|                              null|                null|           null|               null|              null|  8.020618390554434|1.5293928766601648E9|          null|1.0026530646747383E8|              null|                 null|
    +---------+--------------------------+--------------------+----------------------------------+--------------------+---------------+-------------------+------------------+-------------------+--------------------+--------------+--------------------+------------------+---------------------+
    """

    feature_data = spark.read.parquet("/user/***REMOVED***/StackOverflow/output_stackoverflow.parquet")
    feature_data = feature_data.filter(feature_data["is_question"])
    feature_data = feature_data.select(feature_list + ["has_answer"])
    feature_data_resolved = feature_data.filter(col("has_answer"))
    feature_data_unresolved = feature_data.filter(col("has_answer") == False)

    feature_data_buckets = feature_data
    feature_data_buckets_resolved = feature_data_resolved
    feauture_data_buckets_unresolved = feature_data_unresolved
    # Create buckets for the data, we want 100 points per feature.
    for c in feature_list:
        # discretizer = QuantileDiscretizer(inputCol=c, outputCol="buckets_"+c, numBuckets=100)
        # fittedBucketer = discretizer.fit(feature_data)
        # feature_data_buckets = fittedBucketer.transform(feature_data_buckets)
        feature_data_buckets = do_quantile_discretizer(feature_data, feature_data_buckets, c)
        feature_data_buckets_resolved = do_quantile_discretizer(feature_data_resolved, feature_data_buckets_resolved, c)
        feauture_data_buckets_unresolved = do_quantile_discretizer(feature_data_unresolved, feauture_data_buckets_unresolved, c)

    # Take the average per bucket, this is the value we'll use for the point.
    data_points = None
    for c in feature_list:
        bucket_column = "buckets_" + c
        feature = feature_data_buckets \
            .select([c, bucket_column]) \
            .groupBy(bucket_column) \
            .agg(mean(c).alias(c)) \
            .withColumnRenamed(bucket_column, "bucket_id")
        feature_resolved = feature_data_buckets_resolved \
            .select([c, bucket_column]) \
            .groupBy(bucket_column) \
            .agg(mean(c).alias(c+"resolved")) \
            .withColumnRenamed(bucket_column, "bucket_id") \
            .drop(c)
        feature_unresolved = feauture_data_buckets_unresolved \
            .select([c, bucket_column]) \
            .groupBy(bucket_column) \
            .agg(mean(c).alias(c+"_unresolved")) \
            .withColumnRenamed(bucket_column, "bucket_id") \
            .drop(c)
        feature = feature.join(feature_resolved, "bucket_id").join(feature_unresolved, "bucket_id")
        if data_points == None:
            data_points = feature
        else:
            data_points = data_points.join(feature, "bucket_id", "outer")

    data_points = data_points.sort(col("bucket_id").asc())
    return data_points


if __name__ == "__main__":
    print("Checking feature dependency.")
    spark = SparkSession.builder.getOrCreate()

    scatter_points = create_scatter_data(spark)
    scatter_points.write.mode("overwrite").parquet("StackOverflow/scatter_points.parquet")
