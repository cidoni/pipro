import time
import RPi.GPIO as GPIO

gpioPins=[18,23,24,25,12,16,20,21]
def setupGPIO():
	for p in gpioPins:	
		GPIO.setup(p,GPIO.OUT)
	

def sendToBoard(jn):
	#print(jn[0])
	c=0
	for p in gpioPins:	
		l=ord(jn[c])-48
		GPIO.output(p,l)
		#print(ord(l))
		c=c+1	
	time.sleep(0.05)


GPIO.setmode(GPIO.BCM)
setupGPIO()

max=8

sendToBoard('00000000')

for count in range(1,20):
	for i in range(0,max+1):
		num='{:08b}'.format((2**i)-1)
		#print(num)
		sendToBoard(num)
	for k in range(0,max-1):
        	num='{:08b}'.format((2**(max))-(2**(k+1)))
	        #print(num)
		sendToBoard(num)
	

sendToBoard('00000000')
