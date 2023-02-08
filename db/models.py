from sqlalchemy import Column, Integer, String, JSON, ForeignKey, select, delete, Table
from sqlalchemy.orm import relationship

from db.config import Base
from db.database import async_db_session



class BehaviorModel:
    @classmethod
    async def create(cls, **kwargs):
        instance = cls(**kwargs)
        async_db_session.add(instance)

        try:
            await async_db_session.commit()
        except Exception:
            await async_db_session.rollback()
            raise
        return instance

    @classmethod
    async def get(cls, pk):
        stmt = select(cls).where(cls.id == pk)
        result = await async_db_session.execute(stmt)
        return result.first()

    @classmethod
    async def get_all(cls):
        stmt = select(cls)
        instances = await async_db_session.execute(stmt).all()
        return instances

    @classmethod
    async def delete(cls, pk):
        stmt = delete(cls).where(cls.id == pk)
        await async_db_session.execute(stmt)
        try:
            await async_db_session.commit()
        except Exception:
            await async_db_session.rollback()
            raise


class Family(Base, BehaviorModel):
    __tablename__ = 'family'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)
    platforms = relationship('Platform')

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}('
            f'id={self.id}, '
            f'name={self.name}, '
            f')>'
        )


platform_vulnerability = Table(
    'platform_vulnerability', Base.metadata,
    Column('platform_id', Integer, ForeignKey("platform.id")),
    Column('vulnerability_id', Integer, ForeignKey("vulnerability.id"))
)


class Platform(Base, BehaviorModel):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True, autoincrement=True)
    family_id = Column(Integer, ForeignKey('family.id'))
    name = Column(String, nullable=False, unique=True)
    vulnerabilities = relationship('Vulnerability', secondary=platform_vulnerability, backref='platforms')

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}('
            f'id={self.id}, '
            f'family={self.family_id}, '
            f'name={self.name}, '
            f')>'
        )


class Vulnerability(Base, BehaviorModel):
    __tablename__ = 'vulnerability'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cve_id = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    cmd_86 = Column(JSON, nullable=False)
    cmd_64 = Column(JSON, nullable=True)
    platform_id = Column(Integer, ForeignKey('platform.id'))
    version = Column(JSON, nullable=True)

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}('
            f'id={self.id}, '
            f'cve={self.cve_id}, '
            f'description={self.description}, '
            f'severity={self.severity}, '
            f'command_and_result_x86={self.cmd_86}, '
            f'command_and_result_x64={self.cmd_64}, '
            f'platform={self.platform_id}, '
            f'versions_platform={self.versions}, '
            f')>'
        )
