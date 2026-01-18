from typing import List, Dict, Any
from application.repositories import RepositoryManagerInterface


class SaveDataUseCase:
    def __init__(self, repository_manager: RepositoryManagerInterface) -> None:
        self.compra_repository = repository_manager.compra_repository()
        self.orgao_entidade_repository = repository_manager.orgao_entidade_repository()
        self.unidade_orgao_repository = repository_manager.unidade_orgao_repository()
        self.amparo_legal_repository = repository_manager.amparo_legal_repository()

    def execute(self, data: List[Dict[str, Any]]) -> None:
        pass
