"""
Amenity Model
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy
from db import db

class Amenity(db.Model):
    """Amenity representation"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    #places = db.relationship('PlaceAmenity', back_populates='amenity')
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def __init__(self, name: str, **kw) -> None:
        """init"""
        super().__init__(**kw)
        self.name = name

    def __repr__(self) -> str:
        """String represetation of Amenity"""
        return f"<Amenity {self.id} ({self.name})>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }
