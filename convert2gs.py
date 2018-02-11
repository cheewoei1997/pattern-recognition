from PIL import Image, ImageEnhance, ImageFilter
import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import imsave

# basewidth = 800

# for i in range(1,11):
#     im = 'AlleyW3p{}.jpeg'
#     img = Image.open(im.format(i))
#     wpercent = (basewidth/float(img.size[0]))
#     hsize = int((float(img.size[1])*float(wpercent)))
#     img = img.resize((basewidth,hsize), Image.ANTIALIAS)
#     imgg = 'AlleyW3p{}Resz.jpg'
#     img.save(imgg.format(i))

#im = 'Alleytest.jpg'
#img = np.array(Image.open(im))
#print(img)
#plt.scatter()
#plt.show()

#im = "Alleytest.jpg"
#print(scipy.misc.imread(im))

#JPG file
#image_file = Image.open("Alleytest.jpg") # open colour image
#image_file = image_file.convert('1') # convert image to black and white
#image_file.save('result.jpg')

#PNG file
for i in range(1,34):
    im = 'MoriW3p{}Resz.jpg'
    img = Image.open(im.format(i)).convert('LA')   
    imgg = 'MoriW3p{}BW.png'
    img.save(imgg.format(i))