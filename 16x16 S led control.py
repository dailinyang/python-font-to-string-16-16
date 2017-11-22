from microbit import *
import neopixel
led1 = neopixel.NeoPixel(pin2,256)
rle1 = "0,5,1,5,1"
rle1 = "0,5,1,6,1,3,0,2,5,5,1,3,0,2,1,4,2,1,1,1,2,2,0,3,1,2,1,3,1,1,2,2,0,3,1,2,1,3,1,1,2,2,0,4,2,4,1,1,2,2,0,2,2,2,2,2,1,1,2,2,0,5,1,4,1,1,2,2,0,1,8,1,1,1,2,2,0,5,1,4,1,1,2,2,0,2,6,2,1,1,2,2,0,5,1,4,1,1,2,2,0,5,1,4,1,1,2,2,0,1,8,1,4,2,0,5,1,4,1,5,0,5,1,10"
oneLineAry = [0 for i in range(256)]
red=(255,0,0)
black=(0,0,0)
ledAry=[]
pos = 0
def getSPos(pos):
    if (pos//16) % 2 == 0:
        return pos
    else:
        return (16 * (pos // 16)) + (15 - (pos%16))
def shiftBy1():
    for i in range(16):
        startx = i*16
        endx = i*16 + 15
        for j in range(15):
            oneLineAry[startx + j] = oneLineAry[startx + j +1]
        oneLineAry[endx] = 0
def shiftByNeg1():
    for i in range(16):
        startx = i*16
        endx = i*16 + 15
        for j in range(15):
            oneLineAry[endx - j] = oneLineAry[endx - j - 1]
        oneLineAry[startx] = 0
def tar2oneLineAry():
    pos = 0
    for i in range(0,len(ary1)):
        nums = int(ary1[i])
        while nums:
            if i % 2 ==0:
                oneLineAry[pos]=1
            else:
                oneLineAry[pos]=0
            pos+=1
            nums-=1
def tar2oneLineAryDyn():
    pos = 0
    nowIndex = 0
    nextIndex = 0
    global rle1,oneLineAry
    rle1 = "," + rle1
    i=0
    while nextIndex < len(rle1):
        nextIndex = rle1.find(',',nowIndex+1)
        if nextIndex == -1:
            newStr = rle1[nowIndex+1:]
            #print(newStr)
            break
        else:
            #print("now=" + str(nowIndex) + "next = " + str(nextIndex) )
            newStr = rle1[nowIndex+1:nextIndex]
            #print(newStr)
        #print(newStr)
        
        nowIndex = nextIndex
        nums = int(newStr)
        while nums:
            if i % 2 ==0:
                oneLineAry[pos]=1
            else:
                oneLineAry[pos]=0
            pos+=1
            nums-=1
        i+=1
def draw2led():
    for i in range(0,256):
        if oneLineAry[i] == 1:
            led1[getSPos(i)] = red
        else:
            led1[getSPos(i)] = black
'''
ary1= rle1.split(",")
tar2oneLineAry()
draw2led()
led1.show()
for i in range(16):
    shiftByNeg1()
    draw2led()
    led1.show()
'''