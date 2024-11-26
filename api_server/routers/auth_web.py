from typing import Optional

from authlib.integrations.starlette_client import OAuth
from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel

from api_server.cache import redis_client
from api_server.config import Config

from api_server.oauth import oauth

router = APIRouter(
    prefix="/auth/web",
    tags=["auth", "web"],
    responses={404: {"description": "Not found"}},
)

@router.get("/login")
async def login(request: Request, redirect_uri: str):
    redirect_uri = await oauth.oidc.authorize_redirect(
        request,
        redirect_uri=redirect_uri,
    )
    return redirect_uri

@router.get("/callback")
async def callback(request: Request, code: Optional[str] = None, state: Optional[str] = None):
    try:
        token = await oauth.oidc.authorize_access_token(request)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    id_token = token.get("id_token")
    return JSONResponse(
        content={
            "jwt": id_token,
        }
    )
