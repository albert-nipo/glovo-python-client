# swagger_client.SchedulingApi

All URIs are relative to *https://stageapi.glovoapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**active_temporary_closing**](SchedulingApi.md#active_temporary_closing) | **GET** /webhook/stores/{storeId}/closing | Active temporary closing
[**close_temporaly**](SchedulingApi.md#close_temporaly) | **PUT** /webhook/stores/{storeId}/closing | Close temporaly
[**remove_close_temporaly**](SchedulingApi.md#remove_close_temporaly) | **DELETE** /webhook/stores/{storeId}/closing | Remove temporary closing
[**store_schedule**](SchedulingApi.md#store_schedule) | **GET** /webhook/stores/{storeId}/schedule | Schedule

# **active_temporary_closing**
> InlineResponse200 active_temporary_closing(store_id)

Active temporary closing

Allows you to get an active store temporary closure if any.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchedulingApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 

try:
    # Active temporary closing
    api_response = api_instance.active_temporary_closing(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulingApi->active_temporary_closing: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **close_temporaly**
> close_temporaly(content_type, store_id, body=body)

Close temporaly

Allows you to close a store temporarily until a specified date and time in the future. This will ignore the opening times defined in the store schedule, forcing the store to be closed until the specified date and time.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchedulingApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
body = swagger_client.StoreIdClosingBody() # StoreIdClosingBody |  (optional)

try:
    # Close temporaly
    api_instance.close_temporaly(content_type, store_id, body=body)
except ApiException as e:
    print("Exception when calling SchedulingApi->close_temporaly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **body** | [**StoreIdClosingBody**](StoreIdClosingBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_close_temporaly**
> remove_close_temporaly(store_id)

Remove temporary closing

Allows you to remove an active temporary closure for a store. After the removal, the store will continue following their regular schedule.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchedulingApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 

try:
    # Remove temporary closing
    api_instance.remove_close_temporaly(store_id)
except ApiException as e:
    print("Exception when calling SchedulingApi->remove_close_temporaly: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **store_schedule**
> StoreSchedule store_schedule(store_id)

Schedule

Allows you to get the current schedule for a particular store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: token
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.SchedulingApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 

try:
    # Schedule
    api_response = api_instance.store_schedule(store_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulingApi->store_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 

### Return type

[**StoreSchedule**](StoreSchedule.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

