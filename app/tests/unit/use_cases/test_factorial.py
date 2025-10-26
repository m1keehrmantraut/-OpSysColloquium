import pytest
from src.use_cases import CalculateFactorial


class TestCalculateFactorial:
    @pytest.mark.asyncio
    async def test_success_response(self):
        use_case = CalculateFactorial()
        request = CalculateFactorial.Request(value=5)
        response = await use_case.execute(request)

        assert isinstance(response, CalculateFactorial.Response)
        assert response.values == [1, 2, 6, 24, 120]
