"""

Prisma Inc. 2021

computation.py

Status: Under Development

Made by Alexis W.

"""

import tensorflow as tf

def do_magic(model_name, images):
    new_model = tf.keras.models.load_model('sneakers/models/{}.h5'.format(model_name))

    # Show the model architecture
    new_model.summary()

    classes = new_model.predict(images, batch_size=10)

    # print(classes)

    return classes
