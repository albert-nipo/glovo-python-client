# coding: utf-8

"""
    Glovo Partners API

    # Introduction ## Terminology Here is a detailed explanation of key terms used throughout this documentation: - POS Clients: Partners. Integrators or POS providers seeking to receive orders coming from Glovo directly on their POS System. - Vendors: Physical location where the food is prepared. - POS System: Point-of-sale software on POS Clients side which compiles orders and transactions (online and offline) for a certain number of vendors. - Integration Middleware: Glovo order transmission system, in charge of forwarding orders placed on Glovo platforms to the Vendor POS System. - Plugin: Adapter to be created by the POS Clients if they want to do POS Integrations with Glovo. This adaptor serves to allow communication between - Glovo Integration Middleware and Vendor POS System. - Glovo Order App: Glovo application for vendors where orders placed on a Glovo platform can be processed (accepted). This application is running on a device provided by Glovo (Sunmi device). - Stage environment: demo ecosystem where the integration is meant to be tested as a preliminary step before launching in production  # Getting started ## Integration Process 1. Request access to API via partner.integrationseu@glovoapp.com while providing:   - URL endpoints meant for the Stage environment     - Order dispatch notification endpoint (mandatory)     - Order cancellation notification endpoint (non-mandatory)   - Countries where the integration will operate 2. Obtain the Stage Environment Webhook and access to Glovo’s Jira Support service 3. Obtain access to Glovo’s Stage Environment to develop an integration with a staging store to test Glovo’s API features 4. Develop your Plugin for production 5. Obtain the Production Environment Webhook to launch 6. Production Rollout performed by the alignment between Glovo’s local teams and the Integrator on:   - Timings   - Store/External Ids to identify every store address ## API Credentials You must request credentials to connect with the Integration Middleware and start receiving orders. As mentioned above, reach out to partner.integrationseu@glovoapp.com to do so. When requesting credentials, please provide the following URL endpoints where to receive the order notifications, them being: - Dispatched order notification endpoint (mandatory) - where to receive all incoming orders - Canceled order notification endpoint (non-mandatory) - where to receive notification of the canceled orders  ``` # Example of some webhooks https://yourserver.com/glovo/orders/dispatched https://yourserver.com/glovo/orders/cancelled ``` It is important that all the webhook URLs are accessible from any IP address. To understand more about security for these webhooks, please refer to the [Authentication](#section/Authentication) section. As a general rule, we will be calling your registered webhooks with an HTTPS POST method unless otherwise specified in the notification description. Please refer to the [Order Notifications](#tag/Notifications) section to see all different events you can subscribe to along with the notification schemas.  Credentials will always be shared in an encrypted form through Glovo’s standard process. Credentials are composed of: - Webhook id - URL endpoints - Shared token - unique for all the integration  Read more about authentication [here](#section/Authentication).  ## Unique identifier of the store Glovo uses the following system to manage Partner locations: - Stores - one per city - Store addresses - one per physical location  For every store address you will need to establish a unique identifier also known as store id or external id. Since you could be operating with multiple stores, identifying each one in every operation is essential. It's important that you hold and share with us an unique identifier for every store integrated through this API. This identifier will be requested for every endpoint call as a path parameter: ```http /stores/YOUR-STORE-ID/... ``` We will also make sure that you receive it as part all notifications we will be sending to your webhooks: ```json {   ...   \"store_id\": \"YOUR-STORE-ID\",   ... } ``` ## Marketplace orders The delivery of an order can be either taken care by a Glovo courier or by the store itself. For the cases Glovo is not involved in the delivery process we identify these stores as **marketplace**. Through this documention you will see notes and references destinated to these types of stores that require extra information to fulfill an order.  # Build the Plugin - You must build a plugin to be able to receive orders from Glovo. - Your plugin will translate incoming orders to a language understandable by your POS system. - Technical specification of all endpoints and actions available on the plugin scope can be found [here](#tag/Notifications). ## Send Order Updates - The Integration Middleware is used by chains or POS providers to accept or reject orders. - Technical specification of all endpoints and actions available on the Integration Middleware scope can be found [here](#section/Getting-started) TO-DO: NO ANDA ## Scheduling - You must be able to retrieve the current store schedule - Ability to temporarily modify schedules  # Best Usage Policy Please follow these guidelines in order to reduce potential issues that could delay rollout of your integration.  We strongly advise before using our system that the you check two important concepts: - The rate limit for the endpoint that you are intending to used is respected by the systems that will call it. - That the menu uploaded matches our [JSON schema](#json-schema), or it will be rejected as part of the upload process. - All image urls that are uploaded to the system should use the protocol HTTPS for security reasons - the JSON schema above will reject any that are not served by it.  If either of these cause issues or are not understood please contact your account manager for further information and support.  # Store Image Guidelines  It is important to select appropriate images as the structure of store's menu affects the visual display of the products and directly impacts the user experience in both the Glovo app and the website.       ## Product Images  Product images are nice-to-have but not mandatory.    Specifications:      * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1MB          * Background: light, plain colour or plain texture (e.g. wooden)          * Protocol: HTTPS      * You must show the product in a frontal plane          * Each product separately    Note: It's important to maintain the coherent style of the product images (e.g. follow the same color palette and perspective) and keep in mind that for improving the user’s experience, it is recommended to have either all the products with an image or no pictures at all. Having only a few products with images across the menu creates visual chaos and can unwillingly contribute to boosting sales of only those products with visual representation.     In the most common menu type (with Sections only) the products that contain images will be displayed as below:    <div align=\"center\" class=\"img-div\">   <img alt=\"product image 1\" src=\"img/product_image_1.png#center\" /> </div>  After selecting any product, the image becomes square:   <div align=\"center\" class=\"img-div\">   <img alt=\"product image 2\" src=\"img/product_image_2.png#center\" /> </div>  ## Collection Images  These are mandatory for all collections if a store is configured with the Grid View layout.    Specifications:        * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1.5 MB          * Background: light, plain colour (except white and yellow) or plain texture (e.g. wooden)          * Protocol: HTTPS          * The images should have at least 2 products from that Collection  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_grid_view.png#center\" /> </div>  In case a store is configured with the List View layout, collection images are generated automatically from 3 selected images of products grouped under the same collection. They will be displayed together as seen below:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_list_view.png#center\" /> </div>   ## Supercollection Images  These are mandatory for all supercollections.    Specifications:      * Orientation: Horizontal.            * Dimensions - 2484 x 1380 px.            * Format: JPG.            * File size: below 1,5 MB      * Protocol: HTTPS.            * Must show the product in a close-up, without transparency            * They can not be photomontages or contain logos or promotional elements pasted on the image            * They can have the logo of the brand applied to commercial elements as napkins, tablecloths, etc.  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/supercollection_image.png#center\" /> </div>  ## Future changes  Please note that this part of the document is flux. There is the possibility of changes to some of the images specified here in the near future.  # Authentication  A static `token` to operate with our API will be provided by your AM. It's important that you keep it in a secure place. All API calls must be made over HTTPS.   The token won't be require to be changed over time, but if you think it was compromised in some way, please contact us so we can generate a new one.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: partner.integrationseu@glovoapp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import six
from six.moves.urllib.parse import urlencode

try:
    import urllib3
except ImportError:
    raise ImportError('Swagger python client requires urllib3.')


logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):

    def __init__(self, resp):
        self.urllib3_response = resp
        self.status = resp.status
        self.reason = resp.reason
        self.data = resp.data

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.urllib3_response.getheaders()

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.urllib3_response.getheader(name, default)


class RESTClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        # urllib3.PoolManager will pass all kw parameters to connectionpool
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/poolmanager.py#L75  # noqa: E501
        # https://github.com/shazow/urllib3/blob/f9409436f83aeb79fbaf090181cd81b784f1b8ce/urllib3/connectionpool.py#L680  # noqa: E501
        # maxsize is the number of requests to host that are allowed in parallel  # noqa: E501
        # Custom SSL certificates and client certificates: http://urllib3.readthedocs.io/en/latest/advanced-usage.html  # noqa: E501

        # cert_reqs
        if configuration.verify_ssl:
            cert_reqs = ssl.CERT_REQUIRED
        else:
            cert_reqs = ssl.CERT_NONE

        # ca_certs
        if configuration.ssl_ca_cert:
            ca_certs = configuration.ssl_ca_cert
        else:
            # if not set certificate file, use Mozilla's root certificates.
            ca_certs = certifi.where()

        addition_pool_args = {}
        if configuration.assert_hostname is not None:
            addition_pool_args['assert_hostname'] = configuration.assert_hostname  # noqa: E501

        if maxsize is None:
            if configuration.connection_pool_maxsize is not None:
                maxsize = configuration.connection_pool_maxsize
            else:
                maxsize = 4

        # https pool manager
        if configuration.proxy:
            self.pool_manager = urllib3.ProxyManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                proxy_url=configuration.proxy,
                **addition_pool_args
            )
        else:
            self.pool_manager = urllib3.PoolManager(
                num_pools=pools_size,
                maxsize=maxsize,
                cert_reqs=cert_reqs,
                ca_certs=ca_certs,
                cert_file=configuration.cert_file,
                key_file=configuration.key_file,
                **addition_pool_args
            )

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
        """Perform requests.

        :param method: http request method
        :param url: http request url
        :param query_params: query parameters in the url
        :param headers: http request headers
        :param body: request json body, for `application/json`
        :param post_params: request post parameters,
                            `application/x-www-form-urlencoded`
                            and `multipart/form-data`
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        """
        method = method.upper()
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT',
                          'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError(
                "body parameter cannot be used with post_params parameter."
            )

        post_params = post_params or {}
        headers = headers or {}

        timeout = None
        if _request_timeout:
            if isinstance(_request_timeout, (int, ) if six.PY3 else (int, long)):  # noqa: E501,F821
                timeout = urllib3.Timeout(total=_request_timeout)
            elif (isinstance(_request_timeout, tuple) and
                  len(_request_timeout) == 2):
                timeout = urllib3.Timeout(
                    connect=_request_timeout[0], read=_request_timeout[1])

        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        try:
            # For `POST`, `PUT`, `PATCH`, `OPTIONS`, `DELETE`
            if method in ['POST', 'PUT', 'PATCH', 'OPTIONS', 'DELETE']:
                if query_params:
                    url += '?' + urlencode(query_params)
                if re.search('json', headers['Content-Type'], re.IGNORECASE):
                    request_body = '{}'
                    if body is not None:
                        request_body = json.dumps(body)
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'application/x-www-form-urlencoded':  # noqa: E501
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=False,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                elif headers['Content-Type'] == 'multipart/form-data':
                    # must del headers['Content-Type'], or the correct
                    # Content-Type which generated by urllib3 will be
                    # overwritten.
                    del headers['Content-Type']
                    r = self.pool_manager.request(
                        method, url,
                        fields=post_params,
                        encode_multipart=True,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                # Pass a `string` parameter directly in the body to support
                # other content types than Json when `body` argument is
                # provided in serialized form
                elif isinstance(body, str):
                    request_body = body
                    r = self.pool_manager.request(
                        method, url,
                        body=request_body,
                        preload_content=_preload_content,
                        timeout=timeout,
                        headers=headers)
                else:
                    # Cannot generate the request from given parameters
                    msg = """Cannot prepare a request message for provided
                             arguments. Please check that your arguments match
                             declared content type."""
                    raise ApiException(status=0, reason=msg)
            # For `GET`, `HEAD`
            else:
                r = self.pool_manager.request(method, url,
                                              fields=query_params,
                                              preload_content=_preload_content,
                                              timeout=timeout,
                                              headers=headers)
        except urllib3.exceptions.SSLError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

            # log response body
            logger.debug("response body: %s", r.data)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class ApiException(Exception):

    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
