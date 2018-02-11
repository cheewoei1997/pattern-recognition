from PIL import Image
import numpy as np

arry = np.zeros(shape=(2, 14400))

for i in range(3, 4):
    img = Image.open(('AlleyW1p{}BWR.png').format(i))
    img = np.array(img)
    X = img[:, :, 0]
    X = np.reshape(X, (-1, 1))
    X = X.T
    np.savetxt(('AlleyW1p{}BWR.txt').format(i), X)
    print(X)
    print(X.shape)

#for j in 
#for i in img
#    Alleytest[i][j] = 

#X = np.reshape(X, (-1, 1))
#X = X.T
#np.savetxt('Alleytest.txt', X)
