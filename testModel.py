import tensorflow as tf
import numpy as np
from pylsl import StreamInlet, resolve_stream, local_clock
import time
from collections import deque

model = tf.keras.models.load_model("NN\\left_right_model")

ts = 0
tsO = 0
print ("loooking for an EEG stream...")
streams = resolve_stream('type','EEG')
inlet = StreamInlet(streams[0])

for i in range(200):
    channel_data = {}
    data = np.zeros((1,8,60))
    for j in range(8):
        sample, timestamp = inlet.pull_sample()
        ts = timestamp
        if i == 0:
            ts0 = timestamp
        if j not in channel_data:
            channel_data[j] = sample
        else:
            channel_data[j].append(sample)
        data[0][j] = channel_data[j][:60]
    inlet.flush()
    data = np.array(data).reshape(1,8,60)
    data = tf.keras.utils.normalize(data, axis=1)
    pred = model.predict([data])
    
    #BLINK DETECTION CODE
    # if (pred[0][0] > 0.95):
    #     print(format("Blink - Timestamp: %d" % (ts-ts0)))
    # else :
    #     print(format("Nothn - Timestamp: %d" % (ts-ts0)))

    #JAW DETECTION CODE
    # if (int)(pred[0][0]*500) != 0:
    #     print(format("Jaw Clenched - Prediction: %f, Timestamp: %d" % (pred[0][0], ts-ts0)))
    # else: 
    #     print(format("Jaw Not Clenched - Prediction: %f, Timestamp: %d" % (pred[0][0], ts-ts0)))
    # print(format("Timestamp: %d" % (ts-ts0)))
    
    #LEFT/RIGHT DETECTION CODE
    print("\r", format("Prediction: Left: %f, None: %f, Right: %f -- Timestamp: %d" % (pred[0][0]*100.0, pred[0][1]*100.0, pred[0][2]*100.0, ts-ts0)), end="")