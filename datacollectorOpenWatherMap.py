import urllib, json
import uuid
import time
from pymongo import MongoClient


def getDataFromAPI(url):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
    return data


def getTemperatureData(data):
    temp = {}
    temp["_id"] = str(uuid.uuid4())
    temp["timestamp"] = int (round(time.time()*1000))
    temp ["value"] = data ['main']['temp']
    temp ["unit"] = "Degree Celsius"
    return temp


def getHumidityData(data):
    humidity = {}
    humidity["_id"] = str(uuid.uuid4())
    humidity["timestamp"] = int (round(time.time()*1000))
    humidity ["value"] = data ['main']['humidity']
    humidity ["unit"] = "%"
    return humidity


def getWindSData(data):
    windS = {}
    windS["_id"] = str(uuid.uuid4())
    windS["timestamp"] = int (round(time.time()*1000))
    windS["value"] = data ['wind']['speed']
    windS ["unit"] = "Wind speed, mps"
    return windS


def getWeather(data):
    weather = {}
    weather["_id"] = str(uuid.uuid4())
    weather["timestamp"] = int (round(time.time()*1000))
    weather["main"] = data ['weather'][0]['main']
    weather ["description"] =  data ['weather'][0]['description']
    weather["icon"] = data ['weather'][0]['icon']
    return weather


def getWindDData(data):
    windD = {}
    windD["_id"] = str(uuid.uuid4())
    windD["timestamp"] = int (round(time.time()*1000))
    windD["value"] = data ['wind']['deg']
    windD ["unit"] = "Wind direction ,deg "
    return windD


def saveToMongo(db,collection, document):
    client = MongoClient()
    base = client [db]
    coll= base[collection]
    coll.insert(document)


def main():
    apidata = getDataFromAPI("http://api.openweathermap.org/data/2.5/weather?q=[city,country]&appid=[your api key]&units=metric")
    saveToMongo([database name],"temperature", getTemperatureData(apidata))
    print "temperature data saved "
    saveToMongo([database name],"humidity", getHumidityData(apidata))
    print "humidity data saved"
    saveToMongo([database name],"windS", getWindSData(apidata))
    print "wind speed data saved"
    saveToMongo([database name],"windD", getWindDData(apidata))
    print "wind direction data saved"
    saveToMongo([database name],"weather", getWeather(apidata))
    print "weather condition saved"

if __name__ == "__main__":
    main()





