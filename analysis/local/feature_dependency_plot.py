import os
import pickle
import matplotlib.pyplot as plt
from scipy.ndimage import interpolation

# Create plots from the pickle file.
# This should run locally on a computer, instead of anything related to the cluster.

output_dir = "plots/"
output_prefix = "feature_dependency_"

def get_y_data(scatter_points, column_index, x_column = 0, x_points = 100):
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


if __name__ == "__main__":
    print("Creating plots")
    scatter_data = pickle.load(open("/Users/fw/Documents/Projects/resolverflow/analysis/local/data/scatter_points.pickle", "rb"))

    column_names = scatter_data["column_names"]
    scatter_points = scatter_data["scatter_points"]

    for column_index, column in enumerate(column_names):
        if column_index == 0:
            continue

        column_data = get_y_data(scatter_points, column_index)
        for column_index2, column in enumerate(column_names):
            if column_index2 <= column_index:
                continue

            column_data2 = get_y_data(scatter_points, column_index2)

            fig, ax = plt.subplots()
            ax.scatter(column_data, column_data2)
            ax.set_xlabel(column_names[column_index])
            ax.set_ylabel(column_names[column_index2])
            title = column_names[column_index] + " x " + column_names[column_index2]
            ax.set_title(title)
            os.makedirs(output_dir, exist_ok=True)
            fig.savefig(output_dir + output_prefix + title.replace(" ", "_"))
            plt.close(fig)

