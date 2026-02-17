from .base import *  # noqa: F401, F403
from .base import config

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("DB_NAME", default="subtube"),
        "USER": config("DB_USER", default="subtube"),
        "PASSWORD": config("DB_PASSWORD", default="subtube"),
        "HOST": config("DB_HOST", default="localhost"),
        "PORT": config("DB_PORT", default="5432"),
    }
}
