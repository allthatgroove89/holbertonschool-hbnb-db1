from src.models import ORMBase  # Import the BaseModel from where your models are defined
from src.persistence import db

# Create the database tables
db.create_all()
print("Database tables created successfully.")