from typing import Any, List
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS
from src.config import (
    INFLUX_HOST,
    INFLUX_TOKEN,
    INFLUX_ORG,
    INFLUX_BUCKET
)

class InfluxDb:

    client = InfluxDBClient(
        url=INFLUX_HOST,
        token=INFLUX_TOKEN,
        org=INFLUX_ORG)

    write_api = client.write_api(
        write_options=SYNCHRONOUS)

    def write_points(points: List[Point]) -> Any:
        return InfluxDb.write_api.write(
            bucket=INFLUX_BUCKET,
            record=points)
