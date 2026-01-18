from typing import Optional
from abc import ABC, abstractmethod

from domain import Compra


class CompraRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, compra: Compra) -> Compra:
        raise NotImplementedError("Should implement method: insert")

    @abstractmethod
    def find_by_id(self, compra_id: int) -> Optional[Compra]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_numero_controle_pncp(self, numero_controle_pncp: str) -> Optional[Compra]:
        raise NotImplementedError("Should implement method: find_by_numero_controle_pncp")
