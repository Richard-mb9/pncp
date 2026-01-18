from typing import Optional

from application.repositories import OrgaoEntidadeRepositoryInterface
from infra.database_manager import DatabaseManagerConnection
from domain import OrgaoEntidade


class OrgaoEntidadeRepository(OrgaoEntidadeRepositoryInterface):

    def __init__(self, db_manager: DatabaseManagerConnection):
        self.session = db_manager.session

    def insert(self, orgao_entidade: OrgaoEntidade) -> OrgaoEntidade:
        self.session.add(orgao_entidade)
        self.session.commit()
        return orgao_entidade

    def find_by_id(self, orgao_entidade_id: int) -> Optional[OrgaoEntidade]:
        return self.session.query(OrgaoEntidade).filter_by(id=orgao_entidade_id).first()

    def find_by_compra_id(self, compra_id: int) -> Optional[OrgaoEntidade]:
        return self.session.query(OrgaoEntidade).filter_by(compra_id=compra_id).first()
