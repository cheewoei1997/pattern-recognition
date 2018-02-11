from PIL import Image

basewidth = 160

for i in range(1,34):
    im = 'MoriW3p{}BW.png'
    img = Image.open(im.format(i))
    wpercent = (basewidth/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((basewidth,hsize), Image.ANTIALIAS)
    imgg = 'MoriW3p{}BWR.png'
    img.save(imgg.format(i))