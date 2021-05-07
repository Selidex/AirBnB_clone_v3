#!/usr/bin/python3
"""Setting up API for HBNB"""
from flask import Flask, escape, request, render_template, Blueprint
from models import storage
from api.v1.views import app_views
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.teardown_appcontext
def teardown(context):
    """ runs when app is done"""
    storage.close()


if __name__ == "__main__":
    host = getenv('HBNB_API_HOST')
    post = getenv('HBNB_API_PORT')
    if host is None:
        host = '0.0.0.0'
    if post is None:
        post = '5000'
    app.run(host=host, port=post, threaded=True)
