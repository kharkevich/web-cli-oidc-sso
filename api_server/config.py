import os

from dotenv import load_dotenv

load_dotenv()


class Config:
    oidc_issuer = os.getenv("OIDC_ISSUER")
    oidc_client_id = os.getenv("OIDC_CLIENT_ID")
    oidc_client_secret = os.getenv("OIDC_CLIENT_SECRET")
    oidc_metadata_url = f"{oidc_issuer}/.well-known/openid-configuration"
    oidc_scopes = os.getenv("OIDC_SCOPES", "openid email groups profile")
    oidc_allowed_groups = list(os.getenv("OIDC_ALLOWED_GROUPS", "mlflow-users").split(","))
    oidc_cache_ttl = os.getenv("OIDC_CACHE_TTL", 3600)
    device_code_ttl = os.getenv("DEVICE_CODE_TTL", 300)


    redis_host = os.getenv("REDIS_HOST", "localhost")
    redis_port = os.getenv("REDIS_PORT", 6379)
    redis_password = os.getenv("REDIS_PASSWORD", None)
    redis_db = os.getenv("REDIS_DB", 9)
    redis_url = f"redis://{redis_host}:{redis_port}/{redis_db}"

    session_secret = os.getenv("SESSION_SECRET", "your-secret-key")

    cors_enabled = bool(os.getenv("CORS_ENABLED", False))
    cors_allow_origins = list(os.getenv("CORS_ALLOW_ORIGINS", "*").split(","))
    cors_allow_credentials = True
    cors_allow_methods = list(os.getenv("CORS_ALLOW_METHODS", "*").split(","))
    cors_allow_headers = list(os.getenv("CORS_ALLOW_HEADERS", "*").split(","))
