"""
This module contains the routes for the amenities blueprint
"""
from src.persistence.datamanager import DataManager
from db import db
from flask import Blueprint, request, jsonify, abort
from flask_jwt_extended import (
    create_access_token, jwt_required,
    get_jwt_identity, verify_jwt_in_request
    )
from functools import wraps
from src.models.user import User
from src.models.amenity import Amenity
from flask import Blueprint
from src.controllers.amenities import (
    create_amenity,
    delete_amenity,
    get_amenity_by_id,
    get_amenities,
    update_amenity,
)

amenity_blueprint = Blueprint('amenity_manager', __name__)
data_manager = DataManager()


@amenity_blueprint.route('/amenities', methods=['POST'])
@jwt_required()
def create_amenity():
    user = User.query.get(get_jwt_identity())
    if not user.is_admin:
        abort(403, description="Admin rights required")

    if not request.json or 'name' not in request.json:
        abort(400, description="Missing required fields")

    name = request.json['name']

    existing_amenities = Amenity.query.filter_by(name=name).first()

    if existing_amenities:
        abort(409, description="Amenity name already exists")

    amenity = Amenity(
        name=name
    )
    db.session.add(amenity)
    db.session.commit()
    return jsonify(amenity.to_dict()), 201


@amenity_blueprint.route('/amenities', methods=['GET'])
def get_amenities():
    amenities = Amenity.query.all()
    return jsonify([amenities.to_dict() for amenities in amenities]), 200


@amenity_blueprint.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404, description="Amenity not found")
    return jsonify(amenity.to_dict()), 200


@amenity_blueprint.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    amenity = Amenity.query.get(amenity_id)
    if not amenity:
        abort(404, description="Amenity not found")

    if not request.json:
        abort(400, description="Missing required fields")

    new_name = request.json.get('name')
    if new_name and new_name != amenity.name:
        existing_amenity = Amenity.query.filter(
            Amenity.name == new_name, Amenity.id != amenity_id).first()
        if existing_amenity:
            abort(409, description="Amenity name already exists")
        amenity.name = new_name

    db.session.commit()
    return jsonify(amenity.to_dict()), 200


@ amenity_blueprint.route('/amenities/<amenity_id>', methods=['DELETE'])
@ jwt_required()
def delete_amenity(amenity_id):
    user = User.query.get(get_jwt_identity())
    if not user.is_admin:
        abort(403, description="Admin rights required")
    amenity = Amenity.query.get(amenity_id)
    db.session.delete(amenity)
    db.session.commit()
    return '', 204
