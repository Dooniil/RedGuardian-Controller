from sqlalchemy import Column, Integer, String, JSON

from db.config import Base
from db.models.behavior_model import BehaviorModel


class Host(Base, BehaviorModel):
    __tablename__ = 'host'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=True)
    description = Column(String, nullable=True)
    ip_address = Column(String, nullable=False)
    dns_address = Column(String, nullable=True)


class Credential(Base, BehaviorModel):
    __tablename__ = 'credential'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, unique=True, nullable=False)
    description = Column(String, nullable=True)
    access_info = Column(JSON, nullable=False)
    transport_type = Column(Integer, nullable=False)
