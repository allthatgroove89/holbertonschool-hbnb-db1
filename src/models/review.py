"""
Review related functionality
"""

from sqlalchemy.sql import func
from db import db

class Review(db.Model):
    """Review representation"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'), nullable=False)
    user_id = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(120), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    created_at = db.Column(db.DateTime, default=func.now())
    updated_at = db.Column(db.DateTime, default=func.now, onupdate=func.now)
    # Relationships Def


    def __repr__(self) -> str:
        """Review repr"""
        return f"<Review {self.id} - '{self.comment[:25]}...'>"

    def to_dict(self) -> dict:
        """Dictionary representation of the object"""
        return {
            "id": self.id,
            "place_id": self.place_id,
            "user_id": self.user_id,
            "comment": self.comment,
            "rating": self.rating,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
        }

    @classmethod
    def create(cls, data: dict) -> "Review":
        """Create a new review"""
        new_review = cls(
            name=data.get("name"),
            place_id=data("place_id"),
            user_id=data("user_id"),
            comment=data("comment"),
            rating=data("rating")
        )
        db.session.add(new_review)
        db.session.commit
        return new_review

    @classmethod
    def get(cls, review_id) -> "Review | None":
        """Retreives Review"""
        return cls.query.get(review_id)

    @classmethod
    def get_all(cls) -> list:
        """Retrieves all Reviews by list"""
        return cls.query.all()

    @classmethod
    def update(cls, review_id: str, data: dict) -> "Review | None":
        """Update an existing review"""
        review = cls.query.get(review_id)
        if not review:
            raise ValueError("Review not found")

        for key, value in data.item():
            if hasattr(review, key):
                setattr(review, key, value)
        db.session.commit()
        return review

    @classmethod
    def delete(cls,review_id:str) -> bool:
        """Deletes existing review"""
        review = cls.query.get(review_id)

        if not review:
            raise ValueError("Review not found")
        db.session.delete(review)
        db.session.commit()
        return True
