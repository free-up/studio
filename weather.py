

from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
from pyowm.utils.config import get_config_from
config_dict = get_config_from('defo.json')


owm = OWM('8e73d515dcfe39452a17e88b4fc00e51', config_dict)
mgr = owm.weather_manager()





# Ищем погоду в городе N
city = input("В каком городе или стране смотрим погоду? ")
observation = mgr.weather_at_place(city)
w = observation.weather
daily_forecaster = mgr.forecast_at_place(city, 'daily')

temp = w.temperature('celsius')["temp"]
rain = w.rain
hum = w.humidity
clo = w.detailed_status
print ("В городе " + city)
print ("Температура за окном " + str(temp) + "°C, " + clo)
# print (rain)
print ("Относительная влажность " + str(hum) + "%")

prognoz = input("Хотите узнать погоду на завтра? y/n")

if prognoz == "y":
	time = input("В какое время интересует погода?")
	tomorrow = timestamps.tomorrow(time)                                  
	weather = daily_forecaster.get_weather_at(tomorrow)
	print ("Завтра в городе ")
	print (city + " в " + str(time) + " " + str(weather))
else:
	input()





