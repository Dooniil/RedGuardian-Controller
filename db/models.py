from sqlalchemy import Column, Integer, String, JSON, ForeignKey, select
from sqlalchemy.orm import relationship

from db.database import Base, async_db_session


class ModelAdmin:
    @classmethod
    async def create(cls, **kwargs):
        async_db_session.add(cls(**kwargs))
        await async_db_session.commit()

    @classmethod
    async def get(cls, id):
        stmt = select(cls).where(cls.id == id)
        results = await async_db_session.execute(stmt)
        (result, ) = results.one()
        return result


class Family(Base, ModelAdmin):
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


class Platform(Base, ModelAdmin):
    __tablename__ = 'platform'

    id = Column(Integer, primary_key=True, autoincrement=True)
    family_id = Column(ForeignKey('family.id'))
    name = Column(String, nullable=False, unique=True)
    vulnerabilities = relationship('Vulnerability')

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}('
            f'id={self.id}, '
            f'family={self.family_id}, '
            f'name={self.name}, '
            f')>'
        )


class Vulnerability(Base, ModelAdmin):
    __tablename__ = 'vulnerability'

    id = Column(Integer, primary_key=True, autoincrement=True)
    cve_id = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    severity = Column(Integer, nullable=False)
    cmd_86 = Column(JSON, nullable=False)
    cmd_64 = Column(JSON, nullable=True)
    platform_id = Column(ForeignKey('platform.id'))
    versions = Column(JSON, nullable=True)

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
