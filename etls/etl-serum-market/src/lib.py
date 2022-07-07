import logging
import os
from typing import Any, List
from influxdb_client import Point
from src.db import InfluxDb
from src.extract import (
    SolscanApi,
    SerumServiceApi
)
from src.transform import (
    SolscanTransformer,
    SerumServiceTransformer
)
from src.load import (
    SolscanLoader,
    SerumServiceLoader
)


class SerumMarketETL:

    ENABLED: bool = os.environ["ENABLE_ETL_SERUM_MARKET"] == "true"

    def execute(
        address: str,
        program_id: str,
        base_symbol: str,
        quote_symbol: str):

        if not SerumMarketETL.ENABLED:
            return {
                "ok": True,
                "message": "disabled",
                "models_written": 0,
                "points_written": 0
            }

        points: List[Point] = []

        # try:
        # This one would be nice (ie: The chunk of commented code) 
        # but it seems like we get rate limited to oblivion with solscan so 
        # this might need to remove this for now. Oh well.. What a nice
        # dataset. But maybe we can reconsutruct it or include it
        # when we can hack rate limiting. 
        # 
        #
        # Serum Solscan Amm Statistics Job
        # raw_data: Any = SolscanApi.amm_statistics(address)
        # transformed_data: Any = SolscanTransformer.amm_statistics(
        #     data=raw_data)
        # base_symbol: str = transformed_data["base_symbol"]
        # quote_symbol: str = transformed_data["quote_symbol"]
        # program_id: str = transformed_data['program_id']
        # points += SolscanLoader.amm_statistics(
        #     market_address=address,
        #     program_id=program_id,
        #     base_symbol=base_symbol,
        #     quote_symbol=quote_symbol,
        #     data=transformed_data)


        # So like the commented code would be nice too. However this 
        # is probably not the right place to get spl-token data. It should
        # be in the regular spl-token etl... Probably don't wanna grab this
        # from solscan though... Hmmm Tbh, the X-USDC pair might be the best
        # way to go. I think we have some breathing room with the serum service.

        # Serum Solscan Price and Volume USDT Jobs
        # Base Token SubJob
        # raw_data: Any = SolscanApi.price_and_volume_usdt(base_symbol)
        # transformed_data: Any = SolscanTransformer.price_and_volume_usdt(
        #     data=raw_data)
        # points += SolscanLoader.price_and_volume_usdt(
        #     market_address=market_address,
        #     program_id=program_id,
        #     base_symbol=base_symbol,
        #     quote_symbol=quote_symbol,
        #     data=transformed_data)

        # ## Quote Token SubJob
        # raw_data: Any = SolscanApi.price_and_volume_usdt(quote_symbol)
        # transformed_data: Any = SolscanTransformer.price_and_volume_usdt(
        #     data=raw_data)
        # points += SolscanLoader.price_and_volume_usdt(
        #     market_address=market_address,
        #     program_id=program_id,
        #     base_symbol=base_symbol,
        #     quote_symbol=quote_symbol,
        #     data=transformed_data)

        # On Chain Serum Service Job
        raw_data: Any = SerumServiceApi.market_data(
            market_address=address,
            program_id=program_id,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol)
        transformed_data: Any = SerumServiceTransformer.market_data(
            data=raw_data)
        points += SerumServiceLoader.market_data(
            market_address=address,
            program_id=program_id,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol,
            data=transformed_data)

        InfluxDb.write_points(points)


        return {
            "ok": True,
            "message": "success",
            "points_written": len(points),
            "models_written": 0
        }

        # except Exception as e:
        #     return {
        #         "ok": False,
        #         "message": str(e),
        #         "points_written": 0,
        #         "models_written": 0
        #     }
