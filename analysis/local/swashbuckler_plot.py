import os
import pickle
from itertools import izip

import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Creating plots")

    pickle_path = '/Users/kyle/Projects/PycharmProjects/MBDProject/pickles/'
    for pickle_file in os.listdir(pickle_path):
        if pickle_file[-8] == '1':  # Resolved
            resolved_data_points = pickle.load(open(pickle_path + pickle_file, "rb"))
            # all_column_names = resolved_data_points['column_names']
            resolved_counts = resolved_data_points['data_points'].transpose()

            unresolved_data_points = pickle.load(open(pickle_path + pickle_file[:-8] + '0.pickle', "rb"))
            unresolved_counts = unresolved_data_points['data_points'].transpose()
            # counts: [[indices], [values]]

            # Change data format into {index: count} for both resolved and unresolved
            resolved_dict = dict(izip(resolved_counts[0].tolist(), resolved_counts[1].tolist()))
            unresolved_dict = dict(izip(unresolved_counts[0].tolist(), unresolved_counts[1].tolist()))

            # Create a unique list of all data points, to be used as x-ticks
            x_points = list(set(resolved_counts[0].tolist() + unresolved_counts[0].tolist()))

            # Build y arrays with 0 as default value, such that they are in the same order (for stacking)
            y_resolved = []
            y_unresolved = []
            for x in x_points:
                y_resolved.append(resolved_dict.get(x, 0))
                y_unresolved.append(unresolved_dict.get(x, 0))

            # Create two bar plots that are stacked atop each other
            resolved_bar = plt.bar(x_points, y_resolved, 0.2, color='g')
            unresolved_bar = plt.bar(x_points, y_unresolved, 0.2, bottom=y_resolved,  color='r')

            # plt.yscale('log')
            plt.xlim(xmax=max(resolved_counts[0].tolist() + unresolved_counts[0].tolist()))
            plt.ylim(ymax=max(resolved_counts[1].tolist() + unresolved_counts[1].tolist()))

            plt.ylabel('#ocurrences')
            plt.title(pickle_file[:-9])
            plt.legend((resolved_bar[0], unresolved_bar[1]), ('resolved', 'unresolved'))

            plt.savefig('histogram_' + pickle_file[:-9] + '.svg')
            # plt.show()

    print("Done!")
