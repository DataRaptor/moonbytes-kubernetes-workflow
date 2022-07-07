import os
import logging
from typing import Any, List
from influxdb_client import Point
from src.extract import (
    SolscanApi,
    SolanaBlockExplorerApi,
    CoinGeckoApi
)
from src.transform import (
    SolscanTransformer,
    SolanaBlockExplorerTransformer,
    CoinGeckoTransformer
)
from src.load import (
    SolscanLoader,
    SolanaBlockExplorerLoader,
    CoinGeckoLoader
)
from src.db import InfluxDb


class SolanaGlobalETL:

    ENABLED: bool = os.environ["ENABLE_ETL_SOLANA_GLOBAL"] == "true"

    def execute():

        if not SolanaGlobalETL.ENABLED:
            return {
                "ok": True,
                "message": "disabled",
                "points_written": 0,
                "models_written": 0
            }

        points: List[Point] = []

        try:

            # Solana Block Explorer Jobs
            raw_data: Any = SolanaBlockExplorerApi.supply()
            transformed_data: Any = SolanaBlockExplorerTransformer.supply(
                data=raw_data)
            points += SolanaBlockExplorerLoader.supply(
                data=transformed_data)
            
            raw_data: Any = SolanaBlockExplorerApi.epoch_info()
            transformed_data: Any = SolanaBlockExplorerTransformer.epoch_info(
                data=raw_data)
            points += SolanaBlockExplorerLoader.epoch_info(
                data=transformed_data)
            
            # Coingecko Jobs
            raw_data: Any = CoinGeckoApi.token_info()
            transformed_data: Any = CoinGeckoTransformer.token_info(
                data=raw_data)
            points += CoinGeckoLoader.token_info(
                data=transformed_data)
        
            # solscan Jobs
            raw_data: Any = SolscanApi.price_and_volume_usdt(
                symbol='SOL')
            transformed_data: Any = SolscanTransformer.price_and_volume_usdt(
                data=raw_data)
            points += SolscanLoader.price_and_volume_usdt(
                data=transformed_data)

            # Write Points To Influx
            InfluxDb.write_points(points)

            return {
                "ok": True,
                "message": "success",
                "points_written": len(points),
                "models_written": 0
            }

        except Exception as e:
            logging.error("Error: {}".format(e))
            return {
                "ok": False,
                "message": str(e),
                "points_written": 0,
                "models_written": 0
            }