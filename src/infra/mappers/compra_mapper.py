from sqlalchemy import Table, Column, Integer, String, DateTime, Float, Boolean, Text
from sqlalchemy.orm import relationship

from domain import Compra

from .mapper_config import mapper_registry

compra = Table(
    "compra",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True),
    Column("data_atualizacao", DateTime, nullable=False),
    Column("ano_compra", Integer, nullable=False),
    Column("sequencial_compra", Integer, nullable=False),
    Column("numero_compra", String, nullable=False),
    Column("processo", String, nullable=False),
    Column("objeto_compra", Text, nullable=False),
    Column("valor_total_homologado", Float, nullable=True),
    Column("srp", Boolean, nullable=False),
    Column("data_inclusao", DateTime, nullable=False),
    Column("data_abertura_proposta", DateTime, nullable=False),
    Column("data_encerramento_proposta", DateTime, nullable=False),
    Column("data_publicacao_pncp", DateTime, nullable=False),
    Column("data_atualizacao_global", DateTime, nullable=False),
    Column("numero_controle_pncp", String, nullable=False, index=True),
    Column("modalidade_id", Integer, nullable=False),
    Column("modo_disputa_id", Integer, nullable=False),
    Column("valor_total_estimado", Float, nullable=False),
    Column("modalidade_nome", String, nullable=False),
    Column("modo_disputa_nome", String, nullable=False),
    Column("tipo_instrumento_convocatorio_codigo", Integer, nullable=False),
    Column("tipo_instrumento_convocatorio_nome", String, nullable=False),
    Column("situacao_compra_id", Integer, nullable=False),
    Column("situacao_compra_nome", String, nullable=False),
    Column("usuario_nome", String, nullable=False),
    Column("orgao_sub_rogado", String, nullable=True),
    Column("unidade_sub_rogada", String, nullable=True),
    Column("informacao_complementar", Text, nullable=True),
    Column("link_sistema_origem", String, nullable=True),
    Column("justificativa_presencial", Text, nullable=True),
    Column("link_processo_eletronico", String, nullable=True),
    Column("created_at", DateTime, nullable=True),
    Column("updated_at", DateTime, nullable=True),
)

mapper_registry.map_imperatively(
    Compra,
    compra,
    properties={
        "orgao_entidade": relationship(
            "OrgaoEntidade",
            uselist=False,
            backref="compra",
        ),
        "unidade_orgao": relationship(
            "UnidadeOrgao",
            uselist=False,
            backref="compra",
        ),
        "amparo_legal": relationship(
            "AmparoLegal",
            uselist=False,
            backref="compra",
        ),
    },
)
