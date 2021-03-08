import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, Dense, Activation, Flatten, MaxPooling1D, Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD, Adam
from tensorflow.python.keras import optimizers

BATCH_SIZE = 32
TRAIN_SHAPE = (8,60)

trainFeats = (np.load("NN\\data\\features_left_right.npy"))
trainLabels = (np.load("NN\\data\\labels_left_right.npy"))

trainFeats = tf.keras.utils.normalize(trainFeats, axis = 1)
trainLabels = tf.keras.utils.to_categorical(trainLabels, 3)

model = Sequential()
model.add(Conv1D(64, 2, input_shape = TRAIN_SHAPE))
model.add(Activation("relu"))

model.add(Conv1D(128, 2))
model.add(Activation("sigmoid"))

model.add(Conv1D(128, 2))
model.add(Activation("sigmoid"))

model.add(MaxPooling1D(pool_size=(2)))

model.add(Flatten())

model.add(Dense(512))
model.add(Dense(256))
model.add(Dense(128))

model.add(Dense(3))

model.add(Activation("softmax"))

opt = SGD(lr=0.01)

model.compile(loss="categorical_crossentropy", optimizer=opt, metrics=['accuracy'])

model.fit(trainFeats, trainLabels, epochs=40, validation_split=0.4)

model.save("NN\\left_right_model")
