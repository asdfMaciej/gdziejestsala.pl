"""Add default admin user

Revision ID: e1f4434a2f3c
Revises: 4b3f1f39bce1
Create Date: 2022-12-26 21:12:21.799518

"""
from alembic import op
from os import getenv
import sqlalchemy as sa
from werkzeug.security import generate_password_hash

# revision identifiers, used by Alembic.
revision = "e1f4434a2f3c"
down_revision = "4b3f1f39bce1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    username = getenv("ADMIN_USERNAME")
    password = getenv("ADMIN_PASSWORD")
    email = getenv("ADMIN_EMAIL")

    if not username or not password or not email:
        print("Unable to create default admin account")
        return

    hashed_password = generate_password_hash(password)
    insert_query = """INSERT INTO users
    (first_name, last_name, login, email, password)
    VALUES
    ('Administrator', 'The Great', %s, %s, %s)"""

    connection = op.get_bind()
    connection.execute(
        insert_query,
        (
            username,
            email,
            hashed_password,
        ),
    )
    print("Created default admin account")


def downgrade() -> None:
    pass
