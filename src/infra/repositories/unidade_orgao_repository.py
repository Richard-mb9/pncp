from typing import Optional

from application.repositories import UnidadeOrgaoRepositoryInterface
from infra.database_manager import DatabaseManagerConnection
from domain import UnidadeOrgao


class UnidadeOrgaoRepository(UnidadeOrgaoRepositoryInterface):

    def __init__(self, db_manager: DatabaseManagerConnection):
        self.session = db_manager.session

    def insert(self, unidade_orgao: UnidadeOrgao) -> UnidadeOrgao:
        self.session.add(unidade_orgao)
        self.session.commit()
        return unidade_orgao

    def find_by_id(self, unidade_orgao_id: int) -> Optional[UnidadeOrgao]:
        return self.session.query(UnidadeOrgao).filter_by(id=unidade_orgao_id).first()

    def find_by_compra_id(self, compra_id: int) -> Optional[UnidadeOrgao]:
        return self.session.query(UnidadeOrgao).filter_by(compra_id=compra_id).first()
