from sqlalchemy import Column, Integer, String, ForeignKey

from db.config import Base


# class Family(Base):
#     __tablename__ = 'family'
#
#     id = Column(Integer, primary_key=True)
#     name = Column(String, nullable=False)
#

class Vulnerability(Base):
    __tablename__ = 'vulnerability'

    id = Column(Integer, primary_key=True)
    cve_id = Column(String, nullable=False)
    description = Column(String, nullable=False)
    # family_id = Column(Integer, ForeignKey('family.id'), nullable=False)
    # severity = Column(Integer, nullable=False)
    cmd = Column(String, nullable=False)
    cmd_res = Column(String, nullable=False)
