from pyspark.sql import SparkSession
from title_features import title_features_df
from post_time import post_time
from tag_info import tag_info_df

all_features = [title_features_df, post_time, tag_info_df]


def get_feature_name(feature):
    return feature.__name__


def run_all(spark):
    print("Extracting the following features: ", map(get_feature_name, all_features))
    complete_df = None
    for feature in all_features:
        new_df = feature(spark)
        if complete_df == None:
            complete_df = new_df
        else:
            complete_df = complete_df.join(new_df, "_Id")

    return complete_df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    complete_df = run_all(spark)
    if complete_df == None:
        print("No features extracted.")
    else:
        complete_df.show()
