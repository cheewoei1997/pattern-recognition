import numpy as np

matrix = []

for i in range(1, 34):
    data = np.loadtxt(('MoriW3p{}BWR.txt').format(i))
    shape = data.shape
    shape = int(shape[0])
#    print(shape)
    if shape == 14400:
        data = data[:-160]
        np.savetxt('MoriW3p{}NRes.txt'.format(i), data)
        print('MoriW3p{}NRes.txt'.format(i), data.shape)

