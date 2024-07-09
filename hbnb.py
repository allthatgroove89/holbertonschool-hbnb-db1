""" Flask, entry point of the app"""
from flask import Flask
from flask_migrate import Migrate
from db import db
from sqlalchemy import create_engine
from src.models import user, amenity, city, place, country
import os
from flask_jwt_extended import JWTManager
from src.routes.users import user_manager_blueprint
from src.routes.amenities import amenity_blueprint
from src.routes.countries_cities import country_city_manager_blueprint
from src.routes.places import place_manager_blueprint
from src.routes.reviews import review_manager_blueprint


"""Flask Application"""
app = Flask(__name__)

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///development.db'
    JWT_SECRET_KEY = 'super-secret'


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


environment_config = DevelopmentConfig if os.environ.get(
    'ENV') == 'development' else ProductionConfig
app.config.from_object(environment_config)

db.init_app(app)
jwt = JWTManager(app)


@app.route('/')
def index():
    return "Holberton BnB!"

app.register_blueprint(user_manager_blueprint)
app.register_blueprint(country_city_manager_blueprint)
app.register_blueprint(amenity_blueprint)
app.register_blueprint(place_manager_blueprint)
app.register_blueprint(review_manager_blueprint)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
