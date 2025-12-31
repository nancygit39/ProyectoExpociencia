from datetime import timedelta

DEBUG = False
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'expociencia.uagrm.bo']

# --- Seguridad ---
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
SECURE_SSL_REDIRECT = False  # cambiar a True en producción

# --- Contraseñas ---
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', 'OPTIONS': {'min_length': 8}},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# --- JWT ---
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
}

# --- Axes (seguridad contra fuerza bruta) ---
INSTALLED_APPS_EXTRA = ['axes']
MIDDLEWARE_EXTRA = ['axes.middleware.AxesMiddleware']
AXES_FAILURE_LIMIT = 5
AXES_COOLOFF_TIME = 30
AXES_LOCK_OUT_PARAMETERS = ['username', 'ip_address']

# --- CORS ---
INSTALLED_APPS_CORS = ['corsheaders']
MIDDLEWARE_CORS = ['corsheaders.middleware.CorsMiddleware']
CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://expociencia.uagrm.bo"
]

# --- Logs de seguridad ---
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'security_file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'security.log',
        },
    },
    'loggers': {
        'django.security': {
            'handlers': ['security_file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
