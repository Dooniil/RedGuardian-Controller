from db.models import Family, Platform, Vulnerability
import json

async def init_family():
    await Family.create(name='Windows')
    await Family.create(name='Unix')


async def init_platform():
    await Platform.create(family_id=1, name='Microsoft 10')
    await Platform.create(family_id=6, name='Debian 11')


    # id = Column(Integer, primary_key=True, autoincrement=True)
    # cve_id = Column(String, nullable=False, unique=True)
    # description = Column(String, nullable=False)
    # severity = Column(Integer, nullable=False)
    # cmd_86 = Column(JSON, nullable=False)
    # cmd_64 = Column(JSON, nullable=True)
    # platform_id = Column(Integer, ForeignKey('platform.id'))
    # version = Column(JSON, nullable=True)
async def init_vulnerability():
    await Vulnerability.create(
        cve_id='CVE-2021-34527',
        description='Windows Print Spooler Remote Code Execution Vulnerability',
        severity=4,
        cmd_86=json.dumps({
            'Get-Service -Name Spooler': 'Stopped'
        }, separators=(',', ':')),
        platform_id=1,
        version=json.dumps({
            'Get-Service -Name Spooler': 'Stopped'
        }, separators=(',', ':'))
    )
