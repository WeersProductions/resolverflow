import os
import pickle

import matplotlib.pyplot as plt
from tqdm import tqdm

# Adjust these values to get different output images plotted
ABSOLUTE = False  # Absolute values, some of them plotted on log axes
STACKED = True  # Absolute values, stacked atop each other, all on linear axes
PERCENTAGES = False  # Percentage values, where resolved and unresolved always add up to 100%

if __name__ == "__main__":

    # Path to load pickle files from (which are obtained from running swashbuckler.py and parquet_folder_to_pickle.py
    pickle_path = '/Users/kyle/Projects/PycharmProjects/MBDProject/pickles/'
    for pickle_file in tqdm(os.listdir(pickle_path)):
        # Resolved files only, we will load unresolved a few lines later (manually)
        if pickle_file[-8] == '1':
            # print('Plotting ' + pickle_file[:-9] + '...')

            resolved_data_points = pickle.load(open(pickle_path + pickle_file, "rb"))
            resolved_counts = resolved_data_points['data_points']

            # counts: [(index), (value)]
            unresolved_data_points = pickle.load(open(pickle_path + pickle_file[:-8] + '0.pickle', "rb"))
            unresolved_counts = unresolved_data_points['data_points']

            # Change data format into {index: count} for both resolved and unresolved
            resolved_dict = {a: b for a, b in resolved_counts}
            unresolved_dict = {a: b for a, b in unresolved_counts}

            # Create a unique list of all data points, to be used as x-ticks
            x_points = sorted(
                filter(lambda e: e is not None and e >= 0, list(set(resolved_dict.keys() + unresolved_dict.keys()))))

            # Build y arrays with 0 as default value, such that they are in the same order (for stacking)
            y_resolved = []
            y_unresolved = []
            for x in x_points:
                y_resolved.append(resolved_dict.get(x, 0))
                y_unresolved.append(unresolved_dict.get(x, 0))

            # Some debug-ish printing, just in case
            if None in unresolved_counts or None in resolved_counts:
                print('\n' + str(x_points))
                print(y_resolved)
                print(y_unresolved)
                print('There is a None count in here somewhere above, ensure everything is in order!\n'
                      '(should be fine if you see a whole bunch of numbers/data points...)')

            if ABSOLUTE:
                # Create two bar plots that are stacked atop each other
                plt.subplot(111)
                resolved_graph = plt.plot(x_points, y_resolved, color='green')
                unresolved_graph = plt.plot(x_points, y_unresolved, color='orangered')

                plt.ylabel('#ocurrences')
                plt.xlabel(pickle_file[7:-9].replace('_', ' '))
                plt.legend((resolved_graph[0], unresolved_graph[0]), ('resolved', 'unresolved'))

                # The #tags graph looks comically bad with log scales,
                # you might actually want to try it just to see for yourself...
                if pickle_file not in ['output_#tags_1.pickle', 'output_average_word_length_1.pickle']:
                    plt.yscale('log')

                # Hand-picked some graphs that become absolutely unreadable on a linear scale
                # if pickle_file[7:-9] in ['average_line_length']:  # , 'average_word_length']:
                #     plt.xscale('log')

                if pickle_file in ['output_contains_language_tag_1.pickle', 'output_contains_platform_tag_1.pickle',
                                   'output_title_contains_question_mark_1.pickle']:
                    plt.xticks([0, 1], ['False', 'True'])

                plt.savefig('./swashplots/absolutes/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()

            if STACKED:
                unresolved_bar = plt.bar(x_points, y_unresolved, color='orangered', bottom=y_resolved,
                                         align='center')
                resolved_bar = plt.bar(x_points, y_resolved, color='green', align='center')

                plt.ylabel('#ocurrences')
                plt.xlabel(pickle_file[7:-9].replace('_', ' '))
                plt.legend((resolved_bar[0], unresolved_bar[0]), ('resolved', 'unresolved'))

                if pickle_file in ['output_contains_language_tag_1.pickle', 'output_contains_platform_tag_1.pickle',
                                   'output_title_contains_question_mark_1.pickle']:
                    plt.xticks([0, 1], ['False', 'True'])

                plt.savefig('./swashplots/stacked/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()

            if PERCENTAGES:
                # Create two stacked bars, this time adding up to a total of 100%
                totals = [resolved_dict.get(i, 0) + unresolved_dict.get(i, 0) for i in x_points]

                resolved_percentages = [float(resolved_dict.get(i, 0)) / j * 100 for i, j in zip(x_points, totals)]
                unresolved_percentages = [float(unresolved_dict.get(i, 0)) / j * 100 for i, j in zip(x_points, totals)]

                unresolved_bar = plt.bar(x_points, unresolved_percentages, color='orangered')
                resolved_bar = plt.bar(x_points, resolved_percentages, color='green', bottom=unresolved_percentages)

                plt.ylabel('percentage')
                plt.xlabel(pickle_file[7:-9].replace('_', ' '))
                plt.legend((resolved_bar[0], unresolved_bar[0]), ('resolved', 'unresolved'))

                if pickle_file in ['output_contains_language_tag_1.pickle', 'output_contains_platform_tag_1.pickle',
                                   'output_title_contains_question_mark_1.pickle']:
                    plt.xticks([0, 1], ['False', 'True'])

                plt.savefig('./swashplots/percentages/' + pickle_file[7:-9] + '.png', dpi=300)
                # plt.show()

                plt.cla()
                plt.clf()
