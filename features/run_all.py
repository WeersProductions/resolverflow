from pyspark.sql import SparkSession
from title_features import title_features_df
from number_of_tags import number_of_tags_df
from text import text_length_and_formatting

all_features = [title_features_df, text_length_and_formatting]


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
            complete_df.join(new_df, new_df["_Id"] == complete_df["_Id"])

    return complete_df


if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()

    complete_df = run_all(spark)
    if complete_df == None:
        print("No features extracted.")
    else:
        complete_df.show()
