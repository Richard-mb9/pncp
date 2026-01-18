from typing import Optional

from application.repositories import AmparoLegalRepositoryInterface
from infra.database_manager import DatabaseManagerConnection
from domain import AmparoLegal


class AmparoLegalRepository(AmparoLegalRepositoryInterface):

    def __init__(self, db_manager: DatabaseManagerConnection):
        self.session = db_manager.session

    def insert(self, amparo_legal: AmparoLegal) -> AmparoLegal:
        self.session.add(amparo_legal)
        self.session.commit()
        return amparo_legal

    def find_by_id(self, amparo_legal_id: int) -> Optional[AmparoLegal]:
        return self.session.query(AmparoLegal).filter_by(id=amparo_legal_id).first()

    def find_by_compra_id(self, compra_id: int) -> Optional[AmparoLegal]:
        return self.session.query(AmparoLegal).filter_by(compra_id=compra_id).first()
