from models import Base
from sqlalchemy import Column, BigInteger, Integer, String,Text
class Products(Base):
    id= Column(Integer(30),primary_key=True, autoincrement=True )
    title=Column(String(100), nullable=False)
    slug= Column(String(100), nullable=False)
    user_id= Column(BigInteger, nullable=True)
    
