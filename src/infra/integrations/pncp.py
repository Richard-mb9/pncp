from datetime import datetime
from typing import List, Dict, Any

import requests
from requests.exceptions import HTTPError

from config import BASE_URL_PNCP


class PNCP:
    def __init__(self) -> None:
        pass

    def get_data(
        self,
        data_inical: datetime,
        data_final: datetime,
        codigo_modalidade_contratacao: int,
    ) -> List[Dict[str, Any]]:
        data_inicial_formatted = data_inical.strftime("%Y%m%d")
        data_final_formatted = data_final.strftime("%Y%m%d")

        range_for_log = f"({data_inicial_formatted} - {data_final_formatted})"

        params = {
            "dataInicial": data_inicial_formatted,
            "dataFinal": data_final_formatted,
            "codigoModalidadeContratacao": codigo_modalidade_contratacao,
            "pagina": 1,
            "tamanhoPagina": 50,
        }

        try:
            response = requests.get(
                f"{BASE_URL_PNCP}/contratacoes/publicacao", params=params, timeout=3
            )
            response.raise_for_status()
            response_data: Dict[str, Any] = response.json()

            return response_data.get("data", [])
        except HTTPError as error:
            print(f"error http para o range ({range_for_log}): {error.response.json()}")
            return []

        except Exception as error:
            print(f"erro generico para o range ({range_for_log}): {error.args}")
            return []
