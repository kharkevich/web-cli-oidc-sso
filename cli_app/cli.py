import logging

import click
import colorlogging

from cli_app.commands import auth, hello

logger = logging.getLogger(__name__)
colorlogging.configure(level=logging.WARNING)


@click.group()
@click.option(
    "--open-browser",
    is_flag=True,
    help="Open the browser automatically for device flow",
)
@click.option("--api-server", default="http://localhost:8000", help="API server URL")
@click.option("--token-file", default="token.json", help="Token file path")
@click.pass_context
def cli(ctx: click.Context, open_browser: bool, api_server: str, token_file: str) -> None:
    ctx.ensure_object(dict)
    ctx.obj["open_browser"] = open_browser
    ctx.obj["api_server"] = api_server
    ctx.obj["token_file"] = token_file


cli.add_command(hello)
cli.add_command(auth)

if __name__ == "__main__":
    cli(obj={})
