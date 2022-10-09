# swagger_client.MetadataApi

All URIs are relative to */weatherapi/locationforecast/2.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**healthz_get**](MetadataApi.md#healthz_get) | **GET** /healthz | 
[**schema_get**](MetadataApi.md#schema_get) | **GET** /schema | 

# **healthz_get**
> healthz_get()



Check health status for product

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    api_instance.healthz_get()
except ApiException as e:
    print("Exception when calling MetadataApi->healthz_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **schema_get**
> schema_get()



Schema for XML data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MetadataApi()

try:
    api_instance.schema_get()
except ApiException as e:
    print("Exception when calling MetadataApi->schema_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

