import requests, pprint


# apikey ="c0c7cb62c5e8740501f9c83e45bd7dd7"
url = "http://api.openweathermap.org/data/2.5/forecast?q=San%20Jose,USA&appid=c0c7cb62c5e8740501f9c83e45bd7dd7&units=imperial"
url = "http://api.openweathermap.org/data/2.5/forecast?lat=40.1&lon=3.48&appid=c0c7cb62c5e8740501f9c83e45bd7dd7&units=imperial"
# r = requests.get(url)
# print(r.json())

class Weather:
    """Creates a Weather object getting an apikey as input and either a city name or lat and lon coordinates.

    Package use example:
    # Create a weather object using a City name:
    # The api key below is not guranateed to work.
    # Get your own apikey from https://openweathermap.org
    # And wait a couple of hours for the apikey to be activated.

    >>>> weather1 = Weather(apikey="apikey", city="madrid")

    # Using latitude and longitude coordinates

    >>>> weather1 = Weather(apikey="apikey", lat=41.1, lon= -4.1)

    # Get complete weather data for the next 12 hours:

    >>>> weather1.next_12()

    # Simplified data for the next 12 hours:

    >>>> weather1.next_12_simplified()

    """
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
        """
        Returns 3-hour data for the next 12 hours as dict.
        :return:
        """
        # print(self.data)
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a touple of tuples.
        :return:
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description']))
        return simple_data

# weather = Weather(apikey="c0c7cb62c5e8740501f9c83e45bd7dd7", city="San Jose")
weather = Weather(apikey="c0c7cb62c5e8740501f9c83e45bd7dd7", city="Madrid", lat = 4.1, lon = 4.5)
# print(weather.data)
pprint.pprint(weather.next_12h_simplified())


