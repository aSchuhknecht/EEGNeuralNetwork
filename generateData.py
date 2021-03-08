from pylsl import StreamInlet, resolve_stream
import numpy as np
import os
import time
import matplotlib.pyplot as plt
from matplotlib import style
from collections import deque

DATA_DIR = "none"
DATA_RANGE = 2000

DATA_START_RANGE = 4000

last_print = time.time()
fps_counter = deque(maxlen = 150)

print ("loooking for an EEG stream...")
streams = resolve_stream('type','EEG')
inlet = StreamInlet(streams[0])

for k in range(DATA_RANGE):
    channel_data = {}
    data = np.zeros((8,60))
    for i in range(8):
        sample, timestamp = inlet.pull_sample()
        if i not in channel_data:
            channel_data[i] = sample
        else:
            channel_data[i].append(sample)
        data[i] = channel_data[i][:60]
    print("\r", format("%f Percent Done        " % ((k+1)/(float)(DATA_RANGE)*100.0)), end="")
    np.save(format("NN\\data\\%s\\%s_train%d" % (DATA_DIR, DATA_DIR, k+DATA_START_RANGE)),data)

print("\nDONE COLLECTING DATA")
