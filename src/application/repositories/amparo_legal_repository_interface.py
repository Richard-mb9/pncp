from typing import Optional
from abc import ABC, abstractmethod

from domain import AmparoLegal


class AmparoLegalRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, amparo_legal: AmparoLegal) -> AmparoLegal:
        raise NotImplementedError("Should implement method: insert")

    @abstractmethod
    def find_by_id(self, amparo_legal_id: int) -> Optional[AmparoLegal]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_compra_id(self, compra_id: int) -> Optional[AmparoLegal]:
        raise NotImplementedError("Should implement method: find_by_compra_id")
