# order_service/models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    status = Column(String(50))

    def __repr__(self):
        return f"<Order(user_id={self.user_id}, product_id={self.product_id}, status={self.status})>"
