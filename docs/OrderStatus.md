# OrderStatus

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Use the following information to understand when to send each status:  - &#x60;ACCEPTED&#x60;: The order has been accepted by the store. Be aware that if you don&#x27;t accept the order we will still move forward with the order, as we don&#x27;t require an acceptance to proceed. - &#x60;READY_FOR_PICKUP&#x60;: The order is ready to be picked up by a courier or the customer (Only available for orders delivered by Glovo couriers) - &#x60;OUT_FOR_DELIVERY&#x60;: The courier has collected the order in the store and is now being delivered to the customer (Only available for [Marketplace orders](#section/Getting-started/Marketplace-orders)) - &#x60;PICKED_UP_BY_CUSTOMER&#x60;: The order has been picked up by the customer (Only available for orders to be picked up by the customer)  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

