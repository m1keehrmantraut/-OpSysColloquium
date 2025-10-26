from src.algorithms import LinkedList, get_linked_list_values
from src.request import RequestModel
from src.response import ResponseModel

from .base import BaseUseCase


class GetLinkedListValues(BaseUseCase):
    class Request(RequestModel):
        values: list[int]

    class Response(ResponseModel):
        values: list[int]

    def __init__(self) -> None:
        pass

    async def execute(self, request: Request):
        linked_list = LinkedList(request.values)
        result = get_linked_list_values(linked_list.root)
        return self.Response(values=result)
