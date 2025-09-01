from app.processors.registry import register_preprocessor

@register_preprocessor
def enrich_payload(payload):
    # Example: add service name
    # payload["service_name"] = "document_generation"
    # payload["service_name"] = "example_service"
    # print("Preprocessor: enrich_payload executed ->", payload)
    print("Preprocessor 1: enrich_payload executed")
    return payload


@register_preprocessor
def normalize_fields(payload):
    # Example: ensure certain fields exist
    # payload.setdefault("metadata", {})
    print("Preprocessor 2: normalize_fields executed")
    return payload

# other preprocessors can be added similarly 
# just by defining and decorating with @register_preprocessor
# they will be auto picked by the decorator
#
# e.g.
# @register_preprocessor
# def another_preprocessor(payload: dict) -> dict:
#     # modify payload
#    return payload
# etc. 