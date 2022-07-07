import json
import logging
from typing import Any
from flask import Flask, request, Response
import mongoengine
from prometheus_flask_exporter import PrometheusMetrics
from src.lib import MagicEdenCollectionXrayETL
from src.config import (
    LOG_LEVEL,
    MONGO_DB,
    MONGO_URL
)

app = Flask(__name__)
metrics = PrometheusMetrics(app)


mongoengine.connect(
    db=MONGO_DB,
    host=MONGO_URL)

logging.basicConfig(
    level=LOG_LEVEL)

@app.route("/", methods=['POST'])
def execute() -> Response:
    collection = request.get_json()
    bad_execution_body: Any = {
        "ok": False,
        "message": "failed",
        "models_written": 0,
        "points_written": 0
    }
    try:
        if "symbol" not in collection:
            bad_execution_body["message"] = "collection_symbol not found in post request"
            return Response(
                response=json.dumps(bad_execution_body), 
                mimetype='application/json',
                status=400)
        collection_symbol: str = collection['symbol']
        etl_execution_body: Any = MagicEdenCollectionXrayETL.execute(
            collection_symbol=collection_symbol)
        return Response(
            response=json.dumps(etl_execution_body), 
            mimetype='application/json',
            status=200)
    except Exception as e:
        logging.error(e)
        bad_execution_body['message'] = str(e)
        return Response(
            response=json.dumps(bad_execution_body), 
            mimetype='application/json',
            status=400)


if __name__ == '__main__':
    logging.info('💫 [gargantuan] magic-eden-collection-etl started')
    app.run(debug=False, host='0.0.0.0', port=4207)
