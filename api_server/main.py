from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
from fastapi.middleware.cors import CORSMiddleware

from api_server.config import Config
from api_server.routers import api, auth_device, auth_web
from api_server.middleware.access_validator import AccessValidatorMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key=Config.session_secret)
if Config.cors_enabled:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=Config.cors_allow_origins,
        allow_credentials=Config.cors_allow_credentials,
        allow_methods=Config.cors_allow_methods,
        allow_headers=Config.cors_allow_headers,
    )

app.include_router(auth_device.router)
app.include_router(auth_web.router)
# Create a sub-application for the /api router
app_api = FastAPI()
app_api.add_middleware(AccessValidatorMiddleware)
app_api.include_router(api.router)
app.mount("/", app_api)
