"""
Place related functionality
"""
from src.models.base import BaseModel
from typing import List
from db import db

class Place(BaseModel):
    """Place representation"""
    name = db.Column(db.String(128), nullable=False)
    description = db.Column(db.String(1024), nullable=True)
    address = db.Column(db.String(128), nullable=False)
    city_id = db.Column(db.String(60), db.ForeignKey(
        'city.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=True)
    longitude = db.Column(db.Float, nullable=True)
    host_id = db.Column(db.String(60), db.ForeignKey(
        'user.id'), nullable=False)
    number_of_rooms = db.Column(db.Integer, default=0)
    number_of_bathrooms = db.Column(db.Integer, default=0)
    max_guests = db.Column(db.Integer, default=0)
    price_per_night = db.Column(db.Integer, default=0)
    amenity_ids = []


    def __repr__(self) -> str:
        """Place repr"""
        return f"<Place {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "city_id": self.city_id,
            "host_id": self.host_id,
            "price_per_night": self.price_per_night,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "max_guests": self.max_guests,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
