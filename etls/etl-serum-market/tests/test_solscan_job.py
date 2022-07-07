
import os
from typing import Any
from src.extract import SolscanApi
from src.transform import SolscanTransformer
from src.load import SolscanLoader


def test_job():
    market_address: str = "Di66GTLsV64JgCCYGVcY21RZ173BHkjJVgPyezNN7P1K"
    points = []
    raw_data: Any = SolscanApi.amm_statistics(market_address)
    transformed_data: Any = SolscanTransformer.amm_statistics(
        data=raw_data)
    base_symbol: str = transformed_data["base_symbol"]
    quote_symbol: str = transformed_data["quote_symbol"]
    program_id: str = transformed_data['program_id']
    points += SolscanLoader.amm_statistics(
        market_address=market_address,
        program_id=program_id,
        base_symbol=base_symbol,
        quote_symbol=quote_symbol,
        data=transformed_data)
    assert len(points) > 0
