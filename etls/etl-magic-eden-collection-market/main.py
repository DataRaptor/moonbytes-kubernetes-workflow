import json
import logging
from typing import Any
from flask import Flask, request, Response
from prometheus_flask_exporter import PrometheusMetrics
from src.lib import MagicEdenCollectionMarketETL
from src.utils import extract_collection_symbol
from src.config import (
    LOG_LEVEL
)

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=LOG_LEVEL)

@app.route("/", methods=['POST'])
def execute() -> Response:
    collection = request.get_json()
    bad_execution_body: Any = {
        "ok": False,
        "message": "failed",
        "models_written": 0,
        "points_written": 0}
    if "symbol" not in collection:
        bad_execution_body['message'] = "symbol not found in post request"
        return Response(
            response=json.dumps(bad_execution_body), 
            mimetype="application/json",
            status=400)
    collection_symbol: str = collection['symbol']
    try:
        etl_execution_body: Any = MagicEdenCollectionMarketETL.execute(
            collection_symbol=collection_symbol)
        return Response(
            response=json.dumps(etl_execution_body), 
            mimetype='application/json',
            status=200)
    except Exception as e:
        bad_execution_body['message'] = str(e)
        return Response(
            response=json.dumps(bad_execution_body), 
            mimetype='application/json',
            status=400)


if __name__ == '__main__':
    HOST: str = '0.0.0.0'
    PORT: int = 4208
    logging.info('💫 [project_l] magic_eden_collection_etl started')
    app.run(
        debug=False, 
        host=HOST, 
        port=PORT)
