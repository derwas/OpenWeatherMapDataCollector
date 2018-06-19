# Credit

This script aims to collect data from OpenWeatherMap and saves results in mongoDB according to a predefined data model. It has been developed by Hela Allani as part of her internship in 2018 under the supervision of Dr. Wassim Derguech.
This sript is used by the project https://github.com/derwas/WeatherStationApplication

## Requirements
 	- Python 2.7: https://www.python.org/download/releases/2.7/
 	- MongoDB 3.2.8: https://www.mongodb.com/download-center?jmp=nav#community


## HOW TO RUN:

1. Clone or unzip this repository
2. Run MongoDB server
3. Create an account in OpenWeatherMap.org
4. Get you API Key
5. Go to root folder of the appliation and edit the file datacollectorOpenWatherMap.py
6. Indicate the city and the country that you want to collect data from and include your API key
7. Indicate the name of the database in mongoDB that will host your data
8. Run the sript as follows: python datacollectorOpenWatherMap.py

## Data Model

The data is saved in mongoDB in different collections: temperature, humidity, windS, windD and weather.
Each document in these collections follows this model in json:

```json
 {
    	"_id" : "2319034d-5dbe-40f7-9f1f-77829c4e3165",
    	"timestamp" : NumberLong("1524163502950"),
    	"unit" : "Degree Celsius",
    	"value" : 15
 }
```
