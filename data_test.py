import influxdb_client, os, time, random
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

os.environ['INFLUXDB_TOKEN']='8e23q8daqJSKGyFr0DFD2JYEyRCVoJG7pAIGGIhoozsPdGqKzuQeM6XCJOnAGk9bUCYlFVeKFkvttHOm3iychg=='
token = os.environ.get("INFLUXDB_TOKEN")
org = "Weather"
url = "https://europe-west1-1.gcp.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)

print("Connect server done: ",type(client))

bucket="weather_data"
write_api = client.write_api(write_options=SYNCHRONOUS)

print("Push data form Pi to server")  
for value in range(1000):

  temp = random.randrange(20,27)
  humi = random.randrange(55,70)
  light = random.randrange(100, 200)

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
    .tag("light", "light")
    .field("light", light)
  )

  print("Temperature: ",temp," Humidity: ",humi, "light: ",light)
  write_api.write(bucket=bucket, org=org, record=temperature_point)
  write_api.write(bucket=bucket, org=org, record=humidity_point)
  write_api.write(bucket=bucket, org=org, record=light_point)
  time.sleep(5) # separate points by 1 second

