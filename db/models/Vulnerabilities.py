from sqlalchemy import Column, Integer, String, JSON, ForeignKey

from db.config import Base


class Family(Base):
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Platform(Base):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True)
    family_id = Column(Integer, ForeignKey('family.id'), nullable=False)
    name = Column(String, nullable=False)


class Vulnerability(Base):
    __tablename__ = 'vulnerability'

    id = Column(Integer, primary_key=True)
    cve_id = Column(String, nullable=False)
    description = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    cmd_86 = Column(JSON, nullable=False)
    cmd_64 = Column(JSON, nullable=True)
    platform_id = Column(Integer, ForeignKey('platform.id'), nullable=False)
    versions = Column(JSON, nullable=True)
