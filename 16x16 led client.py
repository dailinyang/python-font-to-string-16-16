import radio
import neopixel
from microbit import *
from random import randint
led1=neopixel.NeoPixel(pin2,256)
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
def shiftByNeg1(inc):
	for i in range(16):
		endx = i*16 + 15
		for j in range(15):oneLineAry[endx-j]=oneLineAry[endx-j-1]
	for i in range(16):
		startx = i*16
		oneLineAry[startx] = int(inc[i])
def draw2led(r,g,b):
	for i in range(0,256):
		if oneLineAry[i] == 1:
			led1[getSPos(i)] = (r,g,b)
		else:
			led1[getSPos(i)] = black
radio.on()
while True:
  inc = radio.receive()
  if inc:
	  draw2led(randint(0,255),randint(0,255),randint(0,255))
	  led1.show()
	  shiftByNeg1(str(inc))
