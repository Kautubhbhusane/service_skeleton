import os

# Global config (from env or defaults)
SUBSCRIPTION_API_URL = os.getenv("SUBSCRIPTION_API_URL", "http://dummy-subscription-service/validate")
