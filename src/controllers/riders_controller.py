from typing import Dict
from src.errors.error_types.http_bad_request import HttpBadRequestError
from src.models.sqlite.interfaces.riders_repo import RidersRepositoryInterface
from .interfaces.riders_creator_controller import RidersCreatorControllerInterface

class RidersCreatorController(RidersCreatorControllerInterface):
    def __init__(self, riders_repository: RidersRepositoryInterface) -> None:
        self.__riders_repository = riders_repository

    def create(self, rider_info: Dict) -> Dict:
        name = rider_info["name"]
        hub_id = rider_info["hub_id"]

        self.__validate_name(name)
        self.__insert_rider_in_db(name, hub_id)

        return self.__format_response(rider_info)

    # 🔒 validação simples
    def __validate_name(self, name: str) -> None:
        if not name or len(name.strip()) < 2:
            raise HttpBadRequestError("Invalid rider name")

    # 💾 persistência
    def __insert_rider_in_db(self, name: str, hub_id: int) -> None:
        self.__riders_repository.insert_rider(
            name=name,
            hub_id=hub_id
        )

    # 📦 response padrão
    def __format_response(self, rider_info: Dict) -> Dict:
        return {
            "data": {
                "type": "rider",
                "count": 1,
                "attributes": rider_info
            }
        }
