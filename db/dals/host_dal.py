from db.models.data_for_task_models import Host


class HostDAL:
    @staticmethod
    async def create_new_host(**kwargs):
        host = await Host.create(**kwargs)
        return host

    @staticmethod
    async def delete_host(id_host):
        await Host.delete(id_host)
        return True
