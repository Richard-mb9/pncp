from typing import Optional
from datetime import datetime


class UnidadeOrgao:
    def __init__(
        self,
        id: int,
        compra_id: int,
        uf_nome: str,
        codigo_unidade: str,
        uf_sigla: str,
        municipio_nome: str,
        nome_unidade: str,
        codigo_ibge: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.compra_id = compra_id
        self.uf_nome = uf_nome
        self.codigo_unidade = codigo_unidade
        self.uf_sigla = uf_sigla
        self.municipio_nome = municipio_nome
        self.nome_unidade = nome_unidade
        self.codigo_ibge = codigo_ibge
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at
