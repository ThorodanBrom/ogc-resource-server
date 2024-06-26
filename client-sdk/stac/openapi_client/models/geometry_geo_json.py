# coding: utf-8

"""
    OGC Compliant IUDX Resource Server

    OGC compliant Features and Common API definitions. Includes Schema and Response Objects.

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
from openapi_client.models.linestring_geo_json import LinestringGeoJSON
from openapi_client.models.multilinestring_geo_json import MultilinestringGeoJSON
from openapi_client.models.multipoint_geo_json import MultipointGeoJSON
from openapi_client.models.multipolygon_geo_json import MultipolygonGeoJSON
from openapi_client.models.point_geo_json import PointGeoJSON
from openapi_client.models.polygon_geo_json import PolygonGeoJSON
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GEOMETRYGEOJSON_ONE_OF_SCHEMAS = ["GeometrycollectionGeoJSON", "LinestringGeoJSON", "MultilinestringGeoJSON", "MultipointGeoJSON", "MultipolygonGeoJSON", "PointGeoJSON", "PolygonGeoJSON"]

class GeometryGeoJSON(BaseModel):
    """
    GeometryGeoJSON
    """
    # data type: PointGeoJSON
    oneof_schema_1_validator: Optional[PointGeoJSON] = None
    # data type: MultipointGeoJSON
    oneof_schema_2_validator: Optional[MultipointGeoJSON] = None
    # data type: LinestringGeoJSON
    oneof_schema_3_validator: Optional[LinestringGeoJSON] = None
    # data type: MultilinestringGeoJSON
    oneof_schema_4_validator: Optional[MultilinestringGeoJSON] = None
    # data type: PolygonGeoJSON
    oneof_schema_5_validator: Optional[PolygonGeoJSON] = None
    # data type: MultipolygonGeoJSON
    oneof_schema_6_validator: Optional[MultipolygonGeoJSON] = None
    # data type: GeometrycollectionGeoJSON
    oneof_schema_7_validator: Optional[GeometrycollectionGeoJSON] = None
    actual_instance: Optional[Union[GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON]] = None
    one_of_schemas: Set[str] = { "GeometrycollectionGeoJSON", "LinestringGeoJSON", "MultilinestringGeoJSON", "MultipointGeoJSON", "MultipolygonGeoJSON", "PointGeoJSON", "PolygonGeoJSON" }

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
        instance = GeometryGeoJSON.model_construct()
        error_messages = []
        match = 0
        # validate data type: PointGeoJSON
        if not isinstance(v, PointGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PointGeoJSON`")
        else:
            match += 1
        # validate data type: MultipointGeoJSON
        if not isinstance(v, MultipointGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MultipointGeoJSON`")
        else:
            match += 1
        # validate data type: LinestringGeoJSON
        if not isinstance(v, LinestringGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `LinestringGeoJSON`")
        else:
            match += 1
        # validate data type: MultilinestringGeoJSON
        if not isinstance(v, MultilinestringGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MultilinestringGeoJSON`")
        else:
            match += 1
        # validate data type: PolygonGeoJSON
        if not isinstance(v, PolygonGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `PolygonGeoJSON`")
        else:
            match += 1
        # validate data type: MultipolygonGeoJSON
        if not isinstance(v, MultipolygonGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `MultipolygonGeoJSON`")
        else:
            match += 1
        # validate data type: GeometrycollectionGeoJSON
        if not isinstance(v, GeometrycollectionGeoJSON):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeometrycollectionGeoJSON`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GeometryGeoJSON with oneOf schemas: GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GeometryGeoJSON with oneOf schemas: GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON. Details: " + ", ".join(error_messages))
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

        # deserialize data into PointGeoJSON
        try:
            instance.actual_instance = PointGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MultipointGeoJSON
        try:
            instance.actual_instance = MultipointGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into LinestringGeoJSON
        try:
            instance.actual_instance = LinestringGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MultilinestringGeoJSON
        try:
            instance.actual_instance = MultilinestringGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into PolygonGeoJSON
        try:
            instance.actual_instance = PolygonGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into MultipolygonGeoJSON
        try:
            instance.actual_instance = MultipolygonGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeometrycollectionGeoJSON
        try:
            instance.actual_instance = GeometrycollectionGeoJSON.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GeometryGeoJSON with oneOf schemas: GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GeometryGeoJSON with oneOf schemas: GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON. Details: " + ", ".join(error_messages))
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

    def to_dict(self) -> Optional[Union[Dict[str, Any], GeometrycollectionGeoJSON, LinestringGeoJSON, MultilinestringGeoJSON, MultipointGeoJSON, MultipolygonGeoJSON, PointGeoJSON, PolygonGeoJSON]]:
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

from openapi_client.models.geometrycollection_geo_json import GeometrycollectionGeoJSON
# TODO: Rewrite to not use raise_errors
GeometryGeoJSON.model_rebuild(raise_errors=False)

