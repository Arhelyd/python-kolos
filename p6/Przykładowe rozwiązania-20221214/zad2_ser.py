from urllib.request import urlopen, Request
from json import loads

response = urlopen(Request('https://api.met.no/weatherapi/locationforecast/'
                           '2.0/compact?lat=55.25&lon=22.56667',
                   headers={'User-Agent': 'MyAgent'}))

forecast_json = response.read()
fr = loads(forecast_json)

print(fr['properties']['timeseries'][2]['time'])

print(fr['properties']['timeseries'][2]['data']
        ['instant']['details']['air_temperature'])

print(fr['properties']['timeseries'][2]['data']
        ['instant']['details']['air_pressure_at_sea_level'])
