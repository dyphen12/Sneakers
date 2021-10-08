"""

Prisma Inc. 2021

training.py

Status: Under Development

Made by Alexis W.

"""

import tensorflow as tf

def training_constructor(training_path):

    TRAINING_DIR = training_path

    training_datagen = tf.keras.preprocessing.image.ImageDataGenerator(rescale = 1./255)

    train_generator = training_datagen.flow_from_directory(
        TRAINING_DIR,
        target_size=(150,150),
        class_mode='categorical'
    )

    return train_generator