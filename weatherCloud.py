# Add thư viện DHT và BH1750
import adafruit_dht, adafruit_bh1750
# Add thư viện influbDB client
import influxdb_client, os, time, random, board
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

# Khai bao cac bien trong influxDB
os.environ['INFLUXDB_TOKEN']='8e23q8daqJSKGyFr0DFD2JYEyRCVoJG7pAIGGIhoozsPdGqKzuQeM6XCJOnAGk9bUCYlFVeKFkvttHOm3iychg=='
token = os.environ.get("INFLUXDB_TOKEN")
org = "Weather"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket="weather_data"
write_api = client.write_api(write_options=SYNCHRONOUS)

print("Connect server done: ",type(client))

# Khai báo chân và kiểu DHT 
dhtDevice = adafruit_dht.DHT11(board.D17)

# Khai báo chân I2C và connect tới BH1750 
i2c = board.I2C()
light = adafruit_bh1750.BH1750(i2c)

# Function send data to server 
def updateServer(temp, humi, light):
  # Khoi tao cac point data 
  temperature_point = (
    Point("weather")
    .tag("weather", "temperature")
    .field("temperature", temp)
  )

  humidity_point = (
    Point("weather")
    .tag("weather", "humidity")
    .field("humidity", humi)
  )

  light_point = (
    Point("weather")
    .tag("weather", "light")
    .field("light", light)
  )

  print("Temperature: ",temp," Humidity: ",humi)
  # Send data len server 
  write_api.write(bucket=bucket, org=org, record=temperature_point)
  write_api.write(bucket=bucket, org=org, record=humidity_point)
  write_api.write(bucket=bucket, org=org, record=light_point)

print("Push data form Pi to server")  
while 1:
  # Doc gia tri nhiet do, do am, anh sang 
  _humi = dhtDevice.humidity
  _temp = dhtDevice.temperature
  print("Light: %.2f Lux"%light.lux)

  # Kiem tra neu gia tri nhiet do, do am thoa man 
  if _humi is not None and _temp is not None:
    print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(_humi, _temp))
    # Gui data len server 
    updateServer(_temp,_humi,light.lux)
  else:
    print('Failed to get reading. Try again!')

  time.sleep(5) # separate points by 5 second

