import logging

import httpx

from cli_app.auth import get_token, authorize


def api_call(ctx, endpoint, method="GET", body=None):
    api_server = ctx.obj["api_server"]
    token = get_token(ctx)
    headers = {"Authorization": f"Bearer {token}"}

    if method == "GET":
        response = httpx.get(f"{api_server}{endpoint}", headers=headers)
    elif method == "POST":
        response = httpx.post(f"{api_server}{endpoint}", headers=headers, json=body)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

    if response.status_code == 200:
        return response.json()
    elif response.status_code == 401:
        logging.warning("Token expired or invalid. Re-authorizing...")
        token = authorize(ctx)
        return api_call(ctx, endpoint, method, body)
    else:
        raise ValueError(f"Error: {response.status_code} - {response.text}")
