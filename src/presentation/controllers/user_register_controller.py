from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_case.user_register_interface import UserRegisterInterface



class UserRegisterController(ControllerInterface):

    def __init__(self, use_case: UserRegisterInterface) -> None:
        self.__use_case = use_case

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.body['name']
        email = http_request.body['email']

        new_user = self.__use_case.register(name = name, email = email)
        
        return HttpResponse(status_code = 200,
                            body = {'data': name}
                            )