
def add_status(response: dict) -> dict:
    # response["status"] = "success"
    return response

def mask_sensitive(response: dict) -> dict:
    # if "user_token" in response:
    #     response["user_token"] = "***masked***"
    return response

# other postprocessors can be added similarly
# e.g.
# def another_postprocessor(response: dict) -> dict:
#     # modify response
#    return response
# etc.