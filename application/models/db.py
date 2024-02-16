#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from application.helper import env
# Access the environment variables
database_uri = ''
database_port = ""
database_password=""
DATABASE_ENG = env("DATABASE_ENG")
database_url = env("DATABASE_URL")
database_user = env("DATABASE_USER")
password = env("DATABASE_PASSWORD")
database = env("DATABASE")
port =  env("DATABASE_PORT")

if port != "":
    database_port =  ":"+port
if password != "":
    database_password = ":"+password



if DATABASE_ENG == "postgre":
    database_uri = f"postgresql://{database_user}{database_password}@{database_url}{database_port}/{database}"
elif DATABASE_ENG == "mysql":
    database_uri = f"mysql+mysqlconnector://{database_user}{database_password}@{database_url}{database_port}/{database}"
elif DATABASE_ENG == "sqlite":
    database_uri = f"sqlite:///{database}"

Base  = declarative_base()
engine = create_engine(database_uri)
def create_tables():
    Base.metadata.create_all(engine)
    pass
def database_session():
    Session = sessionmaker(bind=engine)
    return Session()


databaseSession = database_session()
