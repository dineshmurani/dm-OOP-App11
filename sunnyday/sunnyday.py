import requests


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

    sample url to get sky condition icons:

    https://openweathermap.org/img/wn/10d@2x.png

    """
    def __init__(self, apikey, city=None, lat=None, lon=None):
        if city:
            url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={apikey}&units=imperial"
            r = requests.get(url)
            self.data = r.json()

        elif lat and lon:
            url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}8&appid={apikey}&units=imperial"

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
        return self.data['list'][:4]

    def next_12h_simplified(self):
        """
        Returns date, temperature, and sky condition every 3 hours
        for the next 12 hours as a touple of tuples.
        :return:
        """
        simple_data = []
        for dicty in self.data['list'][:4]:
            simple_data.append((dicty['dt_txt'], dicty['main']['temp'], dicty['weather'][0]['description'], dicty['weather'][0]['icon']))
        return simple_data




