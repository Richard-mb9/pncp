from services import GetDataService
from infra.mappers import import_mappers


def execute():
    import_mappers()
    GetDataService().execute()


execute()
