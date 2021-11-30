import time
import serial
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
lora = serial.Serial('/dev/serial0', baudrate=9600, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS)
time.sleep(1)

try:
    while True:
        if lora.inWaiting() > 0:
            print("Se recivió algo")
            #data = lora.readline()
            #serialMsg = data.decode('ascii','ignore')
            #print(serialMsg)
            print(lora.read())
except KeyboardInterrupt:
    print('\nExiting Program')
finally:
    lora.close()
    pass