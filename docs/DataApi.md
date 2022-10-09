# swagger_client.DataApi

All URIs are relative to */weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**classic_format_get**](DataApi.md#classic_format_get) | **GET** /classic.{format} | 
[**classic_get**](DataApi.md#classic_get) | **GET** /classic | 
[**compact_format_get**](DataApi.md#compact_format_get) | **GET** /compact.{format} | 
[**compact_get**](DataApi.md#compact_get) | **GET** /compact | 
[**complete_format_get**](DataApi.md#complete_format_get) | **GET** /complete.{format} | 
[**complete_get**](DataApi.md#complete_get) | **GET** /complete | 
[**status_format_get**](DataApi.md#status_format_get) | **GET** /status.{format} | 
[**status_get**](DataApi.md#status_get) | **GET** /status | 

# **classic_format_get**
> str classic_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
format = 'format_example' # str | format code (file extension)
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.classic_format_get(lat, lon, format, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->classic_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **classic_get**
> str classic_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.classic_get(lat, lon, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->classic_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compact_format_get**
> METJSONForecast compact_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
format = 'format_example' # str | format code (file extension)
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.compact_format_get(lat, lon, format, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->compact_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compact_get**
> METJSONForecast compact_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.compact_get(lat, lon, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->compact_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_format_get**
> METJSONForecast complete_format_get(lat, lon, format, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
format = 'format_example' # str | format code (file extension)
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.complete_format_get(lat, lon, format, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->complete_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **format** | **str**| format code (file extension) | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **complete_get**
> METJSONForecast complete_get(lat, lon, altitude=altitude)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
lat = 3.4 # float | Latitude
lon = 3.4 # float | Longitude
altitude = 56 # int | Whole meters above sea level (optional)

try:
    api_response = api_instance.complete_get(lat, lon, altitude=altitude)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->complete_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lat** | **float**| Latitude | 
 **lon** | **float**| Longitude | 
 **altitude** | **int**| Whole meters above sea level | [optional] 

### Return type

[**METJSONForecast**](METJSONForecast.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_format_get**
> str status_format_get(format)



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()
format = 'format_example' # str | format code (file extension)

try:
    api_response = api_instance.status_format_get(format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->status_format_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **format** | **str**| format code (file extension) | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **status_get**
> str status_get()



Weather forecast for a specified place

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DataApi()

try:
    api_response = api_instance.status_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataApi->status_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json;charset=UTF-8

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

