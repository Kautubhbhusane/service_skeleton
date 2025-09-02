# Validator package
import os
from .subscription_client import SubscriptionClient

validate = SubscriptionClient.validate

__all__ = ["validate"]