# swagger-client
# Introduction ## Terminology Here is a detailed explanation of key terms used throughout this documentation: - POS Clients: Partners. Integrators or POS providers seeking to receive orders coming from Glovo directly on their POS System. - Vendors: Physical location where the food is prepared. - POS System: Point-of-sale software on POS Clients side which compiles orders and transactions (online and offline) for a certain number of vendors. - Integration Middleware: Glovo order transmission system, in charge of forwarding orders placed on Glovo platforms to the Vendor POS System. - Plugin: Adapter to be created by the POS Clients if they want to do POS Integrations with Glovo. This adaptor serves to allow communication between - Glovo Integration Middleware and Vendor POS System. - Glovo Order App: Glovo application for vendors where orders placed on a Glovo platform can be processed (accepted). This application is running on a device provided by Glovo (Sunmi device). - Stage environment: demo ecosystem where the integration is meant to be tested as a preliminary step before launching in production  # Getting started ## Integration Process 1. Request access to API via partner.integrationseu@glovoapp.com while providing:   - URL endpoints meant for the Stage environment     - Order dispatch notification endpoint (mandatory)     - Order cancellation notification endpoint (non-mandatory)   - Countries where the integration will operate 2. Obtain the Stage Environment Webhook and access to Glovo’s Jira Support service 3. Obtain access to Glovo’s Stage Environment to develop an integration with a staging store to test Glovo’s API features 4. Develop your Plugin for production 5. Obtain the Production Environment Webhook to launch 6. Production Rollout performed by the alignment between Glovo’s local teams and the Integrator on:   - Timings   - Store/External Ids to identify every store address ## API Credentials You must request credentials to connect with the Integration Middleware and start receiving orders. As mentioned above, reach out to partner.integrationseu@glovoapp.com to do so. When requesting credentials, please provide the following URL endpoints where to receive the order notifications, them being: - Dispatched order notification endpoint (mandatory) - where to receive all incoming orders - Canceled order notification endpoint (non-mandatory) - where to receive notification of the canceled orders  ``` # Example of some webhooks https://yourserver.com/glovo/orders/dispatched https://yourserver.com/glovo/orders/cancelled ``` It is important that all the webhook URLs are accessible from any IP address. To understand more about security for these webhooks, please refer to the [Authentication](#section/Authentication) section. As a general rule, we will be calling your registered webhooks with an HTTPS POST method unless otherwise specified in the notification description. Please refer to the [Order Notifications](#tag/Notifications) section to see all different events you can subscribe to along with the notification schemas.  Credentials will always be shared in an encrypted form through Glovo’s standard process. Credentials are composed of: - Webhook id - URL endpoints - Shared token - unique for all the integration  Read more about authentication [here](#section/Authentication).  ## Unique identifier of the store Glovo uses the following system to manage Partner locations: - Stores - one per city - Store addresses - one per physical location  For every store address you will need to establish a unique identifier also known as store id or external id. Since you could be operating with multiple stores, identifying each one in every operation is essential. It's important that you hold and share with us an unique identifier for every store integrated through this API. This identifier will be requested for every endpoint call as a path parameter: ```http /stores/YOUR-STORE-ID/... ``` We will also make sure that you receive it as part all notifications we will be sending to your webhooks: ```json {   ...   \"store_id\": \"YOUR-STORE-ID\",   ... } ``` ## Marketplace orders The delivery of an order can be either taken care by a Glovo courier or by the store itself. For the cases Glovo is not involved in the delivery process we identify these stores as **marketplace**. Through this documention you will see notes and references destinated to these types of stores that require extra information to fulfill an order.  # Build the Plugin - You must build a plugin to be able to receive orders from Glovo. - Your plugin will translate incoming orders to a language understandable by your POS system. - Technical specification of all endpoints and actions available on the plugin scope can be found [here](#tag/Notifications). ## Send Order Updates - The Integration Middleware is used by chains or POS providers to accept or reject orders. - Technical specification of all endpoints and actions available on the Integration Middleware scope can be found [here](#section/Getting-started) TO-DO: NO ANDA ## Scheduling - You must be able to retrieve the current store schedule - Ability to temporarily modify schedules  # Best Usage Policy Please follow these guidelines in order to reduce potential issues that could delay rollout of your integration.  We strongly advise before using our system that the you check two important concepts: - The rate limit for the endpoint that you are intending to used is respected by the systems that will call it. - That the menu uploaded matches our [JSON schema](#json-schema), or it will be rejected as part of the upload process. - All image urls that are uploaded to the system should use the protocol HTTPS for security reasons - the JSON schema above will reject any that are not served by it.  If either of these cause issues or are not understood please contact your account manager for further information and support.  # Store Image Guidelines  It is important to select appropriate images as the structure of store's menu affects the visual display of the products and directly impacts the user experience in both the Glovo app and the website.       ## Product Images  Product images are nice-to-have but not mandatory.    Specifications:      * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1MB          * Background: light, plain colour or plain texture (e.g. wooden)          * Protocol: HTTPS      * You must show the product in a frontal plane          * Each product separately    Note: It's important to maintain the coherent style of the product images (e.g. follow the same color palette and perspective) and keep in mind that for improving the user’s experience, it is recommended to have either all the products with an image or no pictures at all. Having only a few products with images across the menu creates visual chaos and can unwillingly contribute to boosting sales of only those products with visual representation.     In the most common menu type (with Sections only) the products that contain images will be displayed as below:    <div align=\"center\" class=\"img-div\">   <img alt=\"product image 1\" src=\"img/product_image_1.png#center\" /> </div>  After selecting any product, the image becomes square:   <div align=\"center\" class=\"img-div\">   <img alt=\"product image 2\" src=\"img/product_image_2.png#center\" /> </div>  ## Collection Images  These are mandatory for all collections if a store is configured with the Grid View layout.    Specifications:        * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1.5 MB          * Background: light, plain colour (except white and yellow) or plain texture (e.g. wooden)          * Protocol: HTTPS          * The images should have at least 2 products from that Collection  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_grid_view.png#center\" /> </div>  In case a store is configured with the List View layout, collection images are generated automatically from 3 selected images of products grouped under the same collection. They will be displayed together as seen below:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_list_view.png#center\" /> </div>   ## Supercollection Images  These are mandatory for all supercollections.    Specifications:      * Orientation: Horizontal.            * Dimensions - 2484 x 1380 px.            * Format: JPG.            * File size: below 1,5 MB      * Protocol: HTTPS.            * Must show the product in a close-up, without transparency            * They can not be photomontages or contain logos or promotional elements pasted on the image            * They can have the logo of the brand applied to commercial elements as napkins, tablecloths, etc.  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/supercollection_image.png#center\" /> </div>  ## Future changes  Please note that this part of the document is flux. There is the possibility of changes to some of the images specified here in the near future.  # Authentication  A static `token` to operate with our API will be provided by your AM. It's important that you keep it in a secure place. All API calls must be made over HTTPS.   The token won't be require to be changed over time, but if you think it was compromised in some way, please contact us so we can generate a new one.  <SecurityDefinitions /> 

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

# create an instance of the API class
api_instance = swagger_client.MenuApi(swagger_client.ApiClient(configuration))
body = swagger_client.Menu2() # Menu2 |  (optional)

try:
    # Validate menu
    api_response = api_instance.validate_menu(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MenuApi->validate_menu: %s\n" % e)

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

## Documentation for API Endpoints

All URIs are relative to *https://stageapi.glovoapp.com*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*MenuApi* | [**upload_menu**](docs/MenuApi.md#upload_menu) | **POST** /webhook/stores/{storeId}/menu | Upload menu
*MenuApi* | [**validate_menu**](docs/MenuApi.md#validate_menu) | **POST** /paris/menu/validate | Validate menu
*MenuApi* | [**verify_upload_menu**](docs/MenuApi.md#verify_upload_menu) | **GET** /webhook/stores/{storeId}/menu/{transactionId} | Verify menu upload
*MenuItemsApi* | [**bulk_update_items**](docs/MenuItemsApi.md#bulk_update_items) | **POST** /webhook/stores/{storeId}/menu/updates | Bulk update items
*MenuItemsApi* | [**modify_attribute**](docs/MenuItemsApi.md#modify_attribute) | **PATCH** /webhook/stores/{storeId}/attributes/{attributeId} | Modify attributes
*MenuItemsApi* | [**modify_product**](docs/MenuItemsApi.md#modify_product) | **PATCH** /webhook/stores/{storeId}/products/{productId} | Modify products
*MenuItemsApi* | [**verify_bulk_update_items**](docs/MenuItemsApi.md#verify_bulk_update_items) | **GET** /webhook/stores/{storeId}/menu/updates/{transactionId} | Verify bulk update items status
*OrdersApi* | [**modify_order_products**](docs/OrdersApi.md#modify_order_products) | **POST** /webhook/stores/{storeId}/orders/{orderId}/replace_products | Modify order products
*OrdersApi* | [**update_order_status**](docs/OrdersApi.md#update_order_status) | **PUT** /webhook/stores/{storeId}/orders/{orderId}/status | Update order status
*SchedulingApi* | [**active_temporary_closing**](docs/SchedulingApi.md#active_temporary_closing) | **GET** /webhook/stores/{storeId}/closing | Active temporary closing
*SchedulingApi* | [**close_temporaly**](docs/SchedulingApi.md#close_temporaly) | **PUT** /webhook/stores/{storeId}/closing | Close temporaly
*SchedulingApi* | [**remove_close_temporaly**](docs/SchedulingApi.md#remove_close_temporaly) | **DELETE** /webhook/stores/{storeId}/closing | Remove temporary closing
*SchedulingApi* | [**store_schedule**](docs/SchedulingApi.md#store_schedule) | **GET** /webhook/stores/{storeId}/schedule | Schedule

## Documentation For Models

 - [AllOfOrder2OrderId](docs/AllOfOrder2OrderId.md)
 - [AllOfOrder2StoreId](docs/AllOfOrder2StoreId.md)
 - [AllOfOrderCancelledOrderId](docs/AllOfOrderCancelledOrderId.md)
 - [AllOfOrderCancelledStoreId](docs/AllOfOrderCancelledStoreId.md)
 - [AllOfOrderOrderId](docs/AllOfOrderOrderId.md)
 - [AllOfOrderStoreId](docs/AllOfOrderStoreId.md)
 - [BadRequest](docs/BadRequest.md)
 - [BulkUpdateItems](docs/BulkUpdateItems.md)
 - [BulkUpdateItemsAttributes](docs/BulkUpdateItemsAttributes.md)
 - [BulkUpdateItemsProducts](docs/BulkUpdateItemsProducts.md)
 - [BulkUpdateItemsRestrictions](docs/BulkUpdateItemsRestrictions.md)
 - [BulkUpdateItemsStatus](docs/BulkUpdateItemsStatus.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Menu](docs/Menu.md)
 - [Menu2](docs/Menu2.md)
 - [MenuAttributeGroups](docs/MenuAttributeGroups.md)
 - [MenuAttributes](docs/MenuAttributes.md)
 - [MenuCollections](docs/MenuCollections.md)
 - [MenuProducts](docs/MenuProducts.md)
 - [MenuRestrictions](docs/MenuRestrictions.md)
 - [MenuSections](docs/MenuSections.md)
 - [MenuSupercollections](docs/MenuSupercollections.md)
 - [MenuUploadStatus](docs/MenuUploadStatus.md)
 - [MenuValidationResponse](docs/MenuValidationResponse.md)
 - [ModifyAttribute](docs/ModifyAttribute.md)
 - [ModifyAttributeResult](docs/ModifyAttributeResult.md)
 - [ModifyOrder](docs/ModifyOrder.md)
 - [ModifyOrderAddedProducts](docs/ModifyOrderAddedProducts.md)
 - [ModifyOrderAttributes](docs/ModifyOrderAttributes.md)
 - [ModifyOrderProduct](docs/ModifyOrderProduct.md)
 - [ModifyOrderProductAttributes](docs/ModifyOrderProductAttributes.md)
 - [ModifyOrderReplacements](docs/ModifyOrderReplacements.md)
 - [ModifyProduct](docs/ModifyProduct.md)
 - [ModifyProductResult](docs/ModifyProductResult.md)
 - [Order](docs/Order.md)
 - [Order2](docs/Order2.md)
 - [OrderAttributes](docs/OrderAttributes.md)
 - [OrderCancelled](docs/OrderCancelled.md)
 - [OrderCourier](docs/OrderCourier.md)
 - [OrderCustomer](docs/OrderCustomer.md)
 - [OrderCustomerInvoicingDetails](docs/OrderCustomerInvoicingDetails.md)
 - [OrderDeliveryAddress](docs/OrderDeliveryAddress.md)
 - [OrderId](docs/OrderId.md)
 - [OrderProducts](docs/OrderProducts.md)
 - [OrderStatus](docs/OrderStatus.md)
 - [StoreId](docs/StoreId.md)
 - [StoreIdClosingBody](docs/StoreIdClosingBody.md)
 - [StoreIdMenuBody](docs/StoreIdMenuBody.md)
 - [StoreSchedule](docs/StoreSchedule.md)
 - [StoreScheduleSchedule](docs/StoreScheduleSchedule.md)
 - [StoreScheduleTimeSlots](docs/StoreScheduleTimeSlots.md)
 - [TransactionId](docs/TransactionId.md)

## Documentation For Authorization


## token

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author

partner.integrationseu@glovoapp.com
