from typing import Optional

from application.repositories import CompraRepositoryInterface
from infra.database_manager import DatabaseManagerConnection
from domain import Compra


class CompraRepository(CompraRepositoryInterface):

    def __init__(self, db_manager: DatabaseManagerConnection):
        self.session = db_manager.session

    def insert(self, compra: Compra) -> Compra:
        self.session.add(compra)
        self.session.commit()
        return compra

    def find_by_id(self, compra_id: int) -> Optional[Compra]:
        return self.session.query(Compra).filter_by(id=compra_id).first()

    def find_by_numero_controle_pncp(self, numero_controle_pncp: str) -> Optional[Compra]:
        return self.session.query(Compra).filter_by(numero_controle_pncp=numero_controle_pncp).first()
