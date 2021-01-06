import sys
from user_features import user_age_df, user_question_amount
from pyspark.sql import SparkSession
from title_features import title_features_df
from text_features import text_features_df
from post_time import post_time
from tag_info import tag_info_df
from post_answered import post_answered_df

# Define what features should be extracted and combined here.
# If you add a new feature, be sure to import it correctly and pass it to the spark-submit command.
all_features = [title_features_df, post_answered_df, text_features_df, post_time, tag_info_df, user_age_df, user_question_amount]


def get_feature_name(feature):
    return feature.__name__


def run_all(spark):
    print("Extracting the following features: ", map(get_feature_name, all_features))
    complete_df = None
    for feature in all_features:
        new_df = feature(spark)
        if complete_df is None:
            complete_df = new_df
        else:
            complete_df = complete_df.join(new_df, "_Id")

    return complete_df


if __name__ == "__main__":
    """
    Run this using: spark-submit --master yarn --deploy-mode cluster --conf spark.dynamicAllocation.maxExecutors=10 --name dreamteam --py-files title_features.py,text_features.py,post_time.py,tag_info.py,user_features.py,post_answered.py run_all.py --file "StackOverflow/output_stackoverflow.parquet" 2> /dev/null

    --py-files, a list of python files that are imported from this file.

    Arguments (optional): --file [filename], this is where the output will be saved if provided.
    If no arguments are given, output is printed.
    """

    spark = SparkSession.builder.getOrCreate()

    complete_df = run_all(spark)
    if complete_df is None:
        print("No features extracted.")
    elif len(sys.argv) > 2 and sys.argv[1]=='--file':
        complete_df.write.parquet(sys.argv[2])
    else:
        complete_df.show()
