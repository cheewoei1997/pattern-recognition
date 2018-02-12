import numpy as np

labels =   [0,1,2,1,0,2,1,1,2,1,0,2,0,2,1,1,1,0,1,0,0,0,0,1,
            2,0,0,0,1,1,1,1,0,0,0,1,1,1,2,2,2,2,2,2,2,2,1,1,1,1,1,
            0,0,1,2,2,2,2,2,2,2,2,2,1,1,0,0,0,0,0,0,0,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1]

labels = np.array(labels)
np.savetxt('TrainLabels.txt', labels)


# data = np.loadtxt('TrainAll.txt')

print(labels)
print(labels.shape)
# print(data)
# print(data.shape)