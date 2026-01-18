from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey

from domain import AmparoLegal

from .mapper_config import mapper_registry

amparo_legal = Table(
    "amparo_legal",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("compra_id", Integer, ForeignKey("compra.id"), nullable=False),
    Column("codigo", Integer, nullable=False),
    Column("nome", String, nullable=False),
    Column("descricao", String, nullable=False),
    Column("created_at", DateTime, nullable=True),
    Column("updated_at", DateTime, nullable=True),
)

mapper_registry.map_imperatively(AmparoLegal, amparo_legal)
