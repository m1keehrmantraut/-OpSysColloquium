from src.algorithms import get_distinct_values
from src.request import RequestModel
from src.response import ResponseModel

from .base import BaseUseCase


class GetDistinctValues(BaseUseCase):
    class Request(RequestModel):
        values: list[int]

    class Response(ResponseModel):
        values: list[int]

    def __init__(self) -> None:
        pass

    async def execute(self, request: Request):
        result = get_distinct_values(request.values)
        return self.Response(values=result)
