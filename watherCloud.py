import Adafruit_DHT, adafruit_bh1750
import influxdb_client, os, time, random, board
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

os.environ['INFLUXDB_TOKEN']='8e23q8daqJSKGyFr0DFD2JYEyRCVoJG7pAIGGIhoozsPdGqKzuQeM6XCJOnAGk9bUCYlFVeKFkvttHOm3iychg=='
token = os.environ.get("INFLUXDB_TOKEN")
org = "Weather"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

print("Connect server done: ",type(client))

sensor = Adafruit_DHT.DHT22
pin = 17

i2c = board.I2C()
light = adafruit_bh1750.BH1750(i2c)

bucket="weather_data"
write_api = client.write_api(write_options=SYNCHRONOUS)

def updateServer(temp, humi, light):
  temperature_point = (
    Point("weather")
    .tag("weather", "weather")
    .field("temperature", temp)
  )

  humidity_point = (
    Point("weather")
    .tag("weather", "weather")
    .field("humidity", humi)
  )

  light_point = (
    Point("weather")
    .tag("weather", "weather")
    .field("light", light.lux)
  )

  print("Temperature: ",temp," Humidity: ",humi)
  write_api.write(bucket=bucket, org=org, record=temperature_point)
  write_api.write(bucket=bucket, org=org, record=humidity_point)
  write_api.write(bucket=bucket, org=org, record=light_point)

print("Push data form Pi to server")  
while 1:
  _humi, _temp = Adafruit_DHT.read_retry(sensor, pin)
  print("Light: %.2f Lux"%sensor.lux)

  if _humi is not None and _temp is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(_humi, _temp))
    updateServer(_temp,_humi,light)
  else:
    print('Failed to get reading. Try again!')

  time.sleep(15) # separate points by 15 second

