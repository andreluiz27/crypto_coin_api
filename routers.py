import asyncio
import datetime
import httpx

from fastapi import APIRouter
from fastapi import Request
from schemas import CryptoDataResponse
from helpers import get_cryptocoin_data, convert_brl_to_usd, get_api_key
from fastapi_simple_cache.decorator import cache
from fastapi.security.api_key import APIKey
from fastapi import Depends


router = APIRouter()
request_client = httpx.AsyncClient()


@router.get("/")
async def root():
    """
    Returns a JSON response with a message "Hello World".
    """
    return {"message": "Hello World"}


@router.post("/coin_infos")
@cache(expire=60)
async def fetch_crypto_data(crypto_symbol: str, request: Request, api_key: APIKey = Depends(get_api_key)):
    """
    Fetches cryptocurrency data for a given symbol.

    Args:
        crypto_symbol (str): The symbol of the cryptocurrency.
        request (Request): The request object.
        api_key (APIKey, optional): The API key. Defaults to None.

    Returns:
        dict: The cryptocurrency data response.
    """

    crypto_data_response = await get_cryptocoin_data(
        crypto_symbol, request_client=request_client, api="mb-api"
    )
    if "error" in crypto_data_response:
        crypto_data_response = await get_cryptocoin_data(
            crypto_symbol, request_client=request_client, api="awesome-api"
        )



    return crypto_data_response
