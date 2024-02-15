from .db import Base
from sqlalchemy import Column, BigInteger, Integer, String,Text,ForeignKey
from sqlalchemy.orm import relationship
class Products(Base):
    __tablename__ = "products"
    id= Column(Integer,primary_key=True, autoincrement=True )
    product_code = Column(String(100), unique=True)
    slug= Column(String(100), nullable=False, unique=True)
    user_id= Column(BigInteger, ForeignKey("users.id"), nullable=True)
    price= Column(BigInteger, nullable=False)
    is_active= Column(BigInteger, default=0)
    stocks= Column(BigInteger, nullable=True)
    out_of_stock = Column(BigInteger, default=0)
    product_metadata = relationship("ProductMetaData", uselist=False, back_populates="product", cascade="all, delete-orphan")
    users = relationship("Users", back_populates='products', cascade="save-update", passive_deletes=True)

    
