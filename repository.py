from src.persistence.repository import Repository
from typing import Optional, Any
from db import db

class DBRepository(Repository):
    def get_all(self, model_name: str) -> list:
        model = globals().get(model_name)
        if model:
            return model.query.all()
        return []

    def get(self, model_name: str, obj_id: str) -> Optional[Any]:
        model = globals().get(model_name)
        if model:
            return model.query.get(obj_id)

    def save(self, obj: Any) -> None:
        db.session.add(obj)
        db.session.commit()

    def update(self, obj: Any) -> Optional[Any]:
        db.session.commit()
        return obj

    def delete(self, obj: Any) -> bool:
        db.session.delete(obj)
        db.session.commit()
        return False
