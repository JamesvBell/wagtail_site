from .base import *
DEBUG = False

import os, dj_database_url
from pathlib import Path               # NEW
# Read the secret key from the Render environment
SECRET_KEY = os.environ.get("SECRET_KEY")

# Convert BASE_DIR to a Path if base.py left it as a string

if isinstance(BASE_DIR, str):     # new
    BASE_DIR = Path(BASE_DIR)     # new




# ---> Static files ---------------------------------------------
STATIC_ROOT = BASE_DIR / "staticfiles"         # now works (Path / str)
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")
STATICFILES_STORAGE = (
    "whitenoise.storage.CompressedManifestStaticFilesStorage"
)
# ---------------------------------------------------------------

# ---> Database -------------------------------------------------
DATABASES = {
    "default": dj_database_url.config(
        default="postgres://*",        # ignored once DATABASE_URL appears
        conn_max_age=600,
        ssl_require=True,
    )
}
# ---------------------------------------------------------------
ALLOWED_HOSTS = [
    "wagtail-site.onrender.com",
    "www.stumptownfin.com"
]

RENDER_HOST = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
if RENDER_HOST:
    ALLOWED_HOSTS.append(RENDER_HOST)
try:
    from .local import *
except ImportError:
    pass

