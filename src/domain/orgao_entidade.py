from typing import Optional
from datetime import datetime


class OrgaoEntidade:
    id: int

    def __init__(
        self,
        compra_id: int,
        cnpj: str,
        razao_social: str,
        poder_id: str,
        esfera_id: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.compra_id = compra_id
        self.cnpj = cnpj
        self.razao_social = razao_social
        self.poder_id = poder_id
        self.esfera_id = esfera_id
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at
