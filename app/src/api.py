from typing import Annotated

from fastapi import APIRouter, Depends

from src.use_cases import CalculateFactorial, GetDistinctValues, GetLinkedListValues

api_router = APIRouter()


@api_router.post("/factorial")
async def calculate_factorial(
    query: CalculateFactorial.Request,
    use_case: Annotated[CalculateFactorial, Depends(CalculateFactorial)],
):
    values = await use_case.execute(query)
    return values


@api_router.post("/distinct")
async def get_distinct_values(
    query: GetDistinctValues.Request,
    use_case: Annotated[GetDistinctValues, Depends(GetDistinctValues)],
):
    values = await use_case.execute(query)
    return values


@api_router.post("/linked_list")
async def get_linked_list_values(
    query: GetLinkedListValues.Request,
    use_case: Annotated[GetLinkedListValues, Depends(GetLinkedListValues)],
):
    values = await use_case.execute(query)
    return values
