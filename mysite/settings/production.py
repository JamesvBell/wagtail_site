from .base import *

DEBUG = False

import os, dj_database_url   # pip install dj-database-url

ALLOWED_HOSTS = [
    "your-render-service.onrender.com",   # Render URL
    "www.yourdomain.com",                 # custom domain
]

# read DATABASE_URL that Render injects
DATABASES = {
    "default": dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# WhiteNoise: serve static files without Nginx
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)
STATIC_ROOT = BASE_DIR / "staticfiles"    # usually already in base.py
# ---- new lines end here ---------------------------------------


try:
    from .local import *
except ImportError:
    pass
