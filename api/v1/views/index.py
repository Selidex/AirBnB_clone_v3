#!/usr/bin/python3
""" Still no clue what I am doing here"""
from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """Returns Status:OK"""
    return jsonify({'status' : 'OK'})
