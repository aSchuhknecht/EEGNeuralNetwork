import numpy as np
import random

DATA_RANGE = 6000
CAT = ["left", "none", "right"]
trainData = []

for cats in CAT:
    dex = CAT.index(cats)
    for datCount in range(DATA_RANGE):
        dat = (np.load(format("NN\\data\\%s\\%s_train%d.npy" % (CAT[dex], CAT[dex], datCount))))
        trainData.append([dat, dex])

random.shuffle(trainData)

feats = []
labels = []

for feature,label in trainData:
    feats.append(feature)
    labels.append(label)

print(labels[:10])

feats = np.array(feats).reshape(DATA_RANGE*len(CAT), 8 ,60)

np.save("NN\\data\\features_left_right.npy",feats)
np.save("NN\\data\\labels_left_right.npy",labels)
