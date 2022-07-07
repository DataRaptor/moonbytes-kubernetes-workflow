import os
from typing import Any
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader


def test_job():
    points = []
    raw_data: Any = MagicEdenApi.volume()
    transformed_data: Any = MagicEdenTransformer.volume(
        data=raw_data)
    points += MagicEdenLoader.volume(
        data=transformed_data)
    assert len(points) > 0
