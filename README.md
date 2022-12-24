# RaspberryPI_with_InfluxDB
Using Raspberry Pi get temperature and humidity form DHT22 and send data to InluxDB Cloud

Using lib DHT22 
  https://github.com/adafruit/Adafruit_Python_DHT
 
Using Influx cloud
  https://www.influxdata.com/
  
Using Grafana to display local
  https://grafana.com/
  
Note:
  Configuration Grafana in local
 
![image](https://user-images.githubusercontent.com/56581148/209429307-5ce319c6-36c4-4232-8d6b-5e382995fd8e.png)

Chose Add your first data source -> InfluxDB

![image](https://user-images.githubusercontent.com/56581148/209429327-18818a64-72f2-468c-a0ed-6616a643df23.png)

InfluxDB cloud using Flux Query Language

![image](https://user-images.githubusercontent.com/56581148/209429366-2fe11d2d-6a9d-452d-9f7b-a623c939738b.png)

Setting Name of Database (You can type anyone name)

![image](https://user-images.githubusercontent.com/56581148/209429393-e5a192b5-5b2a-4885-aa1d-6f84291d4f00.png)

Setting HTTP Url (Url form inluxDB cloud)

![image](https://user-images.githubusercontent.com/56581148/209429405-83ef3c0e-51a4-4135-8a28-d9b990239b57.png)

Setting Authen and InfluxDB detail
- User/ Password: Using user and pass when you register InfluxDB cloud
- Organization:
- Token: Token generate oncetime and hide, so you should copy toke after generate
- Default Bucket: Using bucket you create

![image](https://user-images.githubusercontent.com/56581148/209429435-80efac35-89b3-4a83-b906-c1b6bd90d042.png)

-> Save and test DB if success you get it

![image](https://user-images.githubusercontent.com/56581148/209429685-c7ea01e5-3daf-4c0a-8665-656a7b6ddad7.png)

and if error you get error

Setting DashBoard

![image](https://user-images.githubusercontent.com/56581148/209429580-e7b624b8-ecbe-45cd-860b-41880e67f0e4.png)

You can using influxDB for get tempelate query

![image](https://user-images.githubusercontent.com/56581148/209429791-032aa60a-b069-45b2-9a7d-bbabe89603c9.png)





