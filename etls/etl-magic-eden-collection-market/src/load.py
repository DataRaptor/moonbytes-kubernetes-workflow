import datetime
from typing import Any, List
from influxdb_client import Point, WritePrecision


class MagicEdenLoader:

    def collection_metrics(collection_symbol: str, data: Any) -> List[Point]:
        points: List[Point] = []
        for metric_name in [
            "volume_all",
            "volume_24hr",
            "listed_count",
            "price_average_24hr",
                "price_floor"]:

            if data[metric_name]:
                point = Point(metric_name) \
                    .tag("dataset", "magic_eden") \
                    .tag("model", "markets") \
                    .tag("collection", collection_symbol) \
                    .field("value", float(data[metric_name])) \
                    .time(datetime.datetime.utcnow(), WritePrecision.NS)
                points.append(point)

        for attribute in data['attributes']:
            point = Point("price_floor") \
                .tag("dataset", "magic_eden") \
                .tag("model", "attributes") \
                .tag("collection", collection_symbol) \
                .tag("trait_type", attribute["trait_type"]) \
                .tag("trait_value", attribute["value"]) \
                .field("value", float(attribute["price_floor"])) \
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

            point = Point("listed_count") \
                .tag("dataset", "magic_eden") \
                .tag("model", "attributes") \
                .tag("collection", collection_symbol) \
                .tag("trait_type", attribute["trait_type"]) \
                .tag("trait_value", attribute["value"]) \
                .field("value", float(attribute["listed_count"])) \
                .time(datetime.datetime.utcnow(), WritePrecision.NS)
            points.append(point)

        return points
