import json
import logging
from typing import Any
from flask import Flask, request, Response
from prometheus_flask_exporter import PrometheusMetrics
from src.lib import SerumMarketETL
from src.config import LOG_LEVEL

app = Flask(__name__)
metrics = PrometheusMetrics(app)

logging.basicConfig(
    level=LOG_LEVEL)

@app.route("/", methods=['POST'])
def execute() -> Response:
    data: Any = request.get_json()
    bad_execution_body: Any = {
        "ok": False,
        "message": "failed",
        "models_written": 0,
        "points_written": 0
        }
    try:
        for key in [
            "address",
            "program_id",
            "base_symbol",
            "quote_symbol"]:
            if key not in data:
                bad_execution_body['message'] = "address not found in post request"
                return Response(
                    response=json.dumps(bad_execution_body), 
                    mimetype='application/json',
                    status=400)
        address: str = data["address"]
        program_id: str = data['program_id']
        base_symbol: str = data['base_symbol']
        quote_symbol: str = data['quote_symbol']
        etl_execution_body: Any = SerumMarketETL.execute(
            address=address,
            program_id=program_id,
            base_symbol=base_symbol,
            quote_symbol=quote_symbol)
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
    host = '0.0.0.0'
    port = 4205
    logging.info('💫 [gradient-gargantuan::etl-serum-market started on {}:{}'.format(
        host,
        port))
    app.run(debug=False, host=host, port=port)

