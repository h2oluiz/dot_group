from drf_spectacular.plumbing import build_array_type, build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.openapi import AutoSchema

from drf_spectacular.plumbing import build_array_type, build_basic_type
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.openapi import AutoSchema


def custom_postprocessing_hook(result, generator, request, public):
    """
    Hook para ajustar formatos de data no schema OpenAPI.
    """
    components = result.get("components", {})
    schemas = components.get("schemas", {})

    for schema in schemas.values():
        properties = schema.get("properties", {})
        for prop in properties.values():
            # Altera o formato de campos 'date' para DD/MM/YYYY
            if prop.get("format") == "date":
                prop["format"] = "dd/mm/yyyy"
                prop["example"] = "25/12/2025"
            # Altera o formato de campos 'date-time' se desejar
            elif prop.get("format") == "date-time":
                prop["format"] = "dd/mm/yyyy HH:MM:SS"
                prop["example"] = "25/12/2025 18:30:00"

    return result
