import os


# Import variables from the environment and wraps them into Config class
class Config:
    SECRET_KEY = os.environ["SECRET_KEY"]

    CORS_SUPPORT_CREDENTIALS = True  # Must be true to permit cookie in request handler
    CORS_ALLOW_ORIGIN = os.environ['CORS_ALLOW_ORIGIN']  # Who can make requests
