import pytest
from src.use_cases import GetLinkedListValues


class TestGetLinkedListValues:
    @pytest.mark.asyncio
    async def test_success_response(self):
        use_case = GetLinkedListValues()
        request = GetLinkedListValues.Request(values=[1, 3, 5, 4, 2])
        response = await use_case.execute(request)

        assert isinstance(response, GetLinkedListValues.Response)
        assert response.values == [1, 3, 5, 4, 2]
