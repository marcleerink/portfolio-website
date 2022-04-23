from flask import Blueprint, jsonify, request
from .services.serialize_messages import serialize_users
from ..messages.models import User
import os
import requests
from requests.auth import HTTPBasicAuth

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/messages')
def users():
    API_KEY = os.getenv('API_KEY')
    users = User.query.all()
    return jsonify(serialize_users(users))

@blueprint.get('/planet')
def planet():
    PLANET_API_KEY = os.getenv('PLANET_API_KEY')
    BASE_URL =  'https://tiles0.planet.com/basemaps/v1/planet-tiles/global_monthly_2016_05_mosaic/gmap/0/0/0.png'
    
    auth = HTTPBasicAuth(PLANET_API_KEY, '')
    res = requests.get(url=BASE_URL, auth=auth)

    return (res.text)

