# OrderProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the product within a store | 
**purchased_product_id** | **str** | Unique identifier of every individual selection of a (potentially customized) product within the order. This identifier is necessary to perform order modifications over the products purchased.  | 
**quantity** | **int** | Product quantity | 
**price** | **int** | Product unit price (without attributes) in cents | 
**name** | **str** | Product name | 
**attributes** | [**list[OrderAttributes]**](OrderAttributes.md) | Attributes associated with the given product | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

