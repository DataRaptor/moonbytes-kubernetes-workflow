import os
from typing import Any
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader


def test_job():
    collection_symbol: str = "grim_syndicate"
    points = []
    raw_data: Any = MagicEdenApi.collection_activity(
        collection_symbol=collection_symbol)
    transformed_data: Any = MagicEdenTransformer.collection_activity(
        data=raw_data)
    points += MagicEdenLoader.collection_activity(
        collection_symbol=collection_symbol,
        data=transformed_data)
    assert len(points) > 0
