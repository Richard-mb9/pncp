from datetime import datetime, timedelta

from infra.integrations import PNCP


class GetDataService:
    def __init__(self):
        self.pncp_integration = PNCP()

    def execute(self):
        today = datetime.today()
        dates = [(today - timedelta(days=i)) for i in range(30)]
        for date in dates:
            result = self.pncp_integration.get_data(
                data_inical=date, data_final=date, codigo_modalidade_contratacao=6
            )
            print(len(result))
