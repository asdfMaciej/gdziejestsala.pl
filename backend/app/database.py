from sqlalchemy import create_engine, event
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from os import getenv

SQLALCHEMY_DATABASE_URL = getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)

"""
SQLite3 setup:

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# SQLite3 doesn't enforce foreign keys by default
def _fk_pragma_on_connect(dbapi_con, con_record):
    dbapi_con.execute("pragma foreign_keys=ON")

event.listen(engine, "connect", _fk_pragma_on_connect)
"""

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# This function is required to provide an unique, auto-closed connection per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
