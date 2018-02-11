import numpy as np

matrix = []

for i in range(1, 94):
    data = np.loadtxt(('Test{}.txt').format(i))
    matrix.append(data)
    #print(data)
    #print(matrix)

matrix = np.array(matrix)
np.savetxt('TrainAll.txt'.format(i), matrix)
print(matrix)
print(matrix.shape)