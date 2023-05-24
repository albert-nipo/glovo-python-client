# OrderCancelled

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**order_id** | **AllOfOrderCancelledOrderId** |  | 
**store_id** | **AllOfOrderCancelledStoreId** |  | 
**cancel_reason** | **str** | Description of order cancellation reason  - &#x60;PRODUCTS_NOT_AVAILABLE&#x60;: Products are not available in store - &#x60;STORE_CAN_NOT_DELIVER&#x60;: Order could not be delivered by partner - &#x60;PARTNER_PRINTER_ISSUE&#x60;: Order cancelled due to issues with partner&#x27;s device - &#x60;USER_ERROR&#x60;: Customer has cancelled the order - &#x60;ORDER_NOT_FEASIBLE&#x60;: It is impossible to fulfill the customer&#x27;s request - &#x60;OTHER&#x60;: Other cancellation reasons that do not fall into the above categories  | 
**payment_strategy** | **str** | - &#x60;PAY_NOTHING&#x60;: Glovo will not pay the partner for the order products - &#x60;PAY_PRODUCTS&#x60;: Glovo will pay the partner for the order products  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

