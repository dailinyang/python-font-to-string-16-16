import string

from PIL import Image, ImageFont


point_size = 16
font = ImageFont.truetype("mingliu.ttc", point_size)


for char in '大':
    im = Image.Image()._new(font.getmask(char,mode='1'))
    a= im.resize((16,16))
    for x in range(0,16):
        for y in range(0,16):
            print(str(a.getpixel((y,x)))+",",end="")
        print()
	#print("\n")
    #im.save(char + ".bmp")
