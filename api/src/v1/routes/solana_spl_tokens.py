from typing import Any
from flask import jsonify
from src.v1.db import mongo

def v1_solana_spl_tokens():
    spl_tokens: Any = mongo.SplToken.objects.all()
    return jsonify({
        "ok": True,
        "data": [
            {
                "symbol": token.symbol,
                "name": token.name,
                "mint": token.mint,
                "extensions": token.extensions,
                "icon": token.icon,
                "decimals": token.decimals,
            } for token in spl_tokens
        ]
    })
