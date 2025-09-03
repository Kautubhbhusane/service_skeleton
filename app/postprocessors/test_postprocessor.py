def test_postprocessor(response: dict) -> dict:
    response["test-postprocessor"] = "applied"
    return response