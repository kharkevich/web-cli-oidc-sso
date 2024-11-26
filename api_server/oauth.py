from authlib.integrations.starlette_client import OAuth
from api_server.config import Config

oauth = OAuth()
oauth.register(
    name="oidc",
    client_id=Config.oidc_client_id,
    client_secret=Config.oidc_client_secret,
    server_metadata_url=Config.oidc_metadata_url,
    client_kwargs={"scope": Config.oidc_scopes},
)
