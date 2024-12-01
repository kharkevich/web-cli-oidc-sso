import json
import logging

import httpx
from authlib.jose import jwt
from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from api_server.cache import redis_client
from api_server.config import Config

logger = logging.getLogger("uvicorn.error")


async def get_public_key():
    jwks = redis_client.get("jwks")
    if jwks:
        return jwks
    async with httpx.AsyncClient() as client:
        response = await client.get(Config.oidc_metadata_url)
        if response.status_code != 200:
            raise HTTPException(
                status_code=500, detail="Could not fetch OpenID configuration"
            )
        config = response.json()
        jwks_uri = config.get("jwks_uri")
        jwks_response = await client.get(jwks_uri)
        if jwks_response.status_code != 200:
            raise HTTPException(status_code=500, detail="Could not fetch JWKS")
        jwks = jwks_response.json()
        redis_client.set("jwks", json.dumps(jwks), ex=Config.device_code_ttl)
        return jwks


async def get_jwk_key(token: str):
    try:
        jwks = await get_public_key()
        payload = jwt.decode(token, jwks)
        payload.validate()
        return payload
    except Exception as e:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token",
        )


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class AccessValidatorMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            token = await oauth2_scheme(request)
            user = await get_jwk_key(token)
            if not any(
                group in user.get("groups", []) for group in Config.oidc_allowed_groups
            ):
                logger.error(f"User: {user.get('name')}")
                raise HTTPException(
                    status_code=403,
                    detail="User does not have access to this resource",
                )
            logger.info(f"User: {user.get('name')}")
            response = await call_next(request)
            return response
        except HTTPException as e:
            return JSONResponse(
                status_code=e.status_code,
                content={"message": e.detail},
            )
        except Exception as e:
            raise Exception(e)
