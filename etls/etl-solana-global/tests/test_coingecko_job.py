import os
from typing import Any
from src.extract import CoinGeckoApi
from src.transform import CoinGeckoTransformer
from src.load import CoinGeckoLoader


def test_job():
    points = []
    raw_data: Any = CoinGeckoApi.token_info()
    transformed_data: Any = CoinGeckoTransformer.token_info(
        data=raw_data)
    points += CoinGeckoLoader.token_info(
        data=transformed_data)
    assert len(points) > 0
