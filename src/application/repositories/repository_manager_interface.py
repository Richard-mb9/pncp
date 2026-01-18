from abc import ABC, abstractmethod

from .compra_repository_interface import CompraRepositoryInterface
from .orgao_entidade_repository_interface import OrgaoEntidadeRepositoryInterface
from .unidade_orgao_repository_interface import UnidadeOrgaoRepositoryInterface
from .amparo_legal_repository_interface import AmparoLegalRepositoryInterface


class RepositoryManagerInterface(ABC):

    @abstractmethod
    def compra_repository(self) -> CompraRepositoryInterface:
        raise NotImplementedError("Should implement method: compra_repository")

    @abstractmethod
    def orgao_entidade_repository(self) -> OrgaoEntidadeRepositoryInterface:
        raise NotImplementedError("Should implement method: orgao_entidade_repository")

    @abstractmethod
    def unidade_orgao_repository(self) -> UnidadeOrgaoRepositoryInterface:
        raise NotImplementedError("Should implement method: unidade_orgao_repository")

    @abstractmethod
    def amparo_legal_repository(self) -> AmparoLegalRepositoryInterface:
        raise NotImplementedError("Should implement method: amparo_legal_repository")
