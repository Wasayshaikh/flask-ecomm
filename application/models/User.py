from application.models.db import Base
from sqlalchemy import Column,String, Integer,BigInteger




class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(120),nullable=True)
    first_name= Column(String(50), nullable=True)
    last_name = Column(String(50), nullable=True)
    role= Column(BigInteger, nullable=False, default=0 )