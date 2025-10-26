import pytest
from src.use_cases import GetDistinctValues


class TestGetDistinctValues:
    @pytest.mark.asyncio
    async def test_success_response(self):
        use_case = GetDistinctValues()
        request = GetDistinctValues.Request(values=[1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
        response = await use_case.execute(request)

        assert isinstance(response, GetDistinctValues.Response)
        assert response.values == [1, 2, 3, 4]
