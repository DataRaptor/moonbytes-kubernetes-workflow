import time
import logging
from typing import Any, List
from flask import Flask, jsonify
from prometheus_flask_exporter import PrometheusMetrics
import mongoengine
from src.db import MongoDb
from src.jobs.extract import (
    RaydiumApi,
    SolscanApi,
    MagicEdenApi
)
from src.jobs.transform import ( 
    RaydiumTransformer,
    SolscanTransformer,
    MagicEdenTransformer
)
from src.jobs.load import (
    MagicEdenLoader,
    RaydiumLoader,
    SolscanLoader,
)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

MONGO_DB: str = "gradient-gargantuan"
MONGO_URL: str = "mongodb://root:rootpassword@mongodb:27017/gradient-gargantuan?ssl=false&authSource=admin"

@app.route('/turbine/magic_eden/collections/update', methods=['POST'])
def update_magic_eden_collections():
    models: List[MongoDb.MagicEdenCollection] = []

    raw_data: Any = MagicEdenApi.collections()
    transformed_data: Any = MagicEdenTransformer.collections(
        data=raw_data)
    models += MagicEdenLoader.collections(
        data=transformed_data)
    success: bool = MongoDb.write_models(models)

    return jsonify({
        "ok": success,
        "message": "success" if success else "failed"
    })


@app.route("/turbine/solana/tokens/update", methods=["POST"])
def update_solana_tokens():
    models: List[MongoDb.SplToken] = []

    # Right now we just grab the tokens from Raydium
    # in the future we want to expand this token_list
    # to other sensible choices. A unsensible update source
    # would be the solana token list. It is unreasonable
    # because it contains several thousand tokens, much of
    # which aren't tradable (either due to liquidity constraints
    # or the lack of existence of markets). Reasonable update
    # sources would be Jupyter Labs, Wormhole token list, Orca and FTX.

    raw_data: Any = RaydiumApi.token_list()
    transformed_data: Any = RaydiumTransformer.token_list(
        data=raw_data)
    models += RaydiumLoader.token_list(
        data=transformed_data)
    success: bool = MongoDb.write_models(models)

    return jsonify({
        "ok": success,
        "message": "success" if success else "failed"
    })


@app.route("/turbine/serum/markets/update", methods=['POST'])
def update_serum_markets():
    models: List[MongoDb.SerumMarket] = []

    existing_spl_token_mints: List[str] = list(map(
        lambda spl_token: spl_token.mint,
        MongoDb.SplToken.objects.all()
    ))

    for mint in existing_spl_token_mints:
        try:
            raw_data: Any = SolscanApi.markets_from_mint(
                mint=mint)
            transformed_data: Any = SolscanTransformer.markets_from_mint(
                data=raw_data)
            models += SolscanLoader.markets_from_mint(
                data=transformed_data)
            # logging.info("Got Market from mint: {}".format(mint))
        except Exception as e:
            logging.error("Could not get Raydium token - {} - {}".format(
                mint,
                e
            ))
            pass
        # we want to add some delay here so that Solscan doesn't get mad at us.
        time.sleep(0.3)
    success: bool = MongoDb.write_models(models)
    return jsonify({
        "ok": success,
        "message": "success" if success else "failed"
    })


@app.route("/turbine/magic_eden/collections", methods=['GET'])
def turbine_get_magic_eden_collections():
    magic_eden_collections: Any = MongoDb.MagicEdenCollection.objects.order_by(
        '-volume_all')
    return jsonify({
        "ok": True if len(magic_eden_collections) > 0 else False,
        "data": [
            {
                "symbol": collection.symbol,
                "volume_all": collection.volume_all,
                "twitter": collection.twitter
            } for collection in magic_eden_collections
        ]
    })


@app.route("/turbine/serum/markets", methods=["GET"])
def turbine_get_serum_markets():
    serum_markets: Any = MongoDb.SerumMarket.objects.all()
    return jsonify({
        "ok": True,
        "data": [
            {
                "address": market.address,
                "program_id": market.program_id,
                "base_symbol": market.base_symbol,
                "quote_symbol": market.quote_symbol
            } for market in serum_markets
        ]
    })


@app.route("/turbine/solana/tokens", methods=["GET"])
def turbine_get_solana_tokens():
    spl_tokens: Any = MongoDb.SplToken.objects.all()
    return jsonify({
        "ok": True,
        "data": [
            {
                "symbol": token.symbol,
                "mint": token.mint,
            } for token in spl_tokens
        ]
    })


mongoengine.connect(
    db=MONGO_DB,
    host=MONGO_URL)

logging.basicConfig(
    encoding='utf-8',
    level=logging.INFO)

if __name__ == '__main__':
    print('💫 [gradient-gargantuan::state] started')
    app.run(debug=True, host='0.0.0.0', port=4202)
