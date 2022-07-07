import json
import logging
from typing import Any
from flask import Flask, request, Response
from prometheus_flask_exporter import PrometheusMetrics
from src.lib import SolanaGlobalETL
from src.config import LOG_LEVEL

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=LOG_LEVEL)

@app.route("/", methods=['POST'])
def execute() -> Response:
    logging.info(">>>>> SOLANA GLOBAL ETL STARTED")
    _data = request.get_json()
    bad_execution_body: Any = {
        "ok": False,
        "message": "failed",
        "models_written": 0,
        "points_written": 0
    }
    try:
        etl_execution_body: Any = SolanaGlobalETL.execute()
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
    logging.info('💫 [gradient-gargantuan::etl-solana-global] started')
    app.run(debug=False, host='0.0.0.0', port=4204)
