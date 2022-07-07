import os
import time
import logging
from typing import Any, List
from influxdb_client import Point
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader
from src.db import InfluxDb
from src.db import mongo


class MagicEdenCollectionXrayETL:

    ENABLED: bool = os.environ["ENABLE_ETL_MAGIC_EDEN_COLLECTION_XRAY"] == "true"

    def execute(collection_symbol: str):

        if not MagicEdenCollectionXrayETL.ENABLED:
            return {
                "ok": True,
                "message": "disabled",
                "models_written": 0,
                "points_written": 0
            }

        models: List[Any] = []
        points: List[Point] = []

        # try:

        raw_data: Any = MagicEdenApi.collection_metrics(
            collection_symbol=collection_symbol)
        transformed_data: Any = MagicEdenTransformer.collection_metrics(
            data=raw_data)

        max_listings: int = transformed_data['listed_count']
        max_listings = max_listings if max_listings else 100

        time.sleep(0.5)

        raw_data: Any = MagicEdenApi.collection_activity(
            collection_symbol=collection_symbol)
        transformed_data: Any = MagicEdenTransformer.collection_activity(
            data=raw_data)
        models += MagicEdenLoader.collection_activity(
            collection_symbol=collection_symbol,
            data=transformed_data)

        time.sleep(0.5)

        raw_data: Any = MagicEdenApi.collection_listings(
            collection_symbol=collection_symbol,
            max_listings=max_listings)
        transformed_data: Any = MagicEdenTransformer.collection_listings(
            data=raw_data)
        models += MagicEdenLoader.collection_listings(
            collection_symbol=collection_symbol,
            data=transformed_data)

        InfluxDb.write_points(points)
        mongo.write_models(models)

        return {
            "ok": True,
            "message": "success",
            "models_written": len(models),
            "points_written": len(points)
        }

        # except Exception as e:
        #     return {
        #         "ok": False,
        #         "message": str(e),
        #         "models_written": 0,
        #         "points_written": 0
        #     }
