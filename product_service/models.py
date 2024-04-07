# product_service/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(255))
    price = Column(Integer)

    def __repr__(self):
        return f"<Product(name='{self.name}')>"
