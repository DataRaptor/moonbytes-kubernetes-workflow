import os
import logging
from typing import Any, List
from influxdb_client import Point
from src.extract import MagicEdenApi
from src.transform import MagicEdenTransformer
from src.load import MagicEdenLoader
from src.db import InfluxDb


class MagicEdenGlobalETL:

    ENABLED: bool = os.environ["ENABLE_ETL_MAGIC_EDEN_GLOBAL"] == "true"

    def execute():

        if not MagicEdenGlobalETL.ENABLED:
            return {
                "ok": True,
                "message": "disabled",
                "models_written": 0,
                "points_written": 0
            }

        points: List[Point] = []

        try:

            # Magic Eden Global Volume Job
            raw_data: Any = MagicEdenApi.volume()
            transformed_data: Any = MagicEdenTransformer.volume(
                data=raw_data)
            points += MagicEdenLoader.volume(
                data=transformed_data)

            # logging.info("Num Points: {}".format(len(points)))

            # Write Points To Influx
            InfluxDb.write_points(points)

            return {
                "ok": True,
                "message": "success",
                "points_written": len(points),
                "models_written": 0
            }

        except Exception as e:
            return {
                "ok": False,
                "message": str(e),
                "points_written": 0,
                "models_written": 0
            }
