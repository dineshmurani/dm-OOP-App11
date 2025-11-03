import requests, pprint


# apikey ="c0c7cb62c5e8740501f9c83e45bd7dd7"
url = "http://api.openweathermap.org/data/2.5/forecast?q=San%20Jose,USA&appid=c0c7cb62c5e8740501f9c83e45bd7dd7&units=imperial"
url = "http://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.48&appid=c0c7cb62c5e8740501f9c83e45bd7dd7&units=imperial"
# r = requests.get(url)
# print(r.json())

class Weather:

    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()
            # print(self.data)
        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}8&appid={apikey}&units=imperial"
            # print(url)
            r = requests.get(url)
            self.data = r.json()
        else:
            raise TypeError("provide either a city or lat and lon arguments")

        if self.data['cod'] != "200":
            raise ValueError(self.data["message"])


    def next_12h(self):
        # print(self.data)
        return self.data['list'][:4]

    def next_12h_simplified(self):
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
        return simple_data

# weather = Weather(apikey="c0c7cb62c5e8740501f9c83e45bd7dd7", city="San Jose")
weather = Weather(apikey="c0c7cb62c5e8740501f9c83e45bd7dd7", city="Madrid", lat = 4.1, lon = 4.5)
# print(weather.data)
pprint.pprint(weather.next_12h_simplified())


