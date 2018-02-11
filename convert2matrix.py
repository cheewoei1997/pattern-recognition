import numpy as np

matrix = []

for i in range(43, 57):
    data = np.loadtxt(('Mori{}.txt').format(i))
    matrix.append(data)
    #print(data)
    #print(matrix)

matrix = np.array(matrix)
np.savetxt('MoriTest.txt'.format(i), matrix)
print(matrix)
print(matrix.shape)