# swagger_client.MenuItemsApi

All URIs are relative to *https://stageapi.glovoapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_update_items**](MenuItemsApi.md#bulk_update_items) | **POST** /webhook/stores/{storeId}/menu/updates | Bulk update items
[**modify_attribute**](MenuItemsApi.md#modify_attribute) | **PATCH** /webhook/stores/{storeId}/attributes/{attributeId} | Modify attributes
[**modify_product**](MenuItemsApi.md#modify_product) | **PATCH** /webhook/stores/{storeId}/products/{productId} | Modify products
[**verify_bulk_update_items**](MenuItemsApi.md#verify_bulk_update_items) | **GET** /webhook/stores/{storeId}/menu/updates/{transactionId} | Verify bulk update items status

# **bulk_update_items**
> TransactionId bulk_update_items(content_type, store_id, body=body)

Bulk update items

Allows you to partially modify multiple products and attributes as part of a single request.  If there are fields of the items you want to leave unchanged, simply do not specify them in the request (see the JSON example). Do not set the value of fields you do not want to modify - neither to null nor to an empty array!  This process is asynchronous, so we will provide a `transaction_id` to follow the process with the [Verify bulk update items status endpoint](#operation/Verify-bulk-update-items)  This is a convenient option when you have to perform massive updates in your store catalog. Although this is an async process, the performance is significantly better than sending a request per product with the `PATCH` endpoints.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   The maximum number of items that can be processed in a single request is <strong>10000</strong>. In case the total number is exceeded the request will return an error. </div>  If for some reason the Glovo system fails while updating, it is possible for the bulk update process to succeed only partially: some items will be updated while others will not. Concrete details will be given on the bulk update status endpoint. 

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
api_instance = swagger_client.MenuItemsApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
body = swagger_client.BulkUpdateItems() # BulkUpdateItems |  (optional)

try:
    # Bulk update items
    api_response = api_instance.bulk_update_items(content_type, store_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuItemsApi->bulk_update_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **body** | [**BulkUpdateItems**](BulkUpdateItems.md)|  | [optional] 

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_attribute**
> ModifyAttributeResult modify_attribute(content_type, store_id, attribute_id, body=body)

Modify attributes

Allows you to perform a partial update over an attribute. Only the attributes sent in the request will be updated.

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
api_instance = swagger_client.MenuItemsApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
attribute_id = 'attribute_id_example' # str | Unique identifier of the attribute within a store
body = swagger_client.ModifyAttribute() # ModifyAttribute |  (optional)

try:
    # Modify attributes
    api_response = api_instance.modify_attribute(content_type, store_id, attribute_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuItemsApi->modify_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **attribute_id** | **str**| Unique identifier of the attribute within a store | 
 **body** | [**ModifyAttribute**](ModifyAttribute.md)|  | [optional] 

### Return type

[**ModifyAttributeResult**](ModifyAttributeResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **modify_product**
> ModifyProductResult modify_product(content_type, store_id, product_id, body=body)

Modify products

Allows you to perform a partial update over a product. Only the attributes sent in the request will be updated.

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
api_instance = swagger_client.MenuItemsApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
product_id = 'product_id_example' # str | Unique identifier of the product within a store
body = swagger_client.ModifyProduct() # ModifyProduct |  (optional)

try:
    # Modify products
    api_response = api_instance.modify_product(content_type, store_id, product_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuItemsApi->modify_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **product_id** | **str**| Unique identifier of the product within a store | 
 **body** | [**ModifyProduct**](ModifyProduct.md)|  | [optional] 

### Return type

[**ModifyProductResult**](ModifyProductResult.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_bulk_update_items**
> BulkUpdateItemsStatus verify_bulk_update_items(store_id, transaction_id)

Verify bulk update items status

Allows you to check the status of the items bulk update process in Glovo for a particular `transaction_id`.  These are the possible status:  * `SUCCESS`: The bulk update process finished successfully * `PROCESSING`: The bulk update process has not finished yet * `PARTIALLY_PROCESSED`: Some of the products/attributes submitted in the request could not have been updated. The \"Products/Attributes updated\" and \"Products/Attributes not updated\" arrays in the \"details\" field contain the corresponding IDs. * `NOT_PROCESSED`: The bulk update process finished with errors due to incorrect setup * `GLOVO_ERROR`: The bulk update process finished unsuccessfully due to an error in the Glovo system  If the status indicates an error, we will send additional information to help you understand the cause.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   If the status of your bulk update is <code>NOT_PROCESSED</code> or <code>GLOVO_ERROR</code>, please contact your account manager for support. </div> 

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
api_instance = swagger_client.MenuItemsApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
transaction_id = 'transaction_id_example' # str | Unique identifier of the bulk update transaction to follow

try:
    # Verify bulk update items status
    api_response = api_instance.verify_bulk_update_items(store_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuItemsApi->verify_bulk_update_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **transaction_id** | **str**| Unique identifier of the bulk update transaction to follow | 

### Return type

[**BulkUpdateItemsStatus**](BulkUpdateItemsStatus.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

