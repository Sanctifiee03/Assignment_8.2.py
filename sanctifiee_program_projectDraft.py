# Sanctifiee Musafiri 
# CIS 245-A345
# 9/192020
# Class Project

import requests
import json

# Placeholders containers
myApiKey = "2fc9fec52867d6f2d1c99fb519eb2607"
main_url_path = "http://api.openweathermap.org/data/2.5/weather?"


def cityNameOrZipCode():
	zipCodeOrCity = input ("Enter ZIP code or city name: ")
	while len(zipCodeOrCity) < 1:
		print("Input Not Valid. Please enter a valid ZIP code or city name. \n\n")
		zipCodeOrCity = input("Please Enter a ZIP code or city name: ")
		# print(zipCodeOrCity)
	else:
		if zipCodeOrCity.isnumeric() and (len(zipCodeOrCity) == 5):
			# zipCode = zipCodeOrCity
			# return zipCode
			return main_url_path + 'zip=' + zipCodeOrCity + ',us&appid=' + myApiKey +'&units=imperial'
		else:
			# cityName = zipCodeOrCity
			# return cityName
			return main_url_path + "appid=" + myApiKey + "&q=" + zipCodeOrCity.lower()


def getWeatherData(input):
	response = requests.get(input) 
	cleanResponse = response.json() 
	# print(cleanResponse)
	return cleanResponse


def displayWeatherData(cleanResponse):
	data = cleanResponse
	# Checking for the data availability
	if data["cod"] != "404":
		weatherDescription = data["weather"][0]["description"]
		weatherData = data["main"]
		temperature = weatherData["temp"]
		pressure = weatherData["pressure"]
		humidity = weatherData["humidity"]
		print(" The current temperature (in Fahrenheit) of your city or zip code is  = " +
                    str(temperature) + 
          "\n and the atmospheric pressure of your city or zip code is " +
                    str(pressure) +
          "\n and the humidity (in %) of your city or zip code is " +
                    str(humidity) +
          "\n and the description of your city or zip code is " +
                    str(weatherDescription))
	else:
		print(" The City or ZipCode Weather Data was Not Found ") 


def main():
	print ("Welcome to Sanctifiee’s Weather Data Display Program! ")
	input = cityNameOrZipCode()
	
	# print (input)
	cleanResponse = getWeatherData(input)
	displayWeatherData(cleanResponse)


main()