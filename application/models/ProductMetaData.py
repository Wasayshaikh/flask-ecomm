from .db import Base
from sqlalchemy import Column, BigInteger, Integer, String,Text, ForeignKey
from sqlalchemy.orm import relationship
class ProductMetaData(Base):
    __tablename__ = "product_metadata"
    id= Column(Integer,primary_key=True, autoincrement=True )
    product_id = Column(Integer, ForeignKey("products.id"), unique=True)
    title=Column(String(100), nullable=False)
    thumbnail = Column(Text, nullable=False)
    images = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    product = relationship("Products", back_populates="product_metadata")
