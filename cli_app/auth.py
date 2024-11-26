import json
import logging
import os
import time
import webbrowser

import colorlogging
import httpx


def start_device_flow(ctx):
    api_server = ctx.obj["api_server"]
    response = httpx.get(f"{api_server}/auth/device/code")
    response.raise_for_status()
    data = response.json()
    verification_uri_complete = (
        f"{data['verification_uri']}?exchange_code={data['exchange_code']}"
    )
    colorlogging.show_info(f"Visit {verification_uri_complete} to continue", important=True)
    if ctx.obj["open_browser"]:
        webbrowser.open(verification_uri_complete)
    return data["exchange_code"], data["expires_in"]


def wait_for_token(ctx, exchange_code, expires_in):
    api_server = ctx.obj["api_server"]
    start_time = time.time()
    while time.time() - start_time < expires_in:
        response = httpx.post(
            f"{api_server}/auth/device/token",
            json={"exchange_code": exchange_code},
            timeout=10.0,
        )
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 202:
            logging.info(response.json()["message"])
            time.sleep(5)
        else:
            raise ValueError(f"Error: {response.status_code} - {response.text}")
    raise TimeoutError("Authorization timed out")


def authorize(ctx):
    token_file = ctx.obj["token_file"]
    exchange_code, expires_in = start_device_flow(ctx)
    token_data = wait_for_token(ctx, exchange_code, expires_in)
    with open(token_file, "w") as f:
        json.dump(token_data, f)
    return token_data["jwt"]


def get_token(ctx):
    token_file = ctx.obj["token_file"]
    if os.path.exists(token_file):
        with open(token_file, "r") as f:
            token_data = json.load(f)
            return token_data["jwt"]
    return authorize(ctx)
