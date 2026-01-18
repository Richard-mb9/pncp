from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from domain import OrgaoEntidade

from .mapper_config import mapper_registry

orgao_entidade = Table(
    "orgao_entidade",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("compra_id", Integer, ForeignKey("compra.id"), nullable=False),
    Column("cnpj", String, nullable=False),
    Column("razao_social", String, nullable=False),
    Column("poder_id", String, nullable=False),
    Column("esfera_id", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
    Column("updated_at", DateTime, nullable=True),
)

mapper_registry.map_imperatively(OrgaoEntidade, orgao_entidade)
