import os
from typing import Any
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader


def test_job():
    collection_symbol: str = "grim_syndicate"
    max_listings: int = 30
    points = []
    raw_data: Any = MagicEdenApi.collection_listings(
        collection_symbol=collection_symbol,
        max_listings=max_listings)
    transformed_data: Any = MagicEdenTransformer.collection_listings(
        data=raw_data)
    points += MagicEdenLoader.collection_listings(
        collection_symbol=collection_symbol,
        data=transformed_data)

    assert len(points) > 0
