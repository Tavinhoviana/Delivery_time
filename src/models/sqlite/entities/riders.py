from sqlalchemy import Column, Integer, String, ForeignKey
from src.models.sqlite.settings.base import Base

class RiderTable(Base):
    __tablename__ = "riders"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hub_id = Column(Integer, ForeignKey("hubs.id"))

    def __repr__(self):
        return f"Rider(id={self.id}, name={self.name}, hub_id={self.hub_id})"
