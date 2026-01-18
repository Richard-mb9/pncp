from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from .orgao_entidade import OrgaoEntidade
    from .unidade_orgao import UnidadeOrgao
    from .amparo_legal import AmparoLegal


class Compra:
    orgao_entidade: "OrgaoEntidade"
    unidade_orgao: "UnidadeOrgao"
    amparo_legal: "AmparoLegal"

    def __init__(
        self,
        id: int,
        data_atualizacao: datetime,
        ano_compra: int,
        sequencial_compra: int,
        numero_compra: str,
        processo: str,
        objeto_compra: str,
        valor_total_homologado: Optional[float],
        srp: bool,
        data_inclusao: datetime,
        data_abertura_proposta: datetime,
        data_encerramento_proposta: datetime,
        data_publicacao_pncp: datetime,
        data_atualizacao_global: datetime,
        numero_controle_pncp: str,
        modalidade_id: int,
        modo_disputa_id: int,
        valor_total_estimado: float,
        modalidade_nome: str,
        modo_disputa_nome: str,
        tipo_instrumento_convocatorio_codigo: int,
        tipo_instrumento_convocatorio_nome: str,
        situacao_compra_id: int,
        situacao_compra_nome: str,
        usuario_nome: str,
        orgao_sub_rogado: Optional[str] = None,
        unidade_sub_rogada: Optional[str] = None,
        informacao_complementar: Optional[str] = None,
        link_sistema_origem: Optional[str] = None,
        justificativa_presencial: Optional[str] = None,
        link_processo_eletronico: Optional[str] = None,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
    ) -> None:
        self.id = id
        self.data_atualizacao = data_atualizacao
        self.ano_compra = ano_compra
        self.sequencial_compra = sequencial_compra
        self.numero_compra = numero_compra
        self.processo = processo
        self.objeto_compra = objeto_compra
        self.valor_total_homologado = valor_total_homologado
        self.srp = srp
        self.data_inclusao = data_inclusao
        self.data_abertura_proposta = data_abertura_proposta
        self.data_encerramento_proposta = data_encerramento_proposta
        self.data_publicacao_pncp = data_publicacao_pncp
        self.data_atualizacao_global = data_atualizacao_global
        self.numero_controle_pncp = numero_controle_pncp
        self.modalidade_id = modalidade_id
        self.modo_disputa_id = modo_disputa_id
        self.valor_total_estimado = valor_total_estimado
        self.modalidade_nome = modalidade_nome
        self.modo_disputa_nome = modo_disputa_nome
        self.tipo_instrumento_convocatorio_codigo = tipo_instrumento_convocatorio_codigo
        self.tipo_instrumento_convocatorio_nome = tipo_instrumento_convocatorio_nome
        self.situacao_compra_id = situacao_compra_id
        self.situacao_compra_nome = situacao_compra_nome
        self.usuario_nome = usuario_nome
        self.orgao_sub_rogado = orgao_sub_rogado
        self.unidade_sub_rogada = unidade_sub_rogada
        self.informacao_complementar = informacao_complementar
        self.link_sistema_origem = link_sistema_origem
        self.justificativa_presencial = justificativa_presencial
        self.link_processo_eletronico = link_processo_eletronico
        self.created_at = created_at if created_at is not None else datetime.now()
        self.updated_at = updated_at
