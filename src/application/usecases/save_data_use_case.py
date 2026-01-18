from typing import List, Dict, Any
from datetime import datetime

from application.repositories import RepositoryManagerInterface
from domain import Compra, OrgaoEntidade, UnidadeOrgao, AmparoLegal


class SaveDataUseCase:
    def __init__(self, repository_manager: RepositoryManagerInterface) -> None:
        self.compra_repository = repository_manager.compra_repository()
        self.orgao_entidade_repository = repository_manager.orgao_entidade_repository()
        self.unidade_orgao_repository = repository_manager.unidade_orgao_repository()
        self.amparo_legal_repository = repository_manager.amparo_legal_repository()

    def execute(self, data: List[Dict[str, Any]]) -> None:
        for item in data:
            numero_controle_pncp = item["numeroControlePNCP"]

            existing_compra = self.compra_repository.find_by_numero_controle_pncp(
                numero_controle_pncp
            )
            if existing_compra:
                continue

            compra = self._create_compra(item)
            saved_compra = self.compra_repository.insert(compra)

            if item.get("orgaoEntidade"):
                orgao_entidade = self._create_orgao_entidade(
                    item["orgaoEntidade"], saved_compra.id
                )
                self.orgao_entidade_repository.insert(orgao_entidade)

            if item.get("unidadeOrgao"):
                unidade_orgao = self._create_unidade_orgao(
                    item["unidadeOrgao"], saved_compra.id
                )
                self.unidade_orgao_repository.insert(unidade_orgao)

            if item.get("amparoLegal"):
                amparo_legal = self._create_amparo_legal(
                    item["amparoLegal"], saved_compra.id
                )
                self.amparo_legal_repository.insert(amparo_legal)

    def _parse_datetime(self, date_string: str) -> datetime:
        return datetime.fromisoformat(date_string)

    def _create_compra(self, item: Dict[str, Any]) -> Compra:
        return Compra(
            data_atualizacao=self._parse_datetime(item["dataAtualizacao"]),
            ano_compra=item["anoCompra"],
            sequencial_compra=item["sequencialCompra"],
            numero_compra=item["numeroCompra"],
            processo=item["processo"],
            objeto_compra=item["objetoCompra"],
            valor_total_homologado=item.get("valorTotalHomologado"),
            srp=item["srp"],
            data_inclusao=self._parse_datetime(item["dataInclusao"]),
            data_abertura_proposta=self._parse_datetime(item["dataAberturaProposta"]),
            data_encerramento_proposta=self._parse_datetime(
                item["dataEncerramentoProposta"]
            ),
            data_publicacao_pncp=self._parse_datetime(item["dataPublicacaoPncp"]),
            data_atualizacao_global=self._parse_datetime(item["dataAtualizacaoGlobal"]),
            numero_controle_pncp=item["numeroControlePNCP"],
            modalidade_id=item["modalidadeId"],
            modo_disputa_id=item["modoDisputaId"],
            valor_total_estimado=item["valorTotalEstimado"],
            modalidade_nome=item["modalidadeNome"],
            modo_disputa_nome=item["modoDisputaNome"],
            tipo_instrumento_convocatorio_codigo=item[
                "tipoInstrumentoConvocatorioCodigo"
            ],
            tipo_instrumento_convocatorio_nome=item["tipoInstrumentoConvocatorioNome"],
            situacao_compra_id=item["situacaoCompraId"],
            situacao_compra_nome=item["situacaoCompraNome"],
            usuario_nome=item["usuarioNome"],
            orgao_sub_rogado=item.get("orgaoSubRogado"),
            unidade_sub_rogada=item.get("unidadeSubRogada"),
            informacao_complementar=item.get("informacaoComplementar"),
            link_sistema_origem=item.get("linkSistemaOrigem"),
            justificativa_presencial=item.get("justificativaPresencial"),
            link_processo_eletronico=item.get("linkProcessoEletronico"),
        )

    def _create_orgao_entidade(
        self, data: Dict[str, Any], compra_id: int
    ) -> OrgaoEntidade:
        return OrgaoEntidade(
            compra_id=compra_id,
            cnpj=data["cnpj"],
            razao_social=data["razaoSocial"],
            poder_id=data["poderId"],
            esfera_id=data["esferaId"],
        )

    def _create_unidade_orgao(
        self, data: Dict[str, Any], compra_id: int
    ) -> UnidadeOrgao:
        return UnidadeOrgao(
            compra_id=compra_id,
            uf_nome=data["ufNome"],
            codigo_unidade=data["codigoUnidade"],
            uf_sigla=data["ufSigla"],
            municipio_nome=data["municipioNome"],
            nome_unidade=data["nomeUnidade"],
            codigo_ibge=data["codigoIbge"],
        )

    def _create_amparo_legal(self, data: Dict[str, Any], compra_id: int) -> AmparoLegal:
        return AmparoLegal(
            compra_id=compra_id,
            codigo=data["codigo"],
            nome=data["nome"],
            descricao=data["descricao"],
        )
