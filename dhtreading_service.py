import sys
import Adafruit_DHT

import time
from datetime import datetime
import os

os.chdir('/home/pi/database/')

sensor = 11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

def dht11_read():
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        datastr = ["Time: ", str(datetime.now()), " Temp: ", str(temperature), "C  Humidity: ", str(humidity), "%\n "]
        filename = "datafile.txt"
        append_copy = open(filename, "r")
        original_text = append_copy.read()
        append_copy.close()
        append_copy = open(filename, "w")
        append_copy.write(''.join(datastr))
        append_copy.write(original_text)
        append_copy.close()
        print("Recording succeeded")
    except:
        print("Failed to read, trying again")
        time.sleep(1)
        dht11_read()

while True:
    dht11_read()
    time.sleep(900.0)

