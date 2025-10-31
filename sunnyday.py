import requests


apikey ="c0c7cb62c5e8740501f9c83e45bd7dd7"
url = "http://api.openweathermap.org/data/2.5/forecast?q=San%20Jose,USA&appid=c0c7cb62c5e8740501f9c83e45bd7dd7"
r = requests.get(url)
print(r.json())

class Weather:

    def __init__(self, apikey, city, lat=None, lon=None):
        url = "http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
        r = requests.get(url)
        self.data = r.json()


    def next_12h(self):
        return self.data

    def next_12h_simplified(self):
        pass

weather = Weather(apikey="c0c7cb62c5e8740501f9c83e45bd7dd7", city="San Jose")
print(weather.data)
print(weather.next_12h())


