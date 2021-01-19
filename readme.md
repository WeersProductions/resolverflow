# Resolverflow
Stackoverflow, a programmer's best friend. Well, *if* you get an answer, and *if* it is a useful one.

We will perform a data analysis on the StackOverflow dataset to find out how you can best formulate your question. We aim to find features that will help you get a resolution as quick as possible. Features will be ordinal and categorical, taken from the literal dataset values and but also from some custom NLP. Let's make some Stackoverflow clickbait 😎

## Dataset
The https://archive.org/download/stackexchange dataset is uploaded to an HDFS. `convert_dataset.py` converts the xml dataset into a .parquet file that is already partitioned. This way, loading is a lot faster.
Parquet structures of all generates file can be found at https://github.com/WeersProductions/resolverflow/blob/master/dataFramePreviews.md .

## Project overview
The project is divided into three folders:
- features
- analysis
- analysis/local
- util

### Features
Responsible for collecting features from the big data set of StackOverflow. Uses spark to fetch the features. Each file contains a group of features and can be spark-submitted on its own to gather these features.
However, to run all features at once and combine them into one resulting dataset, `run_all.py` can be used. Users can define what feature groups should be extracted and it will combine those automatically.

To add a feature, create a new file and add your function definition. It should receive a `spark` context that can be used to interact with the Spark cluster. This method should return a dataframe at least one column: `_Id`. `_Id` is the Id of the post. Note: if you are using PostHistory.parquet as a source for data, be sure to use `_PostId` and rename the column to `_Id`.

### Analysis
Responsible for analyzing the features after feature collection has been done. This reads from a `output_stackoverflow.parquet` file which contain the extracted features.
- correlation.py <br>
Calculates the correlation between a feature and the label.
- decision_tree.py <br>
Contains code to train and evaluate a decision tree (whether as classifier or regressor). Features that should be used can be selected.
- swashbuckler.py <br>
Bucketizes the input to be used for graphs.
- vif.py <br>
Used to remove features that have a too high VIF. Calculates the vif of pairs of features and also calculates the VIF while removing a single feature from all features.

### Analaysis/local
To be run on a local machine. This uses .pickle files (small data) and can generate plots.
- qq_plots_plot.py
Generates qq plots for features. Different distributions can be plotted against a feature.
- swashbuckler_plot.py
Generates histograms of a feature for both resolved and unresolved questions.
