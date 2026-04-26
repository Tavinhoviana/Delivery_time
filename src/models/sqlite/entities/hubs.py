from sqlalchemy import Column, Integer, String
from src.models.sqlite.settings.base import Base

class HubTable(Base):
    __tablename__ = "hubs"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return f"Hub(id={self.id}, name={self.name}, city={self.city})"
