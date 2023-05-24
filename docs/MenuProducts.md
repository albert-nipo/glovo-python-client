# MenuProducts

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier of the product within a store | 
**name** | **str** | Product name | 
**price** | **float** | Product price | 
**image_url** | **str** | Url of the main product image. Must use HTTPS protocol. | [optional] 
**extra_image_urls** | **list[str]** | Array of urls of product extra images. Must use HTTPS protocol.  They will be displayed in the product detail page in the same order as in the array, and always after the main image. Support up to 9 images (if more images are sent, the first 9 will be processed).  | [optional] 
**restrictions** | [**MenuRestrictions**](MenuRestrictions.md) |  | [optional] 
**description** | **str** | Product description | [optional] 
**attributes_groups** | **list[str]** | List of attribute group unique identifiers that would be part of the product. Attribute groups will be displayed in the order of the list. | [optional] 
**available** | **bool** | Specifies if the product is available to be purchased | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

