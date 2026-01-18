from application.repositories import RepositoryManagerInterface
from infra.database_manager import DatabaseManagerConnection
from .compra_repository import CompraRepository
from .orgao_entidade_repository import OrgaoEntidadeRepository
from .unidade_orgao_repository import UnidadeOrgaoRepository
from .amparo_legal_repository import AmparoLegalRepository


class RepositoryManager(RepositoryManagerInterface):

    def __init__(self, db_manager: DatabaseManagerConnection):
        self.db_manager = db_manager

    def compra_repository(self) -> CompraRepository:
        return CompraRepository(self.db_manager)

    def orgao_entidade_repository(self) -> OrgaoEntidadeRepository:
        return OrgaoEntidadeRepository(self.db_manager)

    def unidade_orgao_repository(self) -> UnidadeOrgaoRepository:
        return UnidadeOrgaoRepository(self.db_manager)

    def amparo_legal_repository(self) -> AmparoLegalRepository:
        return AmparoLegalRepository(self.db_manager)
