"""

Prisma Inc. 2021

dataset.py

Status: Under Development

Made by Alexis W.

"""

import matplotlib.pyplot as plt


def render_training_history(training_history):
    loss = training_history.history['loss']
    val_loss = training_history.history['val_loss']

    accuracy = training_history.history['accuracy']
    val_accuracy = training_history.history['val_accuracy']

    plt.figure(figsize=(14, 4))

    plt.subplot(1, 2, 1)
    plt.title('Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.plot(loss, label='Training set')
    plt.plot(val_loss, label='Test set', linestyle='--')
    plt.legend()
    plt.grid(linestyle='--', linewidth=1, alpha=0.5)

    plt.subplot(1, 2, 2)
    plt.title('Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.plot(accuracy, label='Training set')
    plt.plot(val_accuracy, label='Test set', linestyle='--')
    plt.legend()
    plt.grid(linestyle='--', linewidth=1, alpha=0.5)

    plt.show()

def prediction_labeling(labels, pred):

    pred = pred.tolist()

    for i in range(0,len(pred)):
        print(pred[i])
        number_list = pred[i]
        max_value = max(number_list)
        max_index = number_list.index(max_value)

        print(max_index)

        for key in labels:
            if labels[key] == max_index:
                print(key)

    return ':p'