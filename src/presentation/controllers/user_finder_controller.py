from src import data
from src.presentation.interfaces.controller_interface import ControllerInterface
from src.presentation.http_types.http_request import HttpRequest
from src.presentation.http_types.http_response import HttpResponse
from src.domain.use_case.user_finder_interface import UserFinderInterface



class UserfinderController(ControllerInterface):
    
    def __init__(self,use_case: UserFinderInterface ) -> None:
        self.__use_case = use_case
    
    def handle(self, http_request: HttpRequest, ) -> HttpResponse:
        
        name = http_request.query_params['name']

        response = self.__use_case.find(name)

        return HttpResponse(status_code = 200,
                            body={'data': response}
                            )
