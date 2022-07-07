import os
import logging
from typing import Any, List
from influxdb_client import Point
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader
from src.db import InfluxDb


class MagicEdenCollectionMarketETL:

    ENABLED: bool = os.environ["ENABLE_ETL_MAGIC_EDEN_COLLECTION_MARKET"] == "true"

    def execute(collection_symbol: str) -> Any:

        if not MagicEdenCollectionMarketETL.ENABLED:
            return {
                "ok": True,
                "message": "disabled",
                "models_written": 0,
                "points_written": 0
            }

        points: List[Point] = []

        try:

            raw_data: Any = MagicEdenApi.collection_metrics(
                collection_symbol=collection_symbol)
            transformed_data: Any = MagicEdenTransformer.collection_metrics(
                data=raw_data)
            points += MagicEdenLoader.collection_metrics(
                collection_symbol=collection_symbol,
                data=transformed_data)

            InfluxDb.write_points(points)
            
            return {
                "ok": True,
                "message": "success",
                "models_written": 0,
                "points_written": len(points)
            }

        except Exception as e:
            return {
                "ok": False,
                "message": str(e),
                "models_written": 0,
                "points_written": 0
            }
