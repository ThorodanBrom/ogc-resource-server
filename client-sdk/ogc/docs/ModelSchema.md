# ModelSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ref** | **str** |  | 
**title** | **str** |  | [optional] 
**multiple_of** | **float** |  | [optional] 
**maximum** | **float** |  | [optional] 
**exclusive_maximum** | **bool** |  | [optional] [default to False]
**minimum** | **float** |  | [optional] 
**exclusive_minimum** | **bool** |  | [optional] [default to False]
**max_length** | **int** |  | [optional] 
**min_length** | **int** |  | [optional] [default to 0]
**pattern** | **str** |  | [optional] 
**max_items** | **int** |  | [optional] 
**min_items** | **int** |  | [optional] [default to 0]
**unique_items** | **bool** |  | [optional] [default to False]
**max_properties** | **int** |  | [optional] 
**min_properties** | **int** |  | [optional] [default to 0]
**required** | **List[str]** |  | [optional] 
**enum** | **List[object]** |  | [optional] 
**type** | **str** |  | [optional] 
**var_not** | [**SchemaOneOfNot**](SchemaOneOfNot.md) |  | [optional] 
**all_of** | [**List[SchemaOneOfNot]**](SchemaOneOfNot.md) |  | [optional] 
**one_of** | [**List[SchemaOneOfNot]**](SchemaOneOfNot.md) |  | [optional] 
**any_of** | [**List[SchemaOneOfNot]**](SchemaOneOfNot.md) |  | [optional] 
**items** | [**SchemaOneOfNot**](SchemaOneOfNot.md) |  | [optional] 
**properties** | [**Dict[str, SchemaOneOfNot]**](SchemaOneOfNot.md) |  | [optional] 
**additional_properties** | [**SchemaOneOfAdditionalProperties**](SchemaOneOfAdditionalProperties.md) |  | [optional] 
**description** | **str** |  | [optional] 
**format** | **str** |  | [optional] 
**default** | **object** |  | [optional] 
**nullable** | **bool** |  | [optional] [default to False]
**read_only** | **bool** |  | [optional] [default to False]
**write_only** | **bool** |  | [optional] [default to False]
**example** | **object** |  | [optional] 
**deprecated** | **bool** |  | [optional] [default to False]
**content_media_type** | **str** |  | [optional] 
**content_encoding** | **str** |  | [optional] 
**content_schema** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.model_schema import ModelSchema

# TODO update the JSON string below
json = "{}"
# create an instance of ModelSchema from a JSON string
model_schema_instance = ModelSchema.from_json(json)
# print the JSON string representation of the object
print(ModelSchema.to_json())

# convert the object into a dict
model_schema_dict = model_schema_instance.to_dict()
# create an instance of ModelSchema from a dict
model_schema_from_dict = ModelSchema.from_dict(model_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


