import os
from typing import Any
from src.extract import SerumServiceApi
from src.transform import SerumServiceTransformer
from src.load import SerumServiceLoader


def test_job():
    program_id: str = "some_id"
    market_address: str = "Di66GTLsV64JgCCYGVcY21RZ173BHkjJVgPyezNN7P1K"
    base_symbol: str = 'ATLAS'
    quote_symbol: str = 'USDC'

    points = []
    if program_id:
        raw_data: Any = SerumServiceApi.market_data(
            market_address=market_address,
            program_id=program_id,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol)
        transformed_data: Any = SerumServiceTransformer.market_data(
            data=raw_data)
        points += SerumServiceLoader.market_data(
            market_address=market_address,
            program_id=program_id,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            data=transformed_data)
    assert len(points) > 0
