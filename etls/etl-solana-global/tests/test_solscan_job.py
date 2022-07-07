
import os
from typing import Any
from src.extract import SolscanApi
from src.transform import SolscanTransformer
from src.load import SolscanLoader


def test_job():
    points = []
    raw_data: Any = SolscanApi.price_and_volume_usdt(
        symbol='SOL')
    transformed_data: Any = SolscanTransformer.price_and_volume_usdt(
        data=raw_data)
    points += SolscanLoader.price_and_volume_usdt(
        data=transformed_data)
    assert len(points) > 0
