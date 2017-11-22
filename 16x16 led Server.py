from microbit import *
import neopixel
import radio
from random import randint
radio.on()
led1=neopixel.NeoPixel(pin2,256)
Taiwanbit=['0,6,1,9,0,2,7,3,1,3,0,2,1,2,1,2,2,2,1,3,0,2,2,1,1,1,2,1,1,2,1,2,0,2,2,1,1,1,2,1,1,2,1,2,0,2,1,1,3,1,1,1,1,2,1,2,0,2,1,1,2,2,1,2,4,1,0,2,2,4,1,2,1,4,0,2,1,5,1,1,1,1,1,3,0,2,7,1,2,1,1,2,0,6,1,5,3,1,0,2,1,1,1,1,1,1,1,1,1,5,0,2,1,1,1,1,1,1,1,1,1,5,0,1,1,4,1,1,1,1,2,1,1,2,0,1,1,1,1,2,1,1,1,2,1,2,1,1,0,3,4,2,1,1,1,2,1,1',\
'0,16,0,5,1,10,0,6,1,2,5,2,0,1,6,3,1,5,0,3,1,3,1,2,1,2,1,2,0,3,1,2,1,1,1,2,2,3,0,4,2,5,1,4,0,4,2,3,6,1,0,2,2,2,1,2,1,1,2,3,0,5,1,1,3,1,2,3,0,5,1,4,2,1,1,2,0,2,7,2,1,1,1,2,0,2,1,3,1,4,1,2,1,1,0,2,1,3,1,4,1,4,0,2,1,4,1,3,1,4,0,3,2,3,2,1,3,2',\
'0,16,0,8,1,7,0,2,7,7,0,8,1,7,0,2,11,3,0,2,1,1,2,2,1,3,1,3,0,5,8,3,0,8,1,2,2,3,0,8,1,2,2,3,0,3,6,4,1,2,0,9,1,3,1,2,0,3,3,1,4,2,1,2,0,1,1,1,1,1,1,1,1,3,1,1,1,2,0,1,1,1,1,1,1,2,1,1,2,1,1,2,0,2,1,3,1,1,2,3,1,2,0,1,7,2,2,2,1,1',\
'0,16,0,2,3,7,1,3,0,5,5,2,1,3,0,1,1,4,1,5,1,3,0,2,1,2,1,3,6,1,0,2,1,2,1,2,1,3,1,3,0,8,1,3,1,3,0,5,1,4,3,3,0,5,1,4,3,3,0,2,4,1,2,3,1,3,0,5,2,5,3,1,0,4,2,1,1,4,1,3,0,3,1,1,1,2,1,3,1,3,0,2,1,2,1,3,1,2,1,3,0,1,1,3,1,4,1,1,1,3,0,5,1,6,2,2',\
'0,16,0,3,1,3,1,8,0,1,9,1,3,2,0,3,1,3,1,2,1,2,1,2,0,2,7,2,3,2,0,3,1,3,1,2,1,2,1,2,0,1,10,2,1,2,0,5,1,5,3,2,0,5,1,5,3,2,0,2,7,1,1,2,1,2,0,2,1,2,1,2,1,1,1,2,1,2,0,2,7,2,3,2,0,2,1,2,1,2,1,2,1,1,1,2,0,1,9,1,1,1,1,2,0,2,1,5,1,1,1,2,1,2,0,2,3,3,1,1,1,3,1,1',\
'0,11,1,4,0,2,6,4,1,3,0,2,1,4,1,4,1,3,0,2,1,4,1,1,1,3,1,2,0,2,1,4,1,2,1,2,1,2,0,2,6,2,4,2,0,2,1,4,1,3,1,4,0,2,1,4,1,1,1,2,1,3,0,2,1,4,1,1,1,2,1,3,0,2,1,4,1,1,3,1,1,2,0,2,6,1,1,2,3,1,0,2,1,4,1,5,1,2,0,2,1,4,1,1,1,1,1,1,1,2,0,2,1,4,1,3,1,1,1,2,0,1,8,2,1,2,1,1,0,14,1,1',\
]

rle1 = ""
oneLineAry = [0 for i in range(256)]
black=(0,0,0)
pos=0
def getSPos(pos):
	if (pos//16)%2==0:return pos
	else:return (16*(pos//16))+(15-(pos%16))
def shiftBy1():
	for i in range(16):
		startx=i*16
		endx=i*16 + 15
		for j in range(15):oneLineAry[startx + j] = oneLineAry[startx + j +1]
		oneLineAry[endx] = 0
def shiftByNeg1():
	sendStr = ""	
	for i in range(16):
		startx = i*16
		endx = i*16 + 15
		sendStr += str(oneLineAry[endx])
		for j in range(15):oneLineAry[endx-j]=oneLineAry[endx-j-1]
		oneLineAry[startx] = 0
	radio.send(sendStr)  #send cell color

def fillo():
	for lines in range(0,16):
		color=1
		painting_cell=0
		while painting_cell<16:
			N=int(getNext())
			print(N)
			while N > 0:
				oneLineAry[ lines * 16 + painting_cell ] = color
				N-=1
				painting_cell+=1
			color=(color+1) % 2
def getNext():
	global rle1,nowIndex,nextIndex
	if nowIndex == -1 : return "-1"
	nextIndex = rle1.find(',',nowIndex+1)
	if nextIndex == -1:
		newStr = rle1[nowIndex+1:]
	else:
		newStr = rle1[nowIndex+1:nextIndex]
	nowIndex = nextIndex
	return newStr
def draw2led(r,g,b):
	for i in range(0,256):
		if oneLineAry[i] == 1:
			led1[getSPos(i)] = (r,g,b)
		else:
			led1[getSPos(i)] = black
while True:
	for rle1 in Taiwanbit:
		nowIndex = 0
		nextIndex = 0
		rle1 = "," + rle1
		fillo()
		draw2led(randint(0,255),randint(0,255),randint(0,255))
		led1.show()
		for i in range(16):
			shiftByNeg1()
			#shiftBy1()
			draw2led(randint(0,255),randint(0,255),randint(0,255))
			led1.show()