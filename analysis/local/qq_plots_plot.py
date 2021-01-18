import os
import pickle
import matplotlib.pyplot as plt
from scipy.ndimage import interpolation
from scipy import stats
import math
from tqdm import tqdm
import numpy as np

# Create plots from the pickle file.
# This should run locally on a computer, instead of anything related to the cluster.

output_dir = "plots/"
output_prefix = "qq_plot_"


def get_y_data(scatter_points, column_index):
    y = []
    for point_index in range(len(scatter_points)):
        y_value = scatter_points[point_index][column_index]
        if y_value is None:
            continue
        y.append(y_value)
    return y


def get_y_data_scale(scatter_points, column_index, x_column = 0, x_points = 100):
    """
    Scales y to match x in length.
    """
    # Create data to plot.
    x = []
    y = []
    for point_index in range(len(scatter_points)):
        y_value = scatter_points[point_index][column_index]
        if y_value is None:
            continue
        y.append(y_value)
        x.append(scatter_points[point_index][x_column])
    if len(x) < x_points:
        # Scale to 100 on x-axis using interpolation.
        zoom = x_points / float(len(x))
        y = interpolation.zoom(y, zoom)

    return y


def plot_distribution_and_save(x, distribution, feature_name):
    """
    distribution: log or https://www.johndcook.com/blog/distributions_scipy/
    """
    fig, ax = plt.subplots()
    title = feature_name + " x " + distribution
    if distribution == 'log':
        y_data = []
        for index in range(len(x)):
            y_data.append(math.log(index + 1))
        ax.scatter(x, y_data)
        ax.plot(x, x, ':r')
    else:
        stats.probplot(x, dist=distribution, plot=ax)
    ax.set_title(title)
    ax.set_xlabel(feature_name)
    ax.set_ylabel(distribution)
    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(output_dir + output_prefix + title.replace(" ", "_"))
    plt.close(fig)


def plot_and_save(y, feature_name):
    """
    Plot against an indexed x.
    Example:
        input: y: [0, 2, 5]
        output: plot of x: [0, 1, 2] vs y: [0, 2, 5]
    """
    fig, ax = plt.subplots()
    title = feature_name
    x = []
    for index in range(len(y)):
        x.append(index)
    ax.scatter(x, y)
    ax.set_title(title)
    ax.set_xlabel('index')
    ax.set_ylabel(feature_name)
    os.makedirs(output_dir, exist_ok=True)
    fig.savefig(output_dir + output_prefix + title.replace(" ", "_"))
    plt.close(fig)


def qq_folder(folder, unresolved_suffix='_0', resolved_suffix='_1', file_extension='.pickle', point_count=10000):
    finished_features = set()
    index = 0
    for pickle_file in tqdm(os.listdir(folder)):
        if index <= 1:
            index += 1
            continue
        # Get feature_name by removing '_x.pickle'.
        feature_name = pickle_file[:-(len(unresolved_suffix) + len(file_extension))]
        if feature_name in finished_features:
            continue

        finished_features.add(feature_name)

        # Load both resolved and unresolved.
        base_path = os.path.join(folder, feature_name)
        resolved_pickle = pickle.load(open(base_path + resolved_suffix + file_extension, "rb"), encoding='latin1')
        unresolved_pickle = pickle.load(open(base_path + unresolved_suffix + file_extension, "rb"), encoding='latin1')
        unresolved_points = unresolved_pickle["data_points"]
        resolved_points = resolved_pickle["data_points"]
        # unresolved_points = unresolved_points[unresolved_points[:,0].argsort()]
        # resolved_points = resolved_points[resolved_points[:,0].argsort()]
        unresolved_dict = {a: b for a,b in unresolved_points}
        resolved_dict = {a: b for a,b in resolved_points}

        # Merge the two together and sum their counts. key: feature value; value: occurences
        point_dict = {k: unresolved_dict.get(k, 0) + resolved_dict.get(k, 0) for k in set(unresolved_dict) | set(resolved_dict)}

        # We want approximately 'point_count' points.
        total_counts = sum(point_dict.values())
        divisor = total_counts / point_count

        # Calculate the exact amount of data points we will have in the end.
        data_point_count = 0
        for feature_value in point_dict:
            point_dict[feature_value] = int(point_dict[feature_value] / divisor)
            data_point_count += point_dict[feature_value]

        # Allocate the numpy array that contains all data points.
        x_points = np.zeros(data_point_count, dtype=np.float32)

        # Create the points.
        index = 0
        for feature_value in point_dict:
            for _ in range(point_dict[feature_value]):
                x_points[index] = feature_value
                index += 1

        # We have the feature y value.
        plot_and_save(x_points, feature_name)
        plot_distribution_and_save(x_points, 'log', feature_name)


if __name__ == "__main__":
    """
    Run this file locally.
    """
    qq_folder('analysis/local/data/bucket_pickles/', point_count=100000)
