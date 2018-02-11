import numpy as np

#for i in range(1, 34):
#    data = np.loadtxt(('MoriW3p{}NRes.txt').format(i))
#    np.savetxt('Mori{}.txt'.format(i+26), data)
#    print('Mori{}.txt'.format(i+26), data.shape)

for i in range(43, 57):
    data = np.loadtxt(('Mori{}.txt').format(i))
    np.savetxt('Train{}.txt'.format(i-25), data)
    print('Train{}.txt'.format(i-25), data.shape)