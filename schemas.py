from pydantic import BaseModel, Field


class CryptoDataResponse(BaseModel):
    coin_name: str = Field(..., title="Coin Name", description="Name of the cryptocurrency", example="Bitcoin")
    symbol: str = Field(..., title="Symbol", description="Symbol of the cryptocurrency", example="BTC")
    coin_price: float = Field(..., title="Coin Price", description="Price of the cryptocurrency", example=200.501231)
    coin_price_dolar: float = Field(..., title="Coin Price Dolar", description="Price of the cryptocurrency in USD", example="40.039391")
    date_consult: str = Field(..., title="Date Consult", description="Date of the consultation", example="2024-01-20 06:35:06")

