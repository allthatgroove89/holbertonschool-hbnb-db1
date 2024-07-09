"""
Country related functionality
"""


from flask_sqlalchemy import SQLAlchemy
from typing import List
from repository import db


class Country(db.Model):
    """
    Country representation

    This class does NOT inherit from Base, you can't delete or update a country

    This class is used to get and list countries
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    code = db.Column(db.String(2), unique=True)
    cities = db.relationship('City', back_populates='country', lazy=True)

    def __repr__(self) -> str:
        """Country representation"""
        return f"<Country {self.code} ({self.name})>"

    def to_dict(self) -> dict:
        """Returns the dictionary representation of the country"""
        return {
            "name": self.name,
            "code": self.code,
            "cities": [city.name for city in self.cities] if self.cities else []
        }
    @classmethod
    def create(cls, name: str, code: str) -> "Country":
        """Create a new country"""
        new_country = cls(name=name, code=code)
        db.session.add(new_country)
        db.session.commit()
        return new_country

    @classmethod
    def get_all(cls) -> List["Country"]:
        """Get all countries"""
        return cls.query.all()

    @classmethod
    def get(cls, code: str) -> "Country | None":
        """Get a country by its code"""
        return cls.query.filter_by(code=code).first()

    @classmethod
    def update(cls, code: str, **kw) -> bool:
        """Update a country by its code with provided keyword arguments."""
        country_to_update = cls.query.filter_by(code=code).first()
        if country_to_update:
            for key, value in kw.item():
                if hasattr(country_to_update, key):
                    setattr(country_to_update, key, value)
            db.session.commit()
            return True
        return False

    @classmethod
    def delete(cls, code:str) -> bool:
        """Delete a country by its code."""
        country_to_delete = cls.query.filter_by(code=code).first()
        if country_to_delete:
            db.session.delete(country_to_delete)
            db.session.commit()
            return True
        return False
