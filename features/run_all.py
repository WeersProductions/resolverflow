from features.number_of_tags import number_of_tags_df

all_features = [number_of_tags_df]

def get_feature_name(feature):
    return feature.__name__

def run_all():
    print("Extracting the following features: ", map(get_feature_name, all_features))
    complete_df = None
    for feature in all_features:
        if complete_df == None:
            complete_df = feature()
        else:
            new_df = feature()
            complete_df.join(new_df, new_df["_Id"] == complete_df["_Id"])

    if complete_df == None:
        print("No features extracted.")
    else:
        complete_df.show()

if __name__ == "__main__":
    run_all()