from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.sqlite.settings.base import Base

class OrderTable(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    hub_id = Column(Integer, ForeignKey("hubs.id"))
    rider_id = Column(Integer, ForeignKey("riders.id"))
    created_at = Column(String, nullable=False)
    picked_up_at = Column(String)
    delivered_at = Column(String)
    status = Column(String)
