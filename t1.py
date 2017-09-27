import string

from PIL import Image, ImageFont

WHITE = 255
BLACK = 0
point_size = 16
font = ImageFont.truetype("msjhl.ttc", point_size)
#font = ImageFont.truetype("arial.ttf", point_size)
outary = []

print("[")
for char in 'Taiwanbit伸峰':
    im = Image.Image()._new(font.getmask(char,mode='1'))
    a= im.resize((16,16))
    for x in range(0,16):
        for y in range(0,16):
            pass
            #print(str(a.getpixel((y,x)))+",",end="")
        #print()
	#print("\n")
    #im.save(char + ".bmp")
    a.save(char + ".bmp")
    

    x = 0
    y = 0
    outary.clear()
    for y in range(16):
        x=0
        turn = WHITE
        count = 0
        while x<16:    
            #print(str(x))
            if a.getpixel((15-x,y)) == turn:
                count+=1
                x+=1
            else:
                outary.append(count)
                if turn == WHITE:
                    turn = BLACK
                else:
                    turn = WHITE
                count=1
                x+=1
        else:
            outary.append(count)
                
    print("'",end="")        
    print( "".join(str(i)+"," for i in outary)[:-1],end=""  )
    
    print("',\\")
print("]")
