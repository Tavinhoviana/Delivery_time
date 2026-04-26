from src.controllers.pet_deleter_controller import PetDeleterController
from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class OrdersDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self.__controller.delete(name)

        return HttpResponse(status_code=204)