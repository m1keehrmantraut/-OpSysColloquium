from src.algorithms import calculate_factorial
from src.request import RequestModel
from src.response import ResponseModel

from .base import BaseUseCase


class CalculateFactorial(BaseUseCase):
    class Request(RequestModel):
        value: int

    class Response(ResponseModel):
        values: list[int]

    async def execute(self, request: Request):
        result = calculate_factorial(request.value)
        return self.Response(values=result)
