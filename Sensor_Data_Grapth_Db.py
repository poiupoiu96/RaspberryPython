import Adafruit_DHT
import pymysql


sensor = Adafruit_DHT.DHT11
pin = 4
url = "http://192.168.0.7:8080/insert?temp="
try:
    
    conn = pymysql.connect(host='localhost',user='iot', password='iot',db='iot_schema', port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
    cur = conn.cursor()  
   
                    
    while True:
       
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)       
        
        if humidity is not None and temperature is not None:
          
             cur.execute('INSERT INTO sensors(temperature,humidity) VALUES(?,?)', (temperature,humidity))
             conn.commit()
        else:
            print('Failed to get reading. Try again!')       
       
        time.sleep(15)
except KeyboardInterrupt:
    console.log('에러 발생')
    
finally:
    conn.close()
    cur.close()
    