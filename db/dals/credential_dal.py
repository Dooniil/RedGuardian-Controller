from db.models.data_for_task_models import Credential


class HostDAL:
    @staticmethod
    async def create_new_host(**kwargs):
        credential = await Credential.create(**kwargs)
        return credential

    @staticmethod
    async def delete_host(id_credential):
        await Credential.delete(id_credential)
        return True
