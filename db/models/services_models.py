from sqlalchemy import Column, Integer, String

from db.config import Base
from db.models.behavior_model import BehaviorModel


class Scanner(Base, BehaviorModel):
    __tablename__ = 'scan_service'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    connection_address = Column(String, unique=True, nullable=False)