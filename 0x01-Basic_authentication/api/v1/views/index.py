#!/usr/bin/env python3
""" Module of Index views
"""
from flask import jsonify, abort
from api.v1.views import app_views
from models.user import User


# Define the route for GET /api/v1/unauthorized
@app_views.route('/unauthorized', methods=['GET'])
def unauthorized():
    # Raise a 401 error
    abort(401)


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status() -> str:
    """ GET /api/v1/status
    Return:
      - the status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/', strict_slashes=False)
def stats() -> str:
    """ GET /api/v1/stats
    Return:
      - the number of each objects
    """
    stats = {}
    stats['users'] = User.count()
    return jsonify(stats)
