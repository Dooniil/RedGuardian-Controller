from db.models.Vulnerabilities import Vulnerability
from sqlalchemy.orm import Session
from sqlalchemy.future import select


class VulnerabilityDAL:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    async def get_all_vulnerabilities(self) -> list:
        q = await self.db_session.execute(select(Vulnerability).order_by(Vulnerability.id))
        return q.scalars().all()
