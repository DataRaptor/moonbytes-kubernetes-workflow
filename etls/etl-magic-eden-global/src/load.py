import datetime
from typing import Any, List
from influxdb_client import Point, WritePrecision


class MagicEdenLoader:

    def volume(data: Any) -> List[Point]:
        points: List[Point] = []

        point = Point("volume_total") \
            .tag("dataset", "magic_eden") \
            .tag("model", "global") \
            .field("value", float(data["total"])) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_24hr") \
            .tag("dataset", "magic_eden") \
            .tag("model", "global") \
            .field("value", float(data["24hr"])) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_7d") \
            .tag("dataset", "magic_eden") \
            .tag("model", "global") \
            .field("value", float(data["7d"])) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        point = Point("volume_30d") \
            .tag("dataset", "magic_eden") \
            .tag("model", "global") \
            .field("value", float(data["30d"])) \
            .time(datetime.datetime.utcnow(), WritePrecision.NS)
        points.append(point)

        return points
