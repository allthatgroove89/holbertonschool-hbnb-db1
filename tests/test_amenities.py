
from flask_testing import TestCase
from hbnb import create_app
from db import db
from src.models.place import Place
from src.controllers import places
from src.routes import places
class TestPlaceOperations(TestCase):
    def create_app(self):
        # Return a Flask instance configured for testing
        app = create_app()
        return app

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_place(self):
        response = self.client.post("/places", json={"name": "Test Place", "description": "A test place"})
        self.assertEqual(response.status_code, 201)
        self.assertIn("Test Place", response.json['name'])

# Additional tests would follow a similar structure