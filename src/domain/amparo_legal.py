from typing import Optional
from datetime import datetime


class AmparoLegal:
    id: int

    def __init__(
        self,
        compra_id: int,
        codigo: int,
        nome: str,
        descricao: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.compra_id = compra_id
        self.codigo = codigo
        self.nome = nome
        self.descricao = descricao
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at
