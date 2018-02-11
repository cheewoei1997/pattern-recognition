import numpy as np

matrix = []

for i in range(1, 32):
    data = np.loadtxt(('Train{}.txt').format(i))
    matrix.append(data)
    #print(data)
    #print(matrix)

matrix = np.array(matrix)
np.savetxt('TestAll.txt'.format(i), matrix)
print(matrix)
print(matrix.shape)