from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    "postgresql+psycopg2://flask_db_user:1234@127.0.0.1:5431/hw_flask"
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

app = Flask(__name__)
