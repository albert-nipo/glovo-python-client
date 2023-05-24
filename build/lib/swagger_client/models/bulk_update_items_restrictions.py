# coding: utf-8

"""
    Glovo Partners API

    # Introduction ## Terminology Here is a detailed explanation of key terms used throughout this documentation: - POS Clients: Partners. Integrators or POS providers seeking to receive orders coming from Glovo directly on their POS System. - Vendors: Physical location where the food is prepared. - POS System: Point-of-sale software on POS Clients side which compiles orders and transactions (online and offline) for a certain number of vendors. - Integration Middleware: Glovo order transmission system, in charge of forwarding orders placed on Glovo platforms to the Vendor POS System. - Plugin: Adapter to be created by the POS Clients if they want to do POS Integrations with Glovo. This adaptor serves to allow communication between - Glovo Integration Middleware and Vendor POS System. - Glovo Order App: Glovo application for vendors where orders placed on a Glovo platform can be processed (accepted). This application is running on a device provided by Glovo (Sunmi device). - Stage environment: demo ecosystem where the integration is meant to be tested as a preliminary step before launching in production  # Getting started ## Integration Process 1. Request access to API via partner.integrationseu@glovoapp.com while providing:   - URL endpoints meant for the Stage environment     - Order dispatch notification endpoint (mandatory)     - Order cancellation notification endpoint (non-mandatory)   - Countries where the integration will operate 2. Obtain the Stage Environment Webhook and access to Glovo’s Jira Support service 3. Obtain access to Glovo’s Stage Environment to develop an integration with a staging store to test Glovo’s API features 4. Develop your Plugin for production 5. Obtain the Production Environment Webhook to launch 6. Production Rollout performed by the alignment between Glovo’s local teams and the Integrator on:   - Timings   - Store/External Ids to identify every store address ## API Credentials You must request credentials to connect with the Integration Middleware and start receiving orders. As mentioned above, reach out to partner.integrationseu@glovoapp.com to do so. When requesting credentials, please provide the following URL endpoints where to receive the order notifications, them being: - Dispatched order notification endpoint (mandatory) - where to receive all incoming orders - Canceled order notification endpoint (non-mandatory) - where to receive notification of the canceled orders  ``` # Example of some webhooks https://yourserver.com/glovo/orders/dispatched https://yourserver.com/glovo/orders/cancelled ``` It is important that all the webhook URLs are accessible from any IP address. To understand more about security for these webhooks, please refer to the [Authentication](#section/Authentication) section. As a general rule, we will be calling your registered webhooks with an HTTPS POST method unless otherwise specified in the notification description. Please refer to the [Order Notifications](#tag/Notifications) section to see all different events you can subscribe to along with the notification schemas.  Credentials will always be shared in an encrypted form through Glovo’s standard process. Credentials are composed of: - Webhook id - URL endpoints - Shared token - unique for all the integration  Read more about authentication [here](#section/Authentication).  ## Unique identifier of the store Glovo uses the following system to manage Partner locations: - Stores - one per city - Store addresses - one per physical location  For every store address you will need to establish a unique identifier also known as store id or external id. Since you could be operating with multiple stores, identifying each one in every operation is essential. It's important that you hold and share with us an unique identifier for every store integrated through this API. This identifier will be requested for every endpoint call as a path parameter: ```http /stores/YOUR-STORE-ID/... ``` We will also make sure that you receive it as part all notifications we will be sending to your webhooks: ```json {   ...   \"store_id\": \"YOUR-STORE-ID\",   ... } ``` ## Marketplace orders The delivery of an order can be either taken care by a Glovo courier or by the store itself. For the cases Glovo is not involved in the delivery process we identify these stores as **marketplace**. Through this documention you will see notes and references destinated to these types of stores that require extra information to fulfill an order.  # Build the Plugin - You must build a plugin to be able to receive orders from Glovo. - Your plugin will translate incoming orders to a language understandable by your POS system. - Technical specification of all endpoints and actions available on the plugin scope can be found [here](#tag/Notifications). ## Send Order Updates - The Integration Middleware is used by chains or POS providers to accept or reject orders. - Technical specification of all endpoints and actions available on the Integration Middleware scope can be found [here](#section/Getting-started) TO-DO: NO ANDA ## Scheduling - You must be able to retrieve the current store schedule - Ability to temporarily modify schedules  # Best Usage Policy Please follow these guidelines in order to reduce potential issues that could delay rollout of your integration.  We strongly advise before using our system that the you check two important concepts: - The rate limit for the endpoint that you are intending to used is respected by the systems that will call it. - That the menu uploaded matches our [JSON schema](#json-schema), or it will be rejected as part of the upload process. - All image urls that are uploaded to the system should use the protocol HTTPS for security reasons - the JSON schema above will reject any that are not served by it.  If either of these cause issues or are not understood please contact your account manager for further information and support.  # Store Image Guidelines  It is important to select appropriate images as the structure of store's menu affects the visual display of the products and directly impacts the user experience in both the Glovo app and the website.       ## Product Images  Product images are nice-to-have but not mandatory.    Specifications:      * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1MB          * Background: light, plain colour or plain texture (e.g. wooden)          * Protocol: HTTPS      * You must show the product in a frontal plane          * Each product separately    Note: It's important to maintain the coherent style of the product images (e.g. follow the same color palette and perspective) and keep in mind that for improving the user’s experience, it is recommended to have either all the products with an image or no pictures at all. Having only a few products with images across the menu creates visual chaos and can unwillingly contribute to boosting sales of only those products with visual representation.     In the most common menu type (with Sections only) the products that contain images will be displayed as below:    <div align=\"center\" class=\"img-div\">   <img alt=\"product image 1\" src=\"img/product_image_1.png#center\" /> </div>  After selecting any product, the image becomes square:   <div align=\"center\" class=\"img-div\">   <img alt=\"product image 2\" src=\"img/product_image_2.png#center\" /> </div>  ## Collection Images  These are mandatory for all collections if a store is configured with the Grid View layout.    Specifications:        * Orientation: Square.          * Dimensions: 1000 x 1000 px.          * Format: JPG.          * File size: below 1.5 MB          * Background: light, plain colour (except white and yellow) or plain texture (e.g. wooden)          * Protocol: HTTPS          * The images should have at least 2 products from that Collection  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_grid_view.png#center\" /> </div>  In case a store is configured with the List View layout, collection images are generated automatically from 3 selected images of products grouped under the same collection. They will be displayed together as seen below:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/collection_image_list_view.png#center\" /> </div>   ## Supercollection Images  These are mandatory for all supercollections.    Specifications:      * Orientation: Horizontal.            * Dimensions - 2484 x 1380 px.            * Format: JPG.            * File size: below 1,5 MB      * Protocol: HTTPS.            * Must show the product in a close-up, without transparency            * They can not be photomontages or contain logos or promotional elements pasted on the image            * They can have the logo of the brand applied to commercial elements as napkins, tablecloths, etc.  They will appear in the app like this:  <div align=\"center\" class=\"img-div\">   <img alt=\"collection image\" src=\"img/supercollection_image.png#center\" /> </div>  ## Future changes  Please note that this part of the document is flux. There is the possibility of changes to some of the images specified here in the near future.  # Authentication  A static `token` to operate with our API will be provided by your AM. It's important that you keep it in a secure place. All API calls must be made over HTTPS.   The token won't be require to be changed over time, but if you think it was compromised in some way, please contact us so we can generate a new one.  <SecurityDefinitions />   # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: partner.integrationseu@glovoapp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class BulkUpdateItemsRestrictions(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'is_alcoholic': 'bool'
    }

    attribute_map = {
        'is_alcoholic': 'is_alcoholic'
    }

    def __init__(self, is_alcoholic=None):  # noqa: E501
        """BulkUpdateItemsRestrictions - a model defined in Swagger"""  # noqa: E501
        self._is_alcoholic = None
        self.discriminator = None
        if is_alcoholic is not None:
            self.is_alcoholic = is_alcoholic

    @property
    def is_alcoholic(self):
        """Gets the is_alcoholic of this BulkUpdateItemsRestrictions.  # noqa: E501

        Flag indicating if the product is an alcoholic beverage. This will trigger a compliant user flow for this restriction for stores in Poland and Romania.  # noqa: E501

        :return: The is_alcoholic of this BulkUpdateItemsRestrictions.  # noqa: E501
        :rtype: bool
        """
        return self._is_alcoholic

    @is_alcoholic.setter
    def is_alcoholic(self, is_alcoholic):
        """Sets the is_alcoholic of this BulkUpdateItemsRestrictions.

        Flag indicating if the product is an alcoholic beverage. This will trigger a compliant user flow for this restriction for stores in Poland and Romania.  # noqa: E501

        :param is_alcoholic: The is_alcoholic of this BulkUpdateItemsRestrictions.  # noqa: E501
        :type: bool
        """

        self._is_alcoholic = is_alcoholic

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(BulkUpdateItemsRestrictions, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BulkUpdateItemsRestrictions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
