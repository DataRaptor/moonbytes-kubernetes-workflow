import logging
from flask import Flask
# from prometheus_flask_exporter import PrometheusMetrics
import mongoengine 
from src.config import (
    LOG_LEVEL,
    MONGO_URL,
    MONGO_DB
)
from src.v1 import routes as v1_routes

app = Flask(__name__)
    # metrics = PrometheusMetrics(app)

app.add_url_rule(
    '/',
    'v1_index',
    methods=['GET'],
    view_func=v1_routes.v1_index
)

app.add_url_rule(
    '/v1/',
    'v1_index',
    methods=['GET'],
    view_func=v1_routes.v1_index
)

app.add_url_rule(
    '/v1/magic_eden/collections', 
    'v1_magic_eden_collections',
    methods=['GET'],
    view_func=v1_routes.v1_magic_eden_collections
)

app.add_url_rule(
    '/v1/serum/markets',
    'v1_serum_markets',
    methods=['GET'],
    view_func=v1_routes.v1_serum_markets
)

app.add_url_rule(
    '/v1/solana/spl_tokens',
    'v1_solana_spl_tokens',
    methods=['GET'],
    view_func=v1_routes.v1_solana_spl_tokens
)

app.add_url_rule(
    '/v1/<dataset>/<model>/<ids>/<measurements>',
    'v1_query_dataset_ids',
    methods=['GET'],
    view_func=v1_routes.v1_query_dataset_ids
)

app.add_url_rule(
    '/v1/<dataset>/<model>/<measurements>',
    'v1_query_dataset',
    methods=['GET'],
    view_func=v1_routes.v1_query_dataset
)



mongoengine.connect(
    db=MONGO_DB,
    host=MONGO_URL)

logging.basicConfig(
    encoding='utf-8',
    level=LOG_LEVEL)


if __name__ == '__main__':
    logging.info('💫 [gargantuan::api] started')
    app.run(debug=True, host='0.0.0.0', port=4200)