import datetime, time
import urllib.request
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4
url = "http://192.168.0.7:8080/insert?temp="
try:
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
            #�뜲�씠�� 蹂대궡湲�
            f = urllib.request.urlopen(url+'{0:0.1f}&humi={1:0.1f}'.format(temperature, humidity))
           
            print('temp={0:0.1f}&humi={1:0.1f}'.format(temperature, humidity))
        else:
            print('Failed to get reading. Try again!')       
       
        time.sleep(15)
except KeyboardInterrupt:
    print('Error')
    