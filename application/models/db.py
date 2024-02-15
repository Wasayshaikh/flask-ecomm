#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base  = declarative_base()
database_uri = 'postgresql://postgres:1234@localhost/blog_post'
# database_uri = 'mysql+mysqlconnector://root:1234@localhost/blog_post'
engine = create_engine(database_uri)
def create_tables():
    Base.metadata.create_all(engine)
    pass
def database_session():
    Session = sessionmaker(bind=engine)
    return Session()


databaseSession = database_session()
