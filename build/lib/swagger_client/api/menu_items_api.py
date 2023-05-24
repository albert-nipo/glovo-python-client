# coding: utf-8

"""
    Glovo Partners API

    # Introduction ## Terminology Here is a detailed explanation of key terms used throughout this documentation: - POS Clients: Partners. Integrators or POS providers seeking to receive orders coming from Glovo directly on their POS System. - Vendors: Physical location where the food is prepared. - POS System: Point-of-sale software on POS Clients side which compiles orders and transactions (online and offline) for a certain number of vendors. - Integration Middleware: Glovo order transmission system, in charge of forwarding orders placed on Glovo platforms to the Vendor POS System. - Plugin: Adapter to be created by the POS Clients if they want to do POS Integrations with Glovo. This adaptor serves to allow communication between - Glovo Integration Middleware and Vendor POS System. - Glovo Order App: Glovo application for vendors where orders placed on a Glovo platform can be processed (accepted). This application is running on a device provided by Glovo (Sunmi device). - Stage environment: demo ecosystem where the integration is meant to be tested as a preliminary step before launching in production  # Getting started ## Integration Process 1. Request access to API via partner.integrationseu@glovoapp.com while providing:   - URL endpoints meant for the Stage environment     - Order dispatch notification endpoint (mandatory)     - Order cancellation notification endpoint (non-mandatory)   - Countries where the integration will operate 2. Obtain the Stage Environment Webhook and access to Glovo’s Jira Support service 3. Obtain access to Glovo’s Stage Environment to develop an integration with a staging store to test Glovo’s API features 4. Develop your Plugin for production 5. Obtain the Production Environment Webhook to launch 6. Production Rollout performed by the alignment between Glovo’s local teams and the Integrator on:   - Timings   - Store/External Ids to identify every store address ## API Credentials You must request credentials to connect with the Integration Middleware and start receiving orders. As mentioned above, reach out to partner.integrationseu@glovoapp.com to do so. When requesting credentials, please provide the following URL endpoints where to receive the order notifications, them being: - Dispatched order notification endpoint (mandatory) - where to receive all incoming orders - Canceled order notification endpoint (non-mandatory) - where to receive notification of the canceled orders  ``` # Example of some webhooks https://yourserver.com/glovo/orders/dispatched https://yourserver.com/glovo/orders/cancelled ``` It is important that all the webhook URLs are accessible from any IP address. To understand more about security for these webhooks, please refer to the [Authentication](#section/Authentication) section. As a general rule, we will be calling your registered webhooks with an HTTPS POST method unless otherwise specified in the notification description. Please refer to the [Order Notifications](#tag/Notifications) section to see all different events you can subscribe to along with the notification schemas.  Credentials will always be shared in an encrypted form through Glovo’s standard process. Credentials are composed of: - Webhook id - URL endpoints - Shared token - unique for all the integration  Read more about authentication [here](#section/Authentication).  ## Unique identifier of the store Glovo uses the following system to manage Partner locations: - Stores - one per city - Store addresses - one per physical location  For every store address you will need to establish a unique identifier also known as store id or external id. Since you could be operating with multiple stores, identifying each one in every operation is essential. It's important that you hold and share with us an unique identifier for every store integrated through this API. This identifier will be requested for every endpoint call as a path parameter: ```http /stores/YOUR-STORE-ID/... ``` We will also make sure that you receive it as part all notifications we will be sending to your webhooks: ```json {   ...   \"store_id\": \"YOUR-STORE-ID\",   ... } ``` ## Marketplace orders The delivery of an order can be either taken care by a Glovo courier or by the store itself. For the cases Glovo is not involved in the delivery process we identify these stores as **marketplace**. Through this documention you will see notes and references destinated to these types of stores that require extra information to fulfill an order.  # Build the Plugin - You must build a plugin to be able to receive orders from Glovo. - Your plugin will translate incoming orders to a language understandable by your POS system. - Technical specification of all endpoints and actions available on the plugin scope can be found [here](#tag/Notifications). ## Send Order Updates - The Integration Middleware is used by chains or POS providers to accept or reject orders. - Technical specification of all endpoints and actions available on the Integration Middleware scope can be found [here](#section/Getting-started) TO-DO: NO ANDA ## Scheduling - You must be able to retrieve the current store schedule - Ability to temporarily modify schedules  # Best Usage Policy Please follow these guidelines in order to reduce potential issues that could delay rollout of your integration.  We strongly advise before using our system that the you check two important concepts: - The rate limit for the endpoint that you are intending to used is respected by the systems that will call it. - That the menu uploaded matches our [JSON schema](#json-schema), or it will be rejected as part of the upload process. - All image urls that are uploaded to the system should use the protocol HTTPS for security reasons - the JSON schema above will reject any that are not served by it.  If either of these cause issues or are not understood please contact your account manager for further information and support.  # Store Image Guidelines  It is important to select appropriate images as the structure of store's menu affects the visual display of the products and directly impacts the user experience in both the Glovo app and the website.       ## Product Images  Product images are nice-to-have but not mandatory.    Specifications:      * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1MB          * Background: light, plain colour or plain texture (e.g. wooden)          * Protocol: HTTPS      * You must show the product in a frontal plane          * Each product separately    Note: It's important to maintain the coherent style of the product images (e.g. follow the same color palette and perspective) and keep in mind that for improving the user’s experience, it is recommended to have either all the products with an image or no pictures at all. Having only a few products with images across the menu creates visual chaos and can unwillingly contribute to boosting sales of only those products with visual representation.     In the most common menu type (with Sections only) the products that contain images will be displayed as below:    <div align=\"center\" class=\"img-div\">   <img alt=\"product image 1\" src=\"img/product_image_1.png#center\" /> </div>  After selecting any product, the image becomes square:   <div align=\"center\" class=\"img-div\">   <img alt=\"product image 2\" src=\"img/product_image_2.png#center\" /> </div>  ## Collection Images  These are mandatory for all collections if a store is configured with the Grid View layout.    Specifications:        * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1.5 MB          * Background: light, plain colour (except white and yellow) or plain texture (e.g. wooden)          * Protocol: HTTPS          * The images should have at least 2 products from that Collection  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_grid_view.png#center\" /> </div>  In case a store is configured with the List View layout, collection images are generated automatically from 3 selected images of products grouped under the same collection. They will be displayed together as seen below:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_list_view.png#center\" /> </div>   ## Supercollection Images  These are mandatory for all supercollections.    Specifications:      * Orientation: Horizontal.            * Dimensions - 2484 x 1380 px.            * Format: JPG.            * File size: below 1,5 MB      * Protocol: HTTPS.            * Must show the product in a close-up, without transparency            * They can not be photomontages or contain logos or promotional elements pasted on the image            * They can have the logo of the brand applied to commercial elements as napkins, tablecloths, etc.  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/supercollection_image.png#center\" /> </div>  ## Future changes  Please note that this part of the document is flux. There is the possibility of changes to some of the images specified here in the near future.  # Authentication  A static `token` to operate with our API will be provided by your AM. It's important that you keep it in a secure place. All API calls must be made over HTTPS.   The token won't be require to be changed over time, but if you think it was compromised in some way, please contact us so we can generate a new one.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: partner.integrationseu@glovoapp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class MenuItemsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def bulk_update_items(self, content_type, store_id, **kwargs):  # noqa: E501
        """Bulk update items  # noqa: E501

        Allows you to partially modify multiple products and attributes as part of a single request.  If there are fields of the items you want to leave unchanged, simply do not specify them in the request (see the JSON example). Do not set the value of fields you do not want to modify - neither to null nor to an empty array!  This process is asynchronous, so we will provide a `transaction_id` to follow the process with the [Verify bulk update items status endpoint](#operation/Verify-bulk-update-items)  This is a convenient option when you have to perform massive updates in your store catalog. Although this is an async process, the performance is significantly better than sending a request per product with the `PATCH` endpoints.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   The maximum number of items that can be processed in a single request is <strong>10000</strong>. In case the total number is exceeded the request will return an error. </div>  If for some reason the Glovo system fails while updating, it is possible for the bulk update process to succeed only partially: some items will be updated while others will not. Concrete details will be given on the bulk update status endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_update_items(content_type, store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param BulkUpdateItems body:
        :return: TransactionId
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bulk_update_items_with_http_info(content_type, store_id, **kwargs)  # noqa: E501
        else:
            (data) = self.bulk_update_items_with_http_info(content_type, store_id, **kwargs)  # noqa: E501
            return data

    def bulk_update_items_with_http_info(self, content_type, store_id, **kwargs):  # noqa: E501
        """Bulk update items  # noqa: E501

        Allows you to partially modify multiple products and attributes as part of a single request.  If there are fields of the items you want to leave unchanged, simply do not specify them in the request (see the JSON example). Do not set the value of fields you do not want to modify - neither to null nor to an empty array!  This process is asynchronous, so we will provide a `transaction_id` to follow the process with the [Verify bulk update items status endpoint](#operation/Verify-bulk-update-items)  This is a convenient option when you have to perform massive updates in your store catalog. Although this is an async process, the performance is significantly better than sending a request per product with the `PATCH` endpoints.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   The maximum number of items that can be processed in a single request is <strong>10000</strong>. In case the total number is exceeded the request will return an error. </div>  If for some reason the Glovo system fails while updating, it is possible for the bulk update process to succeed only partially: some items will be updated while others will not. Concrete details will be given on the bulk update status endpoint.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_update_items_with_http_info(content_type, store_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param BulkUpdateItems body:
        :return: TransactionId
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'store_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method bulk_update_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `bulk_update_items`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `bulk_update_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/stores/{storeId}/menu/updates', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionId',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_attribute(self, content_type, store_id, attribute_id, **kwargs):  # noqa: E501
        """Modify attributes  # noqa: E501

        Allows you to perform a partial update over an attribute. Only the attributes sent in the request will be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_attribute(content_type, store_id, attribute_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str attribute_id: Unique identifier of the attribute within a store (required)
        :param ModifyAttribute body:
        :return: ModifyAttributeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_attribute_with_http_info(content_type, store_id, attribute_id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_attribute_with_http_info(content_type, store_id, attribute_id, **kwargs)  # noqa: E501
            return data

    def modify_attribute_with_http_info(self, content_type, store_id, attribute_id, **kwargs):  # noqa: E501
        """Modify attributes  # noqa: E501

        Allows you to perform a partial update over an attribute. Only the attributes sent in the request will be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_attribute_with_http_info(content_type, store_id, attribute_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str attribute_id: Unique identifier of the attribute within a store (required)
        :param ModifyAttribute body:
        :return: ModifyAttributeResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'store_id', 'attribute_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_attribute" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `modify_attribute`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `modify_attribute`")  # noqa: E501
        # verify the required parameter 'attribute_id' is set
        if ('attribute_id' not in params or
                params['attribute_id'] is None):
            raise ValueError("Missing the required parameter `attribute_id` when calling `modify_attribute`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'attribute_id' in params:
            path_params['attributeId'] = params['attribute_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/stores/{storeId}/attributes/{attributeId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifyAttributeResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_product(self, content_type, store_id, product_id, **kwargs):  # noqa: E501
        """Modify products  # noqa: E501

        Allows you to perform a partial update over a product. Only the attributes sent in the request will be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_product(content_type, store_id, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str product_id: Unique identifier of the product within a store (required)
        :param ModifyProduct body:
        :return: ModifyProductResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_product_with_http_info(content_type, store_id, product_id, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_product_with_http_info(content_type, store_id, product_id, **kwargs)  # noqa: E501
            return data

    def modify_product_with_http_info(self, content_type, store_id, product_id, **kwargs):  # noqa: E501
        """Modify products  # noqa: E501

        Allows you to perform a partial update over a product. Only the attributes sent in the request will be updated.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_product_with_http_info(content_type, store_id, product_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str content_type: Specify that the content will be sent as JSON (required)
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str product_id: Unique identifier of the product within a store (required)
        :param ModifyProduct body:
        :return: ModifyProductResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['content_type', 'store_id', 'product_id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_product" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'content_type' is set
        if ('content_type' not in params or
                params['content_type'] is None):
            raise ValueError("Missing the required parameter `content_type` when calling `modify_product`")  # noqa: E501
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `modify_product`")  # noqa: E501
        # verify the required parameter 'product_id' is set
        if ('product_id' not in params or
                params['product_id'] is None):
            raise ValueError("Missing the required parameter `product_id` when calling `modify_product`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'product_id' in params:
            path_params['productId'] = params['product_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'content_type' in params:
            header_params['Content-Type'] = params['content_type']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/stores/{storeId}/products/{productId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ModifyProductResult',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def verify_bulk_update_items(self, store_id, transaction_id, **kwargs):  # noqa: E501
        """Verify bulk update items status  # noqa: E501

        Allows you to check the status of the items bulk update process in Glovo for a particular `transaction_id`.  These are the possible status:  * `SUCCESS`: The bulk update process finished successfully * `PROCESSING`: The bulk update process has not finished yet * `PARTIALLY_PROCESSED`: Some of the products/attributes submitted in the request could not have been updated. The \"Products/Attributes updated\" and \"Products/Attributes not updated\" arrays in the \"details\" field contain the corresponding IDs. * `NOT_PROCESSED`: The bulk update process finished with errors due to incorrect setup * `GLOVO_ERROR`: The bulk update process finished unsuccessfully due to an error in the Glovo system  If the status indicates an error, we will send additional information to help you understand the cause.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   If the status of your bulk update is <code>NOT_PROCESSED</code> or <code>GLOVO_ERROR</code>, please contact your account manager for support. </div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_bulk_update_items(store_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str transaction_id: Unique identifier of the bulk update transaction to follow (required)
        :return: BulkUpdateItemsStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.verify_bulk_update_items_with_http_info(store_id, transaction_id, **kwargs)  # noqa: E501
        else:
            (data) = self.verify_bulk_update_items_with_http_info(store_id, transaction_id, **kwargs)  # noqa: E501
            return data

    def verify_bulk_update_items_with_http_info(self, store_id, transaction_id, **kwargs):  # noqa: E501
        """Verify bulk update items status  # noqa: E501

        Allows you to check the status of the items bulk update process in Glovo for a particular `transaction_id`.  These are the possible status:  * `SUCCESS`: The bulk update process finished successfully * `PROCESSING`: The bulk update process has not finished yet * `PARTIALLY_PROCESSED`: Some of the products/attributes submitted in the request could not have been updated. The \"Products/Attributes updated\" and \"Products/Attributes not updated\" arrays in the \"details\" field contain the corresponding IDs. * `NOT_PROCESSED`: The bulk update process finished with errors due to incorrect setup * `GLOVO_ERROR`: The bulk update process finished unsuccessfully due to an error in the Glovo system  If the status indicates an error, we will send additional information to help you understand the cause.  <div class=\"alert-box info\">   <i data-feather=\"info\"></i>   If the status of your bulk update is <code>NOT_PROCESSED</code> or <code>GLOVO_ERROR</code>, please contact your account manager for support. </div>   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.verify_bulk_update_items_with_http_info(store_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str store_id: [Unique identifier of the store](#section/Getting-started/Unique-identifier-of-the-store)  (required)
        :param str transaction_id: Unique identifier of the bulk update transaction to follow (required)
        :return: BulkUpdateItemsStatus
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_id', 'transaction_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method verify_bulk_update_items" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'store_id' is set
        if ('store_id' not in params or
                params['store_id'] is None):
            raise ValueError("Missing the required parameter `store_id` when calling `verify_bulk_update_items`")  # noqa: E501
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `verify_bulk_update_items`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'store_id' in params:
            path_params['storeId'] = params['store_id']  # noqa: E501
        if 'transaction_id' in params:
            path_params['transactionId'] = params['transaction_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['token']  # noqa: E501

        return self.api_client.call_api(
            '/webhook/stores/{storeId}/menu/updates/{transactionId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BulkUpdateItemsStatus',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
