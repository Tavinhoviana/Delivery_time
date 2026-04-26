from src.controllers.orders_controller import OrderCreatorControllerInterface
from src.validators.orders_creator_validator import orders_creator_validator

from .interfaces.view_interface import ViewInterface
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class OrdersCreatorView(ViewInterface):
    def __init__(self, controller: OrderCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        orders_creator_validator(http_request)
        person_info = http_request.body
        body_response = self.__controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)