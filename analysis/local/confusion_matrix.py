from sklearn.metrics import confusion_matrix
import pickle
import matplotlib.pyplot as plt
import numpy as np
import itertools


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="black" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')


def calculate_confusion_matrix(predictions, columns, labels):
    print(columns)
    predictions = predictions.transpose()
    count = len(predictions[0])
    for value in range(count):
        for i in range(2):
            if predictions[i][value] == str(0):
                predictions[i][value] = "unresolved"
            else:
                predictions[i][value] = "resolved"
    print(predictions[0][400], type(predictions[0][400]))
    print(predictions[1][400], type(predictions[1][400]))
    return confusion_matrix(predictions[0], predictions[1], labels=labels)


if __name__ == "__main__":
    predictions = pickle.load(open("analysis/local/data/classifier_prediction_results.pickle", "rb"))
    labels = ["resolved", "unresolved"]
    cm = calculate_confusion_matrix(predictions["data_points"], predictions["column_names"], labels)
    print(cm)
    plt.figure()
    plot_confusion_matrix(cm, classes=labels, normalize=True)
    plt.show()
