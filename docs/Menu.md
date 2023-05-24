# Menu

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**list[MenuAttributes]**](MenuAttributes.md) | A product can be customized in different ways e.g. add mayonnaise, bundle it with a drink, or add extra meat.  Each of these customizations is considered an attribute. It is not mandatory for a product to have attributes.  Each attribute can have a different price impact. Similar attributes are grouped into attribute groups.  | [optional] 
**attribute_groups** | [**list[MenuAttributeGroups]**](MenuAttributeGroups.md) | Attribute groups allow to group similar customizations into generic groups. Each attribute group can have a minimum and maximum of choices for the customer. Examples of attribute groups could include: - Sauces: a group of attributes such as mayo, mustard or tomato sauce - Drinks: a group of attributes such as water, coke, or lemonade  | [optional] 
**products** | [**list[MenuProducts]**](MenuProducts.md) | A product is the main component of a Glovo menu. It usually represents a physical product in a store, although we give stores flexibility to configure what they want to offer as products. Each product belongs in a section.  | [optional] 
**collections** | [**list[MenuCollections]**](MenuCollections.md) | A collection is the main categorization of a Glovo menu. It is mandatory to have at least one collection in your menu. It is composed by sections and it must have at least one to contain other elements.  Some examples of collections include: Drinks, Burgers, Salads, Desserts, Pasta.  | [optional] 
**supercollections** | [**list[MenuSupercollections]**](MenuSupercollections.md) | A super collection is the uppermost categorization of a Glovo menu. Super collections are not required. If at least one exists, a list of all the super collections is displayed to customers when they open a store in the app. Otherwise, the collection is displayed as the uppermost categorization.  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

