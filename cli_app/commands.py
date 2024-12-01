import logging

import click
import colorlogging

from cli_app.api_call import api_call
from cli_app.auth import authorize


@click.command()
@click.pass_context
def hello(ctx):
    say_hello(ctx)


def say_hello(ctx):
    response = api_call(ctx, "/api/hello")
    if response not in (None, {}):
        colorlogging.show_info(response["message"])


@click.command()
@click.pass_context
def auth(ctx):
    authorize(ctx)
    logging.info("Authorization successful")
