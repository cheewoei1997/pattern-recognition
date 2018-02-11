import numpy as np

#for i in range(1, 34):
#    data = np.loadtxt(('MoriW3p{}NRes.txt').format(i))
#    np.savetxt('Mori{}.txt'.format(i+26), data)
#    print('Mori{}.txt'.format(i+26), data.shape)

for i in range(1, 4):
    data = np.loadtxt(('AlleyW1p{}NRes.txt').format(i))
    np.savetxt('Test{}.txt'.format(i), data)
    print('Test{}.txt'.format(i), data.shape)