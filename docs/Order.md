# Order

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **AllOfOrderOrderId** |  | 
**store_id** | **AllOfOrderStoreId** |  | 
**order_time** | **str** | Local time of the acceptance of the order by Glovo | [optional] 
**estimated_pickup_time** | **str** | Local time of courier&#x27;s expected arrival at the store | [optional] 
**utc_offset_minutes** | **str** | Time difference in minutes between UTC and the local time of the store | [optional] 
**payment_method** | **str** | - &#x60;CASH&#x60;: Indicates that the courier will pay for the order with cash  - &#x60;DELAYED&#x60;: Indicates that Glovo will pay for the order by an invoice sent to the partner  | 
**currency** | **str** | Currency code of the order | 
**order_code** | **str** | Alphanumeric identifier of the order used for historical identification or by Glovo support | 
**allergy_info** | **str** | Customer provided details of their allergies | [optional] 
**special_requirements** | **str** | Customer provided details of special requirements for the order (In case the store has this feature enabled, otherwise it will be null) | [optional] 
**estimated_total_price** | **int** | Estimated total price of products and attributes in the order denominated in cents and excluding the delivery fee | 
**delivery_fee** | **int** | Delivery price of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be &#x60;null&#x60;  | [optional] 
**minimum_basket_surcharge** | **int** | The minimum basket surcharge in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be &#x60;null&#x60;  | [optional] 
**customer_cash_payment_amount** | **int** | The total amount the customer will pay as cash. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo or if this value is not informed by the customer, this will be set to &#x60;null&#x60;  | [optional] 
**courier** | [**OrderCourier**](OrderCourier.md) |  | 
**customer** | [**OrderCustomer**](OrderCustomer.md) |  | 
**products** | [**list[OrderProducts]**](OrderProducts.md) | List of order products | 
**delivery_address** | [**OrderDeliveryAddress**](OrderDeliveryAddress.md) |  | [optional] 
**bundled_orders** | **list[str]** | Bundled orders are those that are to be delivered together by a single courier. Relevant to Glovo orders only.  For [marketplace orders](#section/Getting-started/Marketplace-orders) this will be set to &#x60;null&#x60;  | 
**pick_up_code** | **str** | Non-sequential, non-unique 3 digit numerical code used to identify an order for pickup by the courier or customer | [optional] 
**is_picked_up_by_customer** | **bool** | Indicates that the order will be picked up by a customer instead of by a courier | 
**cutlery_requested** | **bool** | Indicates that the customer requested cutlery for the order | [optional] 
**partner_discounts_products** | **int** | Total value in cents of partner-funded promotional discounts applied to products | 
**partner_discounted_products_total** | **int** | Total value in cents of products after partner-funded promotional discounts have been applied | 
**total_customer_to_pay** | **int** | The final amount to be paid in cents by customer after discounts, promotions, surcharges, fees and other adjustments have been calculated.  Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If the order is delivered by Glovo this will be set to &#x60;null&#x60;  | [optional] 
**loyalty_card** | **str** | Optional customer-provided store loyalty code. If the value is present, the Partner can choose to apply the corresponding rewards or discounts for the order to the identified loyalty customer.  If the value is not provided by the customer this will be set to &#x60;null&#x60;  | [optional] 
**service_fee** | **int** | Service fee of the order in cents. Relevant to [marketplace orders](#section/Getting-started/Marketplace-orders) only.  If there is no service fee determined by Glovo, this field will be &#x60;null&#x60;  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

