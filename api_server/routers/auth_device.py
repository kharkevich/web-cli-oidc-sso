import uuid
from typing import Optional

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from api_server.cache import redis_client
from api_server.config import Config
from api_server.oauth import oauth

router = APIRouter(
    prefix="/auth/device",
    tags=["auth", "device"],
    responses={404: {"description": "Not found"}},
)


@router.get("/code")
async def device_code(request: Request):
    exchange_code = str(uuid.uuid4())
    redis_client.hset(exchange_code, "status", "initiated")
    redis_client.expire(exchange_code, Config.device_code_ttl)
    return JSONResponse(
        content={
            "exchange_code": exchange_code,
            "expires_in": Config.device_code_ttl,
            "verification_uri": f"{str(request.base_url).rstrip('/')}{router.url_path_for('verify')}",
        }
    )


@router.get("/verify")
async def verify(request: Request, exchange_code: Optional[str] = None):
    if not exchange_code:
        raise HTTPException(status_code=400, detail="Exchange code is required")
    redirect_uri = await oauth.oidc.authorize_redirect(
        request,
        redirect_uri=f"{str(request.base_url).rstrip('/')}{router.url_path_for('callback')}",
        state=exchange_code,
    )
    return redirect_uri


@router.get("/callback")
async def callback(request: Request):
    try:
        token = await oauth.oidc.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    id_token = token.get("id_token")
    state = request.query_params.get("state")
    try:
        uuid.UUID(state)
        if redis_client.exists(state):
            redis_client.expire(state, Config.device_code_ttl)
            redis_client.hset(state, "jwt", id_token)
            redis_client.hset(state, "status", "authorized")
            return JSONResponse(
                content={
                    "message": "Authorization successful. You can close this window."
                }
            )
        return HTTPException(
            status_code=400, content={"message": "Invalid or expired exchange code."}
        )
    except ValueError:
        return HTTPException(
            status_code=500, content={"message": "Internal server error"}
        )


class TokenRequest(BaseModel):
    exchange_code: str


@router.post("/token")
async def token(token_request: TokenRequest):
    exchange_code = token_request.exchange_code
    if not exchange_code:
        raise HTTPException(status_code=400, detail="Exchange code is required")
    data = redis_client.hgetall(exchange_code)
    if not data:
        raise HTTPException(status_code=400, detail="Invalid exchange code")
    if data.get("status") == "authorized":
        jwt = data.get("jwt")
        return JSONResponse(content={"jwt": jwt})
    return JSONResponse(status_code=202, content={"message": "Authorization pending"})
