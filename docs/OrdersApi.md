# swagger_client.OrdersApi

All URIs are relative to *https://stageapi.glovoapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**modify_order_products**](OrdersApi.md#modify_order_products) | **POST** /webhook/stores/{storeId}/orders/{orderId}/replace_products | Modify order products
[**update_order_status**](OrdersApi.md#update_order_status) | **PUT** /webhook/stores/{storeId}/orders/{orderId}/status | Update order status

# **modify_order_products**
> Order2 modify_order_products(content_type, store_id, order_id, body=body)

Modify order products

This option allows an update to the products and attributes of an order when a customer asks for changes or the order cannot be fulfilled as initially requested.  Depending on the information in the request body, we will replace products / attributes from the order, remove products from the order or add products to the order.  An order can only be modified once. An attempt to modify an order more than once will result in an error. 

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
order_id = 'order_id_example' # str | Unique identifier of the order to update
body = swagger_client.ModifyOrder() # ModifyOrder |  (optional)

try:
    # Modify order products
    api_response = api_instance.modify_order_products(content_type, store_id, order_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->modify_order_products: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **order_id** | **str**| Unique identifier of the order to update | 
 **body** | [**ModifyOrder**](ModifyOrder.md)|  | [optional] 

### Return type

[**Order2**](Order2.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_order_status**
> update_order_status(content_type, store_id, order_id, body=body)

Update order status

Allows the update of the order status during different stages of the preparation

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
api_instance = swagger_client.OrdersApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
order_id = 'order_id_example' # str | Unique identifier of the order to update
body = swagger_client.OrderStatus() # OrderStatus |  (optional)

try:
    # Update order status
    api_instance.update_order_status(content_type, store_id, order_id, body=body)
except ApiException as e:
    print("Exception when calling OrdersApi->update_order_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **order_id** | **str**| Unique identifier of the order to update | 
 **body** | [**OrderStatus**](OrderStatus.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

