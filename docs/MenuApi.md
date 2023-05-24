# swagger_client.MenuApi

All URIs are relative to *https://stageapi.glovoapp.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_menu**](MenuApi.md#upload_menu) | **POST** /webhook/stores/{storeId}/menu | Upload menu
[**validate_menu**](MenuApi.md#validate_menu) | **POST** /paris/menu/validate | Validate menu
[**verify_upload_menu**](MenuApi.md#verify_upload_menu) | **GET** /webhook/stores/{storeId}/menu/{transactionId} | Verify menu upload

# **upload_menu**
> TransactionId upload_menu(content_type, store_id, body=body)

Upload menu

Allows you to upload or update the entire menu of a store in Glovo.  This process is asynchronous, so we will provide a `transaction_id` to follow the process with the [Verify menu upload endpoint](#operation/Verify-upload-menu)  <div align=\"center\">   <img alt=\"menu flow\" src=\"img/menu_update_process.png#center\" /> </div>  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   There is a maximum number of 5 of menu updates allowed per day per store address. For small products and attributes updates please use the individual or bulk endpoints. </div>  In case the limit is reached we will return status code 429 (too many requests).  If for some reason the Glovo system fails while updating, no changes will be made at all to avoid inconsistencies. 

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
api_instance = swagger_client.MenuApi(swagger_client.ApiClient(configuration))
content_type = 'application/json' # str | Specify that the content will be sent as JSON (default to application/json)
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
body = swagger_client.StoreIdMenuBody() # StoreIdMenuBody |  (optional)

try:
    # Upload menu
    api_response = api_instance.upload_menu(content_type, store_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->upload_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **content_type** | **str**| Specify that the content will be sent as JSON | [default to application/json]
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **body** | [**StoreIdMenuBody**](StoreIdMenuBody.md)|  | [optional] 

### Return type

[**TransactionId**](TransactionId.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **validate_menu**
> MenuValidationResponse validate_menu(body=body)

Validate menu

Allows you to upload a menu and validate it against the current JSON schema definition. You will receive either an all-OK message or a list of errors and a list of warnings that the menu would generate along with details of the errors

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.MenuApi()
body = swagger_client.Menu2() # Menu2 |  (optional)

try:
    # Validate menu
    api_response = api_instance.validate_menu(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->validate_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Menu2**](Menu2.md)|  | [optional] 

### Return type

[**MenuValidationResponse**](MenuValidationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_upload_menu**
> MenuUploadStatus verify_upload_menu(store_id, transaction_id)

Verify menu upload

 Allows you to check the status of the menu update process in Glovo for a particular `transaction_id`.  These are the possible status:  * `SUCCESS`: The menu update process finished successfully * `PROCESSING`: The menu update process has not finished yet * `FETCH_MENU_INVALID_PAYLOAD`: The menu update process finished with errors caused by invalid JSON input * `FETCH_MENU_SERVER_ERROR`: The menu update process finished with errors trying to download the menu from the partner URL (eg. time-out, invalid URL, etc.) * `FETCH_MENU_UNAUTHORIZED`: The menu update process finished with errors trying to download the menu from the partner URL (eg. authorization errors) * `NOT_PROCESSED`: The menu update process finished with errors due to incorrect integration setup * `LIMIT_EXCEEDED`: The maximum number of menu updates allowed per day per store address was exceeded * `GLOVO_ERROR`: The menu update process finished unsuccessfully due to an error in the Glovo system  If the status indicates an error, we will send additional information to help you understand the cause.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   If the status of your menu update is <code>NOT_PROCESSED</code> or <code>GLOVO_ERROR</code>, please contact your account manager for support. </div> 

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
api_instance = swagger_client.MenuApi(swagger_client.ApiClient(configuration))
store_id = 'store_id_example' # str | [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store) 
transaction_id = 'transaction_id_example' # str | Unique identifier of the menu update transaction to follow

try:
    # Verify menu upload
    api_response = api_instance.verify_upload_menu(store_id, transaction_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->verify_upload_menu: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_id** | **str**| [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  | 
 **transaction_id** | **str**| Unique identifier of the menu update transaction to follow | 

### Return type

[**MenuUploadStatus**](MenuUploadStatus.md)

### Authorization

[token](../README.md#token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

