# Getting Started

## Installation
```sh
pip install git+https://github.com/pwrtux/pyMetnoForecast.git
```

## Example

```python
from __future__ import print_function
from distutils.command.config import config
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

conf = swagger_client.Configuration()
conf.host = "https://api.met.no/weatherapi/locationforecast/2.0"

# create an instance of the API class
api_instance = swagger_client.DataApi(swagger_client.ApiClient(conf))
lat = 50.1106444 # float | Latitude
lon = 8.6820917 # float | Longitude

try:
    api_response = api_instance.complete_get(lat, lon)
except ApiException as e:
    print("Exception when calling DataApi->complete_get: %s\n" % e)


# Print date and temperture of all forecasts
newforecast = api_response.properties.timeseries
for i in newforecast:
    pprint(f"{i.time}  {i.data.instant.details.air_temperature}°C")
```


## TODO
- [ ] Add location lookup for coordinates
- [ ] Hardcode host url

## Further Documentation
Look at [the auto generated Readme from Swagger](swagger_README.md)