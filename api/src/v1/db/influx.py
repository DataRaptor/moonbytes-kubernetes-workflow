import os
import logging
from typing import Any, List
import pandas as pd
from influxdb_client import InfluxDBClient


class InfluxDb:

    HOST: str = os.environ.get("INFLUXDB_HOST")
    TOKEN: str = os.environ.get('INFLUXDB_TOKEN')
    ORG: str = os.environ.get("INFLUXDB_ORG")
    BUCKET: str = os.environ.get("INFLUXDB_BUCKET")

    client = InfluxDBClient(
        url=HOST,
        token=TOKEN,
        org=ORG)

    query_api = client.query_api()

    def query(query: str) -> Any:
        logging.debug("InfluxDb::query_points::{}".format(query))
        tables = InfluxDb.query_api.query(
            query,
            org=InfluxDb.ORG)
        records: List[Any] = []
        for table in tables:
            for record in table.records:
                records.append(record)
        return records

    def query_df(query: str) -> pd.DataFrame:
        logging.debug("InfluxDb::query_df::{}".format(query))
        df = InfluxDb.query_api.query_data_frame(
            query)
        return df
