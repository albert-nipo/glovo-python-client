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

class Order2(object):
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
        'order_id': 'AllOfOrder2OrderId',
        'store_id': 'AllOfOrder2StoreId',
        'order_time': 'str',
        'estimated_pickup_time': 'str',
        'utc_offset_minutes': 'str',
        'payment_method': 'str',
        'currency': 'str',
        'order_code': 'str',
        'allergy_info': 'str',
        'special_requirements': 'str',
        'estimated_total_price': 'int',
        'delivery_fee': 'int',
        'minimum_basket_surcharge': 'int',
        'customer_cash_payment_amount': 'int',
        'courier': 'OrderCourier',
        'customer': 'OrderCustomer',
        'products': 'list[OrderProducts]',
        'delivery_address': 'OrderDeliveryAddress',
        'bundled_orders': 'list[str]',
        'pick_up_code': 'str',
        'is_picked_up_by_customer': 'bool',
        'cutlery_requested': 'bool',
        'partner_discounts_products': 'int',
        'partner_discounted_products_total': 'int',
        'total_customer_to_pay': 'int',
        'loyalty_card': 'str',
        'service_fee': 'int'
    }

    attribute_map = {
        'order_id': 'order_id',
        'store_id': 'store_id',
        'order_time': 'order_time',
        'estimated_pickup_time': 'estimated_pickup_time',
        'utc_offset_minutes': 'utc_offset_minutes',
        'payment_method': 'payment_method',
        'currency': 'currency',
        'order_code': 'order_code',
        'allergy_info': 'allergy_info',
        'special_requirements': 'special_requirements',
        'estimated_total_price': 'estimated_total_price',
        'delivery_fee': 'delivery_fee',
        'minimum_basket_surcharge': 'minimum_basket_surcharge',
        'customer_cash_payment_amount': 'customer_cash_payment_amount',
        'courier': 'courier',
        'customer': 'customer',
        'products': 'products',
        'delivery_address': 'delivery_address',
        'bundled_orders': 'bundled_orders',
        'pick_up_code': 'pick_up_code',
        'is_picked_up_by_customer': 'is_picked_up_by_customer',
        'cutlery_requested': 'cutlery_requested',
        'partner_discounts_products': 'partner_discounts_products',
        'partner_discounted_products_total': 'partner_discounted_products_total',
        'total_customer_to_pay': 'total_customer_to_pay',
        'loyalty_card': 'loyalty_card',
        'service_fee': 'service_fee'
    }

    def __init__(self, order_id=None, store_id=None, order_time=None, estimated_pickup_time=None, utc_offset_minutes=None, payment_method=None, currency=None, order_code=None, allergy_info=None, special_requirements=None, estimated_total_price=None, delivery_fee=None, minimum_basket_surcharge=None, customer_cash_payment_amount=None, courier=None, customer=None, products=None, delivery_address=None, bundled_orders=None, pick_up_code=None, is_picked_up_by_customer=None, cutlery_requested=None, partner_discounts_products=None, partner_discounted_products_total=None, total_customer_to_pay=None, loyalty_card=None, service_fee=None):  # noqa: E501
        """Order2 - a model defined in Swagger"""  # noqa: E501
        self._order_id = None
        self._store_id = None
        self._order_time = None
        self._estimated_pickup_time = None
        self._utc_offset_minutes = None
        self._payment_method = None
        self._currency = None
        self._order_code = None
        self._allergy_info = None
        self._special_requirements = None
        self._estimated_total_price = None
        self._delivery_fee = None
        self._minimum_basket_surcharge = None
        self._customer_cash_payment_amount = None
        self._courier = None
        self._customer = None
        self._products = None
        self._delivery_address = None
        self._bundled_orders = None
        self._pick_up_code = None
        self._is_picked_up_by_customer = None
        self._cutlery_requested = None
        self._partner_discounts_products = None
        self._partner_discounted_products_total = None
        self._total_customer_to_pay = None
        self._loyalty_card = None
        self._service_fee = None
        self.discriminator = None
        self.order_id = order_id
        self.store_id = store_id
        if order_time is not None:
            self.order_time = order_time
        if estimated_pickup_time is not None:
            self.estimated_pickup_time = estimated_pickup_time
        if utc_offset_minutes is not None:
            self.utc_offset_minutes = utc_offset_minutes
        self.payment_method = payment_method
        self.currency = currency
        self.order_code = order_code
        if allergy_info is not None:
            self.allergy_info = allergy_info
        if special_requirements is not None:
            self.special_requirements = special_requirements
        self.estimated_total_price = estimated_total_price
        if delivery_fee is not None:
            self.delivery_fee = delivery_fee
        if minimum_basket_surcharge is not None:
            self.minimum_basket_surcharge = minimum_basket_surcharge
        if customer_cash_payment_amount is not None:
            self.customer_cash_payment_amount = customer_cash_payment_amount
        self.courier = courier
        self.customer = customer
        self.products = products
        if delivery_address is not None:
            self.delivery_address = delivery_address
        self.bundled_orders = bundled_orders
        if pick_up_code is not None:
            self.pick_up_code = pick_up_code
        self.is_picked_up_by_customer = is_picked_up_by_customer
        if cutlery_requested is not None:
            self.cutlery_requested = cutlery_requested
        self.partner_discounts_products = partner_discounts_products
        self.partner_discounted_products_total = partner_discounted_products_total
        if total_customer_to_pay is not None:
            self.total_customer_to_pay = total_customer_to_pay
        if loyalty_card is not None:
            self.loyalty_card = loyalty_card
        self.service_fee = service_fee

    @property
    def order_id(self):
        """Gets the order_id of this Order2.  # noqa: E501


        :return: The order_id of this Order2.  # noqa: E501
        :rtype: AllOfOrder2OrderId
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this Order2.


        :param order_id: The order_id of this Order2.  # noqa: E501
        :type: AllOfOrder2OrderId
        """
        if order_id is None:
            raise ValueError("Invalid value for `order_id`, must not be `None`")  # noqa: E501

        self._order_id = order_id

    @property
    def store_id(self):
        """Gets the store_id of this Order2.  # noqa: E501


        :return: The store_id of this Order2.  # noqa: E501
        :rtype: AllOfOrder2StoreId
        """
        return self._store_id

    @store_id.setter
    def store_id(self, store_id):
        """Sets the store_id of this Order2.


        :param store_id: The store_id of this Order2.  # noqa: E501
        :type: AllOfOrder2StoreId
        """
        if store_id is None:
            raise ValueError("Invalid value for `store_id`, must not be `None`")  # noqa: E501

        self._store_id = store_id

    @property
    def order_time(self):
        """Gets the order_time of this Order2.  # noqa: E501

        Local time of the acceptance of the order by Glovo  # noqa: E501

        :return: The order_time of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._order_time

    @order_time.setter
    def order_time(self, order_time):
        """Sets the order_time of this Order2.

        Local time of the acceptance of the order by Glovo  # noqa: E501

        :param order_time: The order_time of this Order2.  # noqa: E501
        :type: str
        """

        self._order_time = order_time

    @property
    def estimated_pickup_time(self):
        """Gets the estimated_pickup_time of this Order2.  # noqa: E501

        Local time of courier's expected arrival at the store  # noqa: E501

        :return: The estimated_pickup_time of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._estimated_pickup_time

    @estimated_pickup_time.setter
    def estimated_pickup_time(self, estimated_pickup_time):
        """Sets the estimated_pickup_time of this Order2.

        Local time of courier's expected arrival at the store  # noqa: E501

        :param estimated_pickup_time: The estimated_pickup_time of this Order2.  # noqa: E501
        :type: str
        """

        self._estimated_pickup_time = estimated_pickup_time

    @property
    def utc_offset_minutes(self):
        """Gets the utc_offset_minutes of this Order2.  # noqa: E501

        Time difference in minutes between UTC and the local time of the store  # noqa: E501

        :return: The utc_offset_minutes of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._utc_offset_minutes

    @utc_offset_minutes.setter
    def utc_offset_minutes(self, utc_offset_minutes):
        """Sets the utc_offset_minutes of this Order2.

        Time difference in minutes between UTC and the local time of the store  # noqa: E501

        :param utc_offset_minutes: The utc_offset_minutes of this Order2.  # noqa: E501
        :type: str
        """

        self._utc_offset_minutes = utc_offset_minutes

    @property
    def payment_method(self):
        """Gets the payment_method of this Order2.  # noqa: E501

        - `CASH`: Indicates that the courier will pay for the order with cash  - `DELAYED`: Indicates that Glovo will pay for the order by an invoice sent to the partner   # noqa: E501

        :return: The payment_method of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this Order2.

        - `CASH`: Indicates that the courier will pay for the order with cash  - `DELAYED`: Indicates that Glovo will pay for the order by an invoice sent to the partner   # noqa: E501

        :param payment_method: The payment_method of this Order2.  # noqa: E501
        :type: str
        """
        if payment_method is None:
            raise ValueError("Invalid value for `payment_method`, must not be `None`")  # noqa: E501
        allowed_values = ["CASH", "DELAYED"]  # noqa: E501
        if payment_method not in allowed_values:
            raise ValueError(
                "Invalid value for `payment_method` ({0}), must be one of {1}"  # noqa: E501
                .format(payment_method, allowed_values)
            )

        self._payment_method = payment_method

    @property
    def currency(self):
        """Gets the currency of this Order2.  # noqa: E501

        Currency code of the order  # noqa: E501

        :return: The currency of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Order2.

        Currency code of the order  # noqa: E501

        :param currency: The currency of this Order2.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501

        self._currency = currency

    @property
    def order_code(self):
        """Gets the order_code of this Order2.  # noqa: E501

        Alphanumeric identifier of the order used for historical identification or by Glovo support  # noqa: E501

        :return: The order_code of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._order_code

    @order_code.setter
    def order_code(self, order_code):
        """Sets the order_code of this Order2.

        Alphanumeric identifier of the order used for historical identification or by Glovo support  # noqa: E501

        :param order_code: The order_code of this Order2.  # noqa: E501
        :type: str
        """
        if order_code is None:
            raise ValueError("Invalid value for `order_code`, must not be `None`")  # noqa: E501

        self._order_code = order_code

    @property
    def allergy_info(self):
        """Gets the allergy_info of this Order2.  # noqa: E501

        Customer provided details of their allergies  # noqa: E501

        :return: The allergy_info of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._allergy_info

    @allergy_info.setter
    def allergy_info(self, allergy_info):
        """Sets the allergy_info of this Order2.

        Customer provided details of their allergies  # noqa: E501

        :param allergy_info: The allergy_info of this Order2.  # noqa: E501
        :type: str
        """

        self._allergy_info = allergy_info

    @property
    def special_requirements(self):
        """Gets the special_requirements of this Order2.  # noqa: E501

        Customer provided details of special requirements for the order (In case the store has this feature enabled, otherwise it will be null)  # noqa: E501

        :return: The special_requirements of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._special_requirements

    @special_requirements.setter
    def special_requirements(self, special_requirements):
        """Sets the special_requirements of this Order2.

        Customer provided details of special requirements for the order (In case the store has this feature enabled, otherwise it will be null)  # noqa: E501

        :param special_requirements: The special_requirements of this Order2.  # noqa: E501
        :type: str
        """

        self._special_requirements = special_requirements

    @property
    def estimated_total_price(self):
        """Gets the estimated_total_price of this Order2.  # noqa: E501

        Estimated total price of products and attributes in the order denominated in cents and excluding the delivery fee  # noqa: E501

        :return: The estimated_total_price of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._estimated_total_price

    @estimated_total_price.setter
    def estimated_total_price(self, estimated_total_price):
        """Sets the estimated_total_price of this Order2.

        Estimated total price of products and attributes in the order denominated in cents and excluding the delivery fee  # noqa: E501

        :param estimated_total_price: The estimated_total_price of this Order2.  # noqa: E501
        :type: int
        """
        if estimated_total_price is None:
            raise ValueError("Invalid value for `estimated_total_price`, must not be `None`")  # noqa: E501

        self._estimated_total_price = estimated_total_price

    @property
    def delivery_fee(self):
        """Gets the delivery_fee of this Order2.  # noqa: E501

        Delivery price of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be `null`   # noqa: E501

        :return: The delivery_fee of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._delivery_fee

    @delivery_fee.setter
    def delivery_fee(self, delivery_fee):
        """Sets the delivery_fee of this Order2.

        Delivery price of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be `null`   # noqa: E501

        :param delivery_fee: The delivery_fee of this Order2.  # noqa: E501
        :type: int
        """

        self._delivery_fee = delivery_fee

    @property
    def minimum_basket_surcharge(self):
        """Gets the minimum_basket_surcharge of this Order2.  # noqa: E501

        The minimum basket surcharge in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be `null`   # noqa: E501

        :return: The minimum_basket_surcharge of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._minimum_basket_surcharge

    @minimum_basket_surcharge.setter
    def minimum_basket_surcharge(self, minimum_basket_surcharge):
        """Sets the minimum_basket_surcharge of this Order2.

        The minimum basket surcharge in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be `null`   # noqa: E501

        :param minimum_basket_surcharge: The minimum_basket_surcharge of this Order2.  # noqa: E501
        :type: int
        """

        self._minimum_basket_surcharge = minimum_basket_surcharge

    @property
    def customer_cash_payment_amount(self):
        """Gets the customer_cash_payment_amount of this Order2.  # noqa: E501

        The total amount the customer will pay as cash. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo or if this value is not informed by the customer, this will be set to `null`   # noqa: E501

        :return: The customer_cash_payment_amount of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._customer_cash_payment_amount

    @customer_cash_payment_amount.setter
    def customer_cash_payment_amount(self, customer_cash_payment_amount):
        """Sets the customer_cash_payment_amount of this Order2.

        The total amount the customer will pay as cash. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo or if this value is not informed by the customer, this will be set to `null`   # noqa: E501

        :param customer_cash_payment_amount: The customer_cash_payment_amount of this Order2.  # noqa: E501
        :type: int
        """

        self._customer_cash_payment_amount = customer_cash_payment_amount

    @property
    def courier(self):
        """Gets the courier of this Order2.  # noqa: E501


        :return: The courier of this Order2.  # noqa: E501
        :rtype: OrderCourier
        """
        return self._courier

    @courier.setter
    def courier(self, courier):
        """Sets the courier of this Order2.


        :param courier: The courier of this Order2.  # noqa: E501
        :type: OrderCourier
        """
        if courier is None:
            raise ValueError("Invalid value for `courier`, must not be `None`")  # noqa: E501

        self._courier = courier

    @property
    def customer(self):
        """Gets the customer of this Order2.  # noqa: E501


        :return: The customer of this Order2.  # noqa: E501
        :rtype: OrderCustomer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this Order2.


        :param customer: The customer of this Order2.  # noqa: E501
        :type: OrderCustomer
        """
        if customer is None:
            raise ValueError("Invalid value for `customer`, must not be `None`")  # noqa: E501

        self._customer = customer

    @property
    def products(self):
        """Gets the products of this Order2.  # noqa: E501

        List of order products  # noqa: E501

        :return: The products of this Order2.  # noqa: E501
        :rtype: list[OrderProducts]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this Order2.

        List of order products  # noqa: E501

        :param products: The products of this Order2.  # noqa: E501
        :type: list[OrderProducts]
        """
        if products is None:
            raise ValueError("Invalid value for `products`, must not be `None`")  # noqa: E501

        self._products = products

    @property
    def delivery_address(self):
        """Gets the delivery_address of this Order2.  # noqa: E501


        :return: The delivery_address of this Order2.  # noqa: E501
        :rtype: OrderDeliveryAddress
        """
        return self._delivery_address

    @delivery_address.setter
    def delivery_address(self, delivery_address):
        """Sets the delivery_address of this Order2.


        :param delivery_address: The delivery_address of this Order2.  # noqa: E501
        :type: OrderDeliveryAddress
        """

        self._delivery_address = delivery_address

    @property
    def bundled_orders(self):
        """Gets the bundled_orders of this Order2.  # noqa: E501

        Bundled orders are those that are to be delivered together by a single courier. Relevant to Glovo orders only.  For [marketplace orders](#section/Getting-started/Marketplace-orders) this will be set to `null`   # noqa: E501

        :return: The bundled_orders of this Order2.  # noqa: E501
        :rtype: list[str]
        """
        return self._bundled_orders

    @bundled_orders.setter
    def bundled_orders(self, bundled_orders):
        """Sets the bundled_orders of this Order2.

        Bundled orders are those that are to be delivered together by a single courier. Relevant to Glovo orders only.  For [marketplace orders](#section/Getting-started/Marketplace-orders) this will be set to `null`   # noqa: E501

        :param bundled_orders: The bundled_orders of this Order2.  # noqa: E501
        :type: list[str]
        """
        if bundled_orders is None:
            raise ValueError("Invalid value for `bundled_orders`, must not be `None`")  # noqa: E501

        self._bundled_orders = bundled_orders

    @property
    def pick_up_code(self):
        """Gets the pick_up_code of this Order2.  # noqa: E501

        Non-sequential, non-unique 3 digit numerical code used to identify an order for pickup by the courier or customer  # noqa: E501

        :return: The pick_up_code of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._pick_up_code

    @pick_up_code.setter
    def pick_up_code(self, pick_up_code):
        """Sets the pick_up_code of this Order2.

        Non-sequential, non-unique 3 digit numerical code used to identify an order for pickup by the courier or customer  # noqa: E501

        :param pick_up_code: The pick_up_code of this Order2.  # noqa: E501
        :type: str
        """

        self._pick_up_code = pick_up_code

    @property
    def is_picked_up_by_customer(self):
        """Gets the is_picked_up_by_customer of this Order2.  # noqa: E501

        Indicates that the order will be picked up by a customer instead of by a courier  # noqa: E501

        :return: The is_picked_up_by_customer of this Order2.  # noqa: E501
        :rtype: bool
        """
        return self._is_picked_up_by_customer

    @is_picked_up_by_customer.setter
    def is_picked_up_by_customer(self, is_picked_up_by_customer):
        """Sets the is_picked_up_by_customer of this Order2.

        Indicates that the order will be picked up by a customer instead of by a courier  # noqa: E501

        :param is_picked_up_by_customer: The is_picked_up_by_customer of this Order2.  # noqa: E501
        :type: bool
        """
        if is_picked_up_by_customer is None:
            raise ValueError("Invalid value for `is_picked_up_by_customer`, must not be `None`")  # noqa: E501

        self._is_picked_up_by_customer = is_picked_up_by_customer

    @property
    def cutlery_requested(self):
        """Gets the cutlery_requested of this Order2.  # noqa: E501

        Indicates that the customer requested cutlery for the order  # noqa: E501

        :return: The cutlery_requested of this Order2.  # noqa: E501
        :rtype: bool
        """
        return self._cutlery_requested

    @cutlery_requested.setter
    def cutlery_requested(self, cutlery_requested):
        """Sets the cutlery_requested of this Order2.

        Indicates that the customer requested cutlery for the order  # noqa: E501

        :param cutlery_requested: The cutlery_requested of this Order2.  # noqa: E501
        :type: bool
        """

        self._cutlery_requested = cutlery_requested

    @property
    def partner_discounts_products(self):
        """Gets the partner_discounts_products of this Order2.  # noqa: E501

        Total value in cents of partner-funded promotional discounts applied to products  # noqa: E501

        :return: The partner_discounts_products of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._partner_discounts_products

    @partner_discounts_products.setter
    def partner_discounts_products(self, partner_discounts_products):
        """Sets the partner_discounts_products of this Order2.

        Total value in cents of partner-funded promotional discounts applied to products  # noqa: E501

        :param partner_discounts_products: The partner_discounts_products of this Order2.  # noqa: E501
        :type: int
        """
        if partner_discounts_products is None:
            raise ValueError("Invalid value for `partner_discounts_products`, must not be `None`")  # noqa: E501

        self._partner_discounts_products = partner_discounts_products

    @property
    def partner_discounted_products_total(self):
        """Gets the partner_discounted_products_total of this Order2.  # noqa: E501

        Total value in cents of products after partner-funded promotional discounts have been applied  # noqa: E501

        :return: The partner_discounted_products_total of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._partner_discounted_products_total

    @partner_discounted_products_total.setter
    def partner_discounted_products_total(self, partner_discounted_products_total):
        """Sets the partner_discounted_products_total of this Order2.

        Total value in cents of products after partner-funded promotional discounts have been applied  # noqa: E501

        :param partner_discounted_products_total: The partner_discounted_products_total of this Order2.  # noqa: E501
        :type: int
        """
        if partner_discounted_products_total is None:
            raise ValueError("Invalid value for `partner_discounted_products_total`, must not be `None`")  # noqa: E501

        self._partner_discounted_products_total = partner_discounted_products_total

    @property
    def total_customer_to_pay(self):
        """Gets the total_customer_to_pay of this Order2.  # noqa: E501

        The final amount to be paid in cents by customer after discounts, promotions, surcharges, fees and other adjustments have been calculated.  Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be set to `null`   # noqa: E501

        :return: The total_customer_to_pay of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._total_customer_to_pay

    @total_customer_to_pay.setter
    def total_customer_to_pay(self, total_customer_to_pay):
        """Sets the total_customer_to_pay of this Order2.

        The final amount to be paid in cents by customer after discounts, promotions, surcharges, fees and other adjustments have been calculated.  Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be set to `null`   # noqa: E501

        :param total_customer_to_pay: The total_customer_to_pay of this Order2.  # noqa: E501
        :type: int
        """

        self._total_customer_to_pay = total_customer_to_pay

    @property
    def loyalty_card(self):
        """Gets the loyalty_card of this Order2.  # noqa: E501

        Optional customer-provided store loyalty code. If the value is present, the Partner can choose to apply the corresponding rewards or discounts for the order to the identified loyalty customer.  If the value is not provided by the customer this will be set to `null`   # noqa: E501

        :return: The loyalty_card of this Order2.  # noqa: E501
        :rtype: str
        """
        return self._loyalty_card

    @loyalty_card.setter
    def loyalty_card(self, loyalty_card):
        """Sets the loyalty_card of this Order2.

        Optional customer-provided store loyalty code. If the value is present, the Partner can choose to apply the corresponding rewards or discounts for the order to the identified loyalty customer.  If the value is not provided by the customer this will be set to `null`   # noqa: E501

        :param loyalty_card: The loyalty_card of this Order2.  # noqa: E501
        :type: str
        """

        self._loyalty_card = loyalty_card

    @property
    def service_fee(self):
        """Gets the service_fee of this Order2.  # noqa: E501

        Service fee of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If there is no service fee determined by Glovo, this field will be `null`   # noqa: E501

        :return: The service_fee of this Order2.  # noqa: E501
        :rtype: int
        """
        return self._service_fee

    @service_fee.setter
    def service_fee(self, service_fee):
        """Sets the service_fee of this Order2.

        Service fee of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If there is no service fee determined by Glovo, this field will be `null`   # noqa: E501

        :param service_fee: The service_fee of this Order2.  # noqa: E501
        :type: int
        """
        if service_fee is None:
            raise ValueError("Invalid value for `service_fee`, must not be `None`")  # noqa: E501

        self._service_fee = service_fee

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
        if issubclass(Order2, dict):
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
        if not isinstance(other, Order2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
