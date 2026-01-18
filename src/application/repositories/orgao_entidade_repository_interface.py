from typing import Optional
from abc import ABC, abstractmethod

from domain import OrgaoEntidade


class OrgaoEntidadeRepositoryInterface(ABC):

    @abstractmethod
    def insert(self, orgao_entidade: OrgaoEntidade) -> OrgaoEntidade:
        raise NotImplementedError("Should implement method: insert")

    @abstractmethod
    def find_by_id(self, orgao_entidade_id: int) -> Optional[OrgaoEntidade]:
        raise NotImplementedError("Should implement method: find_by_id")

    @abstractmethod
    def find_by_compra_id(self, compra_id: int) -> Optional[OrgaoEntidade]:
        raise NotImplementedError("Should implement method: find_by_compra_id")
