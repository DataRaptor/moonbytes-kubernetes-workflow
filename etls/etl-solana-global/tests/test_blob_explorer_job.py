import os
from typing import Any
from src.extract import SolanaBlockExplorerApi
from src.transform import SolanaBlockExplorerTransformer
from src.load import SolanaBlockExplorerLoader


def test_job():
    points = []
    raw_data: Any = SolanaBlockExplorerApi.supply()
    transformed_data: Any = SolanaBlockExplorerTransformer.supply(
        data=raw_data)
    points += SolanaBlockExplorerLoader.supply(
        data=transformed_data)
    print(points)
    assert len(points) > 0
