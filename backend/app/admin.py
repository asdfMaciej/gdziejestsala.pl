import secrets
import models
import flask, flask_login, flask_admin
from wtforms import form, fields, validators
from database import SessionLocal
from werkzeug.security import generate_password_hash, check_password_hash

from flask import Flask
from flask_admin import Admin
from flask_admin import helpers
from flask_admin.contrib.sqla import ModelView


def get_user_by_login(login):
    return SessionLocal().query(models.User).filter(models.User.login == login).first()


class AuthModelView(ModelView):
    def is_accessible(self):
        return flask_login.current_user.is_authenticated


class AuthIndexView(flask_admin.AdminIndexView):
    @flask_admin.expose("/")
    def index(self):
        if not flask_login.current_user.is_authenticated:
            return flask.redirect(flask.url_for(".login"))
        return super(AuthIndexView, self).index()

    @flask_admin.expose("/login", methods=["GET", "POST"])
    def login(self):
        if flask.request.method == "GET":
            if flask_login.current_user.is_authenticated:
                return flask.redirect(flask.url_for(".index"))

            return """
            <form action='login' method='POST'>
                <input type='text' name='login' id='login' placeholder='login'>
                <input type='password' name='password' id='password' placeholder='password'>
                <input type='submit' name='submit'>
            </form>
            """

        login, password = flask.request.form["login"], flask.request.form["password"]
        user = get_user_by_login(login)
        print(user)
        if user and check_password_hash(pwhash=user.password, password=password):
            flask_login.login_user(user)

        if flask_login.current_user.is_authenticated:
            return flask.redirect(flask.url_for(".index"))

        return "Bad login"

    @flask_admin.expose("/logout")
    def logout(self):
        flask_login.logout_user()
        return flask.redirect(flask.url_for(".index"))


# Include an admin panel for CRUD operations
flask_app = Flask(__name__)
flask_app.secret_key = secrets.token_hex(16)


login_manager = flask_login.LoginManager()

# Create user loader function
@login_manager.user_loader
def load_user(user_id):
    return SessionLocal().query(models.User).filter(models.User.id == user_id).first()


login_manager.init_app(flask_app)

flask_admin = Admin(
    flask_app, name="USOS", index_view=AuthIndexView(url=""), template_mode="bootstrap4"
)
flask_admin.add_view(AuthModelView(models.Point, SessionLocal()))
flask_admin.add_view(AuthModelView(models.Edge, SessionLocal()))
flask_admin.add_view(AuthModelView(models.Image, SessionLocal()))
flask_admin.add_view(AuthModelView(models.Floor, SessionLocal()))
flask_admin.add_view(AuthModelView(models.FloorPoint, SessionLocal()))
