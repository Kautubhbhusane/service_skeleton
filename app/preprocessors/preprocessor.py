
def enrich_payload(payload):
    payload["service_name"] = "document_generation"
    print("Preprocessor 1: enrich_payload executed", payload)
    return payload

def normalize_fields(payload):
    payload["role"] = "admin"
    print("Preprocessor 2: normalize_fields executed", payload)
    return payload
      
