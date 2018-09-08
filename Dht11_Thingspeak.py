
import datetime, time
import urllib.request
import random
import Adafruit_DHT


sensor = Adafruit_DHT.DHT11
pin = 4
url = "https://api.thingspeak.com/update?api_key=0IZ0XD1PS2JWXRSJ&field1="


try:
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
            f = urllib.request.urlopen(url+'{0:0.1f}&humidity={1:0.1f}'.format(temperature, humidity))
            print(url+'{0:0.1f}&humidity={1:0.1f}'.format(temperature, humidity))
            data = str(f.read())
            print("recieve data : ", data)
            print('Temp={0:0.1f}&Humidity={1:0.1f}'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')
        
        time.sleep(10)
except KeyboardInterrupt:
    pass