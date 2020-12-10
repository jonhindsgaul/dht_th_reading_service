import sys
import time
from datetime import datetime
import os
import socket

# Remember to install packages!!!
import pymongo
from pymongo import MongoClient

# Adafruit_DHT library to read the sensor
import Adafruit_DHT

#Assuming the database is at the user level
os.chdir('/home/pi/database/')

#Sensor type and Raspberry Pi Zero W GPIO pin in use
sensor = 11
pin = 4

#MongoDB access
client = MongoClient('mongodb url')
db = client.dhtreadings

#Reading the sensor - somhuetimes the reading is troublesome, because DHT11 sensors can be difficult to read
def dht_read(sensor, pin):
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
        return humidity, temperature
    except:
        print("Failed to read, trying again")
        time.sleep(1)
        dht_read(sensor, pin)

#Posting to MongoDBs
def mongodb_post(db,humidity,temperature):
    post = {
        "Sensor": socket.gethostname(),
        "Temperature": temperature,
        "Humidity": humidity,
        "Time": datetime.now(),
    }
    posts = db.posts
    posts.insert_one(post).inserted_id
    print("Post successfully inserted in MongoDB")

#Making the script run
while True:
    humidity, temperature = dht_read(sensor, pin)
    mongodb_post(db, humidity, temperature)
    time.sleep(900.0)
