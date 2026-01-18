from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from domain import UnidadeOrgao

from .mapper_config import mapper_registry

unidade_orgao = Table(
    "unidade_orgao",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("compra_id", Integer, ForeignKey("compra.id"), nullable=False),
    Column("uf_nome", String, nullable=False),
    Column("codigo_unidade", String, nullable=False),
    Column("uf_sigla", String, nullable=False),
    Column("municipio_nome", String, nullable=False),
    Column("nome_unidade", String, nullable=False),
    Column("codigo_ibge", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
    Column("updated_at", DateTime, nullable=True),
)

mapper_registry.map_imperatively(UnidadeOrgao, unidade_orgao)
