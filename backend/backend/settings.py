"""
🎯 Django settings for backend project
👉 These settings control how your Django project behaves
"""

from dotenv import load_dotenv  # 📦 Load .env file for environment variables
import dj_database_url          # 🛠️ Easy database config using a single URL
from pathlib import Path
import os

# 🔐 Load environment variables (from .env file)
load_dotenv()
# 📌 Tip: You can also use `decouple` instead of `dotenv` for env management

# 📁 Define base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent

# 🚨 Security Settings
# 🔑 Secret key used for cryptographic signing — keep it safe in production!
SECRET_KEY = str(os.getenv("SECRET_KEY", "your-default-secret-key"))

# 🐞 Debug mode: Should be False in production
DEBUG = os.getenv("DEBUG", "TRUE").upper() == "TRUE"

# 🌍 Allowed domains/IPs that can access the server
ALLOWED_HOSTS = ["*"]  # ⚠️ In production, use specific domain/IP

# 🚀 Installed Django & Third-Party Apps
INSTALLED_APPS = [
    'baton',  # 🛠️ Admin theme
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",             # 🧰 Django REST Framework
    "rest_framework.authtoken",   # 🔐 Token-based authentication
    "corsheaders",                # 🌐 CORS for frontend-backend connection
    # 🧩 Custom Apps
    "authentication",
    "checkout",
    "customize",
    "feedback",
    "reviews",
    "store",
    "payments",
    "baton.autodiscover",         # ⚙️ Automatically load baton configs
]

# 🧱 Middleware — runs on every request/response
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # ✅ Enable CORS
]

# 🌐 Root URL configuration
ROOT_URLCONF = "backend.urls"

# 🔑 Django Authentication backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

# 🎨 Templates (HTML rendering)
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],  # 🛠️ You can add custom template folders here
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# 🔌 WSGI entry point for deployment (used by Gunicorn, etc.)
WSGI_APPLICATION = "backend.wsgi.application"

# 🗃️ Database Configuration
DATABASES = {
    "default": dj_database_url.parse(
        os.getenv("DB_URL", "sqlite:///db.sqlite3")  # ✅ Default: SQLite
    )
}

# 🔒 Password validation rules
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ⚙️ Django REST Framework configuration
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",  # 🔓 You can change to IsAuthenticated
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
        # "rest_framework.authentication.SessionAuthentication",  # Optional for session login
    ],
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
}

# 🌍 CORS configuration to allow frontend (like React/Vue) to connect
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

# 🌐 Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# 🧾 Static files (CSS, JS, images)
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# 💳 Stripe Payment Integration
STRIPE_SECRET_KEY = str(os.getenv("STRIPE_SECRET_KEY", ""))

# 📧 Email configuration (for sending order confirmations etc.)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = str(os.getenv("EMAIL_HOST_USER", ""))
EMAIL_HOST_PASSWORD = str(os.getenv("EMAIL_HOST_PASSWORD", ""))
EMAIL_RECIEVER = str(os.getenv("EMAIL_RECIEVER", ""))  # 👥 Receiver of order mails

# 💰 CCAvenue Payment Gateway settings
MERCHANT_ID = str(os.getenv("MERCHANT_ID", ""))
ACCESS_CODE = str(os.getenv("ACCESS_CODE", ""))
WORKING_KEY = str(os.getenv("WORKING_KEY", ""))

# 💳 Razorpay settings
ROZERPAY_KEY_ID = str(os.getenv("ROZERPAY_KEY_ID", ""))
ROZERPAY_KEY_SECRET = str(os.getenv("ROZERPAY_KEY_SECRET", ""))

# 🆔 Default primary key type for models
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# 🔐 Google OAuth (for social login or Google APIs)
# 🔐 Google OAuth (used for social login, Google APIs, etc.)
# ✅ Credentials are now loaded securely from environment variables

GOOGLE_CLIENT_ID = str(os.getenv("GOOGLE_CLIENT_ID", "your-default-google-client-id"))
SOCIAL_SECRET = str(os.getenv("SOCIAL_SECRET", "your-default-social-secret"))
