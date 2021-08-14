#!/usr/bin/env python

from flask import Flask, request
from dotenv import load_dotenv

import os

load_dotenv()

MAJOR_VERSION = 0
MINOR_VERSION = 1
PATCH_VERSION = 0
VERSION = f"{MAJOR_VERSION}.{MINOR_VERSION}.{PATCH_VERSION}"

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def main():
        config = ["MDX_CONTENT_DIR"]

        config_output = "<pre>\n"
        for cfgvar in config:
            config_output += f"{cfgvar}={os.environ.get(cfgvar, None)}\n"
        config_output += "</pre>"

        return f"<pre>mdxtunnel {VERSION}</pre>\n{config_output}"

    @app.route("/content")
    def get_file():
        return str(request.args)

    return app
