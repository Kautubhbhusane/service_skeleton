from app.processors.registry import register_postprocessor

@register_postprocessor
def add_status(response: dict) -> dict:
    # response["status"] = "success"
    return response


@register_postprocessor
def mask_sensitive(response: dict) -> dict:
    # if "user_token" in response:
    #     response["user_token"] = "***masked***"
    return response

# other postprocessors can be added similarly
# just by defining and decorating with @register_postprocessor
# they will be auto picked by the decorator
# e.g.
# @register_postprocessor
# def another_postprocessor(response: dict) -> dict:
#     # modify response
#    return response
# etc.