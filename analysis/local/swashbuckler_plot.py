import os
import pickle

import matplotlib.pyplot as plt
from scipy import stats
from tqdm import tqdm

# Adjust these values to get different output images plotted
ABSOLUTE = True  # Absolute values, some of them plotted on log axes
STACKED = False  # Absolute values, stacked atop each other, all on linear axes
PERCENTAGES = False  # Percentage values, where resolved and unresolved always add up to 100%

# z-score to use as upper limit for outlier removal
Z_SCORE_THRESHOLD = 1.5

if __name__ == "__main__":

    # Path to load pickle files from (which are obtained from running swashbuckler.py and parquet_folder_to_pickle.py
    pickle_path = '/Users/kyle/Projects/PycharmProjects/MBDProject/pickles/'
    for pickle_file in tqdm(os.listdir(pickle_path)):
        # Resolved files only, we will load unresolved a few lines later (manually)
        # TODO: remove comment on next line
        if pickle_file[-8] == '1':  # and pickle_file != 'output_#characters_1.pickle':
            # print('Plotting ' + pickle_file[:-9] + '...')

            resolved_data_points = pickle.load(open(pickle_path + pickle_file, "rb"))
            resolved_counts = resolved_data_points['data_points'].transpose()

            unresolved_data_points = pickle.load(open(pickle_path + pickle_file[:-8] + '0.pickle', "rb"))
            unresolved_counts = unresolved_data_points['data_points'].transpose()
            # counts: [[indices], [values]]

            # Change data format into {index: count} for both resolved and unresolved
            resolved_dict = dict(zip(resolved_counts[0].tolist(), resolved_counts[1].tolist()))
            unresolved_dict = dict(zip(unresolved_counts[0].tolist(), unresolved_counts[1].tolist()))

            # Create a unique list of all data points, to be used as x-ticks
            x_points = \
                filter(lambda e: e is not None, list(set(resolved_counts[0].tolist() + unresolved_counts[0].tolist())))

            # Remove outliers to the right, keep any values down to x = 0
            # All values with a z-score above Z_SCORE_THRESHOLD are filtered out
            z_scores = stats.zscore(x_points)
            x_points = filter(lambda e: e[1] < Z_SCORE_THRESHOLD, zip(x_points, z_scores))
            filtered_z_scores = [x[1] for x in x_points]
            x_points = [x[0] for x in x_points]

            # Build y arrays with 0 as default value, such that they are in the same order (for stacking)
            y_resolved = []
            y_unresolved = []
            for x in x_points:
                y_resolved.append(resolved_dict.get(x, 0))
                y_unresolved.append(unresolved_dict.get(x, 0))

            # Some debug-ish printing, just in case
            if None in unresolved_counts or None in resolved_counts:
                print(x_points)
                print(y_resolved)
                print(y_unresolved)
                print('There is a None count in here somewhere above, ensure everything is in order!\n'
                      '(should be fine if you see a whole bunch of numbers/data points...)')

            if ABSOLUTE:
                # Create two bar plots that are stacked atop each other
                plt.subplot(111)
                resolved_bar = plt.bar([elem - 0.25 for elem in x_points], y_resolved, 0.5, color='lime',
                                       align='center')
                unresolved_bar = plt.bar([elem + 0.25 for elem in x_points], y_unresolved, 0.5, color='fuchsia',
                                         align='center')

                plt.ylabel('#ocurrences')
                plt.title(pickle_file[:-9])
                plt.legend((resolved_bar[0], unresolved_bar[1]), ('resolved', 'unresolved'))

                # The #tags graph looks comically bad with log scales,
                # you might actually want to try it just to see for yourself...
                if not pickle_file == 'output_#tags_1.pickle':
                    plt.yscale('log')

                # Hand-picked some graphs that become absolutely unreadable on a linear scale
                if pickle_file[7:-9] in ['#lines', '#words', 'average_line_length', 'average_word_length',
                                         '#punctuation_characters']:
                    plt.xscale('log')

                plt.savefig('./swashplots/absolutes/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()

            if STACKED:
                unresolved_bar = plt.bar(x_points, y_unresolved, 0.5, color='fuchsia', bottom=y_resolved,
                                         align='center')
                resolved_bar = plt.bar(x_points, y_resolved, 0.5, color='lime', align='center')

                plt.ylabel('#ocurrences')
                plt.title(pickle_file[:-9])
                plt.legend((resolved_bar[0], unresolved_bar[1]), ('resolved', 'unresolved'))

                plt.savefig('./swashplots/stacked/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()

            if PERCENTAGES:
                # Create two stacked bars, this time adding up to a total of 100%
                totals = [resolved_dict.get(i, 0) + unresolved_dict.get(i, 0) for i in x_points]

                resolved_percentages = [float(resolved_dict.get(i, 0)) / j * 100 for i, j in zip(x_points, totals)]
                unresolved_percentages = [float(unresolved_dict.get(i, 0)) / j * 100 for i, j in zip(x_points, totals)]

                # plt.xlim(xmin=0)
                unresolved_bar = plt.bar(x_points, unresolved_percentages, 1, color='fuchsia')
                resolved_bar = plt.bar(x_points, resolved_percentages, 1, color='lime', bottom=unresolved_percentages)

                plt.ylabel('percentage')
                plt.title(pickle_file[7:-9])
                plt.legend((resolved_bar[0], unresolved_bar[0]), ('resolved', 'unresolved'))

                plt.savefig('./swashplots/percentages/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()
