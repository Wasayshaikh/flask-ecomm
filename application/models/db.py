#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base  = declarative_base()

def create_session(db_uri):
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()

database_uri = 'postgresql://postgres:1234@localhost/blog_post'
session = create_session(database_uri)
