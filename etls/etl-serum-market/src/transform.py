from typing import Any 
from src.utils import safe_get as get


class SolscanTransformer:

    def amm_statistics(data: Any) -> Any:
        data = get(data,'data')
        return {
            "address": get(data, "address"),
            "program_id": get(data, "programId"),
            "base_address": get(get(data, 'base'), 'address'),
            "quote_address": get(get(data, 'quote'), 'address'),
            "base_symbol": get(get(data, 'base'), 'symbol'),
            "quote_symbol": get(get(data, 'quote'), 'symbol'),
            "base_amount": get(data, 'amountBase', cast=float),
            "quote_amount": get(data, 'amountQuote', cast=float),
            "liquidity": get(data, 'liquidity', cast=float),
            "liquidity_pct_change_24h": get(data, 'liquidityChangePercentage24h', cast=float),
            "exchange_rate": get(data, 'price', cast=float),
            "volume_7d": get(data, 'volume7d', cast=float),
            "volume_24hr": get(data, 'volume24h', cast=float),
            "volume_24hr_pct_change_24hr": get(data, 'volume24hChangePercentage24h', cast=float)
        }

    def price_and_volume_usdt(data: Any) -> Any:
        data = get(data, 'data')
        return {
            'price_usdt': get(data, 'priceUsdt', cast=float),
            'volume_usdt': get(data, 'volumeUsdt', cast=float)
        }

class SerumServiceTransformer:


    def market_data(data: Any) -> Any:
        asks, bids = get(data, "asks"), get(data, "bids")
        transformed_asks, transformed_bids = [], []
        for ask in asks:
            transformed_asks.append({
                "price": get(ask, "price", cast=float),
                "size": get(ask, "size", cast=int)
            })
        for bid in bids:
            transformed_bids.append({
                "price": get(bid, "price", cast=float),
                "size": get(bid, "size", cast=int)
            })
        return {
            "midpoint_price": get(data, "midpointPrice", cast=float),
            "best_bid_price": get(data, "bestBidPrice", cast=float),
            "best_ask_price": get(data, "bestAskPrice", cast=float),
            "bid_ask_spread": get(data, "bidAskSpread", cast=float),
            "bid_ask_pct_spread": get(data, "bidAskPctSpread", cast=float),
            "asks": transformed_asks,
            "bids": transformed_bids
        }