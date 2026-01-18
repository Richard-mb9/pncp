from datetime import datetime, timedelta

from infra.integrations import PNCP
from infra.repositories import RepositoryManager
from infra.database_manager import DatabaseManagerConnection

from application.usecases.save_data_use_case import SaveDataUseCase


class GetDataService:
    def __init__(self):
        self.pncp_integration = PNCP()
        self.repository_manager = RepositoryManager(DatabaseManagerConnection())
        self.use_case = SaveDataUseCase(self.repository_manager)

    def execute(self):
        today = datetime.today()
        dates = [(today - timedelta(days=i)) for i in range(30)]
        for date in dates:
            result = self.pncp_integration.get_data(
                data_inical=date, data_final=date, codigo_modalidade_contratacao=6
            )

            self.use_case.execute(result)
