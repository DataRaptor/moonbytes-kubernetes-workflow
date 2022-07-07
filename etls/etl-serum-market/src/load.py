import datetime 
from typing import Any, List
from src.utils import safe_cast as cast
from influxdb_client import Point, WritePrecision

class SolscanLoader:

    def amm_statistics(
        market_address: str,
        program_id: str,
        base_symbol: str,
        quote_symbol: str,
        data: Any) -> List[Point]:
        points: List[Point] = []

        point = Point("base_amount") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", cast(data['base_amount'], float)) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("quote_amount") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["quote_amount"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("liquidity") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["liquidity"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("liquidity_pct_change_24h") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["liquidity"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_7d") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["volume_7d"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_24hr") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["volume_24hr"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_24hr_pct_change_24hr") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["volume_24hr_pct_change_24hr"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        return points

    def price_and_volume_usdt(
        market_address: str, 
        program_id: str,
        base_symbol: str,
        quote_symbol: str,
        data: Any) -> List[Point]:
        points: List[Point] = []
                
        point = Point("price_usdt") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["price_usdt"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_usdt") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", "markets") \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["volume_usdt"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        return points


class SerumServiceLoader:


    def market_data(
        market_address: str,
        program_id: str,
        base_symbol: str,
        quote_symbol: str,
        data: Any) -> List[Point]:

        points: List[Point] = []

        point = Point("midpoint_price") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["midpoint_price"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("best_bid_price") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["best_bid_price"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("best_ask_price") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["best_ask_price"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("bid_ask_spread") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["bid_ask_spread"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)
        
        point = Point("bid_ask_pct_spread") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["bid_ask_pct_spread"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("best_ask_price") \
            .tag("dataset", "serum") \
            .tag("model", "markets") \
            .tag("address", market_address) \
            .tag("program_id", program_id) \
            .tag("base_symbol", base_symbol) \
            .tag("quote_symbol", quote_symbol) \
            .field("value", data["best_ask_price"]) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)


        time = datetime.datetime.utcnow()
        for ask in data["asks"]:
            point = Point("price") \
                .tag("dataset", "serum") \
                .tag("model", "orderbook") \
                .tag("address", market_address) \
                .tag("program_id", program_id) \
                .tag("base_symbol", base_symbol) \
                .tag("quote_symbol", quote_symbol) \
                .tag("side", "ask") \
                .field("value", ask["price"]) \
                .time(time, WritePrecision.NS)
            points.append(point)
            point = Point("size") \
                .tag("dataset", "serum") \
                .tag("model", "orderbook") \
                .tag("address", market_address) \
                .tag("program_id", program_id) \
                .tag("base_symbol", base_symbol) \
                .tag("quote_symbol", quote_symbol) \
                .tag("side", "ask") \
                .field("value", ask["size"]) \
                .time(time, WritePrecision.NS)
            points.append(point)

        for bid in data["bids"]:
            point = Point("price") \
                .tag("dataset", "serum") \
                .tag("model", "orderbook") \
                .tag("address", market_address) \
                .tag("program_id", program_id) \
                .tag("base_symbol", base_symbol) \
                .tag("quote_symbol", quote_symbol) \
                .tag("side", "bid") \
                .field("value", bid["price"]) \
                .time(time, WritePrecision.NS)
            points.append(point)
            point = Point("size") \
                .tag("dataset", "serum") \
                .tag("model", "orderbook") \
                .tag("address", market_address) \
                .tag("program_id", program_id) \
                .tag("base_symbol", base_symbol) \
                .tag("quote_symbol", quote_symbol) \
                .tag("side", "bid") \
                .field("value", bid["size"]) \
                .time(time, WritePrecision.NS)
            points.append(point)

        return points
