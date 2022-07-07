from typing import Any
from flask import jsonify
from src.v1.db import mongo

def v1_serum_markets():
    serum_markets: Any = mongo.SerumMarket.objects.all()
    return jsonify({
        "ok": True,
        "data": [
            {
                "address": market.address,
                "base_coingecko_id": market.base_coingecko_id,
                "base_decimals": market.base_decimals,
                "base_icon": market.base_icon,
                "base_mint": market.base_mint,
                "base_symbol": market.base_symbol,
                "base_twitter": market.base_twitter,
                "created": market.created,
                "name": market.name,
                "program_id": market.program_id,
                "quote_coingecko_id": market.quote_coingecko_id,
                "quote_decimals": market.quote_decimals,
                "quote_icon": market.quote_icon,
                "quote_mint": market.quote_mint,
                "quote_symbol": market.quote_symbol,
                "quote_twitter": market.quote_twitter,
                "source": market.source
            } for market in serum_markets
        ]
    })