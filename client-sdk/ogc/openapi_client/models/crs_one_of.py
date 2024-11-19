# coding: utf-8

"""
    OGC Compliant DX Resource Server

    OGC compliant Features and Common API definitions. Includes Schema and Response Objects.   <a href='/stac/api'>STAC API Documentation</a>    <a href='/metering/api'>DX Metering API Documentation</a>

    The version of the OpenAPI document: 1.0.1
    Contact: info@iudx.org.in
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.crs_one_of_one_of import CrsOneOfOneOf
from openapi_client.models.crs_one_of_one_of1 import CrsOneOfOneOf1
from openapi_client.models.crs_one_of_one_of2 import CrsOneOfOneOf2
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

CRSONEOF_ONE_OF_SCHEMAS = ["CrsOneOfOneOf", "CrsOneOfOneOf1", "CrsOneOfOneOf2"]

class CrsOneOf(BaseModel):
    """
    CrsOneOf
    """
    # data type: CrsOneOfOneOf
    oneof_schema_1_validator: Optional[CrsOneOfOneOf] = None
    # data type: CrsOneOfOneOf1
    oneof_schema_2_validator: Optional[CrsOneOfOneOf1] = None
    # data type: CrsOneOfOneOf2
    oneof_schema_3_validator: Optional[CrsOneOfOneOf2] = None
    actual_instance: Optional[Union[CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2]] = None
    one_of_schemas: Set[str] = { "CrsOneOfOneOf", "CrsOneOfOneOf1", "CrsOneOfOneOf2" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = CrsOneOf.model_construct()
        error_messages = []
        match = 0
        # validate data type: CrsOneOfOneOf
        if not isinstance(v, CrsOneOfOneOf):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CrsOneOfOneOf`")
        else:
            match += 1
        # validate data type: CrsOneOfOneOf1
        if not isinstance(v, CrsOneOfOneOf1):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CrsOneOfOneOf1`")
        else:
            match += 1
        # validate data type: CrsOneOfOneOf2
        if not isinstance(v, CrsOneOfOneOf2):
            error_messages.append(f"Error! Input type `{type(v)}` is not `CrsOneOfOneOf2`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in CrsOneOf with oneOf schemas: CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in CrsOneOf with oneOf schemas: CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into CrsOneOfOneOf
        try:
            instance.actual_instance = CrsOneOfOneOf.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CrsOneOfOneOf1
        try:
            instance.actual_instance = CrsOneOfOneOf1.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into CrsOneOfOneOf2
        try:
            instance.actual_instance = CrsOneOfOneOf2.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CrsOneOf with oneOf schemas: CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CrsOneOf with oneOf schemas: CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], CrsOneOfOneOf, CrsOneOfOneOf1, CrsOneOfOneOf2]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


