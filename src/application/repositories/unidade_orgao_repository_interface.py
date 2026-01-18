from typing import Optional
from abc import ABC, abstractmethod

from domain import UnidadeOrgao


class UnidadeOrgaoRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, unidade_orgao: UnidadeOrgao) -> UnidadeOrgao:
        raise NotImplementedError("Should implement method: insert")

    @abstractmethod
    def find_by_id(self, unidade_orgao_id: int) -> Optional[UnidadeOrgao]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_compra_id(self, compra_id: int) -> Optional[UnidadeOrgao]:
        raise NotImplementedError("Should implement method: find_by_compra_id")
