from services import GetDataService
from infra.mappers import import_mappers


import_mappers()
GetDataService().execute()
