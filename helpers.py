import asyncio
import os
import datetime


from database import forecast_collection
from schemas import CryptoDataResponse
from fastapi import Security, HTTPException, Depends
from fastapi.security.api_key import APIKeyHeader
from constants import API_CRYPTO


api_key_header = APIKeyHeader(name="access_token", auto_error=False)

async def get_cryptocoin_data(crypto_symbol,request_client, api):
    """
    Fetch the cryptocurrency data from the API.

    Args:
        crypto_symbol (str): The symbol of the cryptocurrency.

    Returns:
        dict: A dictionary containing the response from the API.
    """
    headers = {
        "User-Agent": "fastapi",
        "Accept": "application/json",

    }

    if api == "mb-api":
        url = API_CRYPTO[api]
        response = await request_client.get(f"{url}symbol={crypto_symbol}", headers=headers)

        if response.status_code == 200:
            cryptocoin_data_json = response.json()
            crypto_infos = cryptocoin_data_json["response_data"]["products"][0]
            coin_name = crypto_infos["name"]
            symbol = crypto_infos["product_data"]["symbol"]
            coin_price = crypto_infos["market_price"]
            coin_price_dolar = await convert_brl_to_usd(float(coin_price), request_client=request_client) 
            date_consult = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        else:
            return {"error": "An error occurred while fetching the data."}   
    
    if api == "awesome-api":
        url = f"{API_CRYPTO[api]}/{crypto_symbol}-BRL"
        response = await request_client.get(url, headers=headers)
        if response.status_code == 200:
            cryptocoin_data_json = response.json()
            data_key = f"{crypto_symbol}BRL"
            coin_name = cryptocoin_data_json[data_key]["name"].split("/")[0]
            symbol = cryptocoin_data_json[data_key]["code"]
            coin_price = cryptocoin_data_json[data_key]["bid"]
            coin_price_dolar = await convert_brl_to_usd(float(coin_price), request_client=request_client)
            date_consult = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
           
        else:
            # Raise an exception if the request fails
            raise HTTPException(status_code=404, detail="API not available")


    crypto_data = CryptoDataResponse(
        coin_name=coin_name,
        symbol=symbol,
        coin_price=coin_price,
        coin_price_dolar=coin_price_dolar,
        date_consult=date_consult
    )


    return crypto_data 

async def convert_brl_to_usd(brl_value, request_client):
    """
    Convert a value from BRL to USD.

    Args:
        brl_value (float): The value in BRL.

    Returns:
        float: The value in USD.
    """
    headers = {
        "User-Agent": "fastapi",
        "Accept": "application/json",
    }

    url = "https://economia.awesomeapi.com.br/last/BRL-USD"
    response = await request_client.get(url, headers=headers)
    conversion_rate = response.json()["BRLUSD"]["bid"]
    return brl_value*float(conversion_rate)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header == os.getenv("API_KEY",'452f7377b202e85cd6c34d2b4cbe43be'):
        return api_key_header   
    else:
        raise HTTPException(
            status_code=HTTP_403_FORBIDDEN, detail="Could not validate API KEY"
        )



   