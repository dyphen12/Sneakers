"""

Prisma Inc. 2021

model.py

Status: Under Development

Made by Alexis W.

"""

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.layers import Flatten
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Dense



def load_model(labels):

    model = Sequential([
        Conv2D(64, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D(2, 2),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D(2, 2),
        Flatten(),
        Dropout(0.5),
        Dense(512, activation='relu'),
        Dense(labels, activation='softmax')
    ])

    return model

def compile_model(model, train_generator, model_name):

    model.compile(loss = 'categorical_crossentropy',
                  optimizer= 'rmsprop',
                  metrics=['accuracy'])

    history = model.fit_generator(train_generator, epochs=25, validation_data = train_generator, verbose=1)


    model.save('sneakers/models/{}.h5'.format(model_name))

    print('Model Trained and saved!')

    return history
