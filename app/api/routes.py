from flask import Blueprint, jsonify, request
from .services.serialize_messages import serialize_users
from ..messages.models import User
from os import environ

blueprint = Blueprint('api', __name__)

@blueprint.get('/api/v1/messages')
def users():
    if environ.get('API_KEY') == request.headers.get('X-API-KEY'):
        users = User.query.all()
        return jsonify(
            serialize_users(users)     
        )
    else:
        return jsonify({'error': 'Invalid API Key'}), 401