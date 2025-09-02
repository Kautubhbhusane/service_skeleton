def add_timestamp(payload):
    from datetime import datetime
    payload["timestamp"] = datetime.utcnow().isoformat()
    print("new pre processor testign  3: add_timestamp executed", payload)
    return payload