from flask import url_for, current_app, jsonify
from . import users_blueprint
from user.instance import db


@users_blueprint.route('/')
def index():
    return jsonify({'status': 'Ok'})
