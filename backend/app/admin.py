import secrets, models
from database import SessionLocal

from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


# Include an admin panel for CRUD operations
flask_app = Flask(__name__)
flask_app.secret_key = secrets.token_hex(16)

flask_admin = Admin(flask_app, name="USOS", template_mode="bootstrap4", url="")
flask_admin.add_view(ModelView(models.Point, SessionLocal()))
flask_admin.add_view(ModelView(models.Edge, SessionLocal()))
flask_admin.add_view(ModelView(models.Image, SessionLocal()))
flask_admin.add_view(ModelView(models.Floor, SessionLocal()))
flask_admin.add_view(ModelView(models.FloorPoint, SessionLocal()))
