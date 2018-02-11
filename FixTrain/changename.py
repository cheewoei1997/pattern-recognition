import numpy as np

#for i in range(1, 34):
#    data = np.loadtxt(('MoriW3p{}NRes.txt').format(i))
#    np.savetxt('Mori{}.txt'.format(i+26), data)
#    print('Mori{}.txt'.format(i+26), data.shape)

for i in range(1, 34):
    data = np.loadtxt(('MoriW3p{}NRes.txt').format(i))
    np.savetxt('Test{}.txt'.format(i+77), data)
    print('Test{}.txt'.format(i+77), data.shape)