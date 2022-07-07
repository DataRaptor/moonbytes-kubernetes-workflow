import logging
import pandas as pd
from src.v1.db.influx import InfluxDb
from typing import List

class InfluxDbInterface:

    def get_magic_eden_global_measurements_df(
        model: str,
        measurements: List[str] = [],
        start: str = "-30d",
        end: str = "now()",
        interval: str = "1m") -> pd.DataFrame:

        dataset: str = "magic_eden"

        df: pd.DataFrame = None

        query: str = 'from(bucket: "{}")'.format(InfluxDb.BUCKET)
        query += ' |> range(start: {}, stop: {})'.format(
            start,
            end)
        query += ' |> filter(fn: (r) => r["dataset"] == "{}")'.format(dataset)
        query += ' |> filter(fn: (r) => r["model"] == "{}")'.format(model)

        if measurements:
            if len(measurements) == 1:
                query += ' |> filter(fn: (r) => r["_measurement"] == "{}") '.format(
                    measurements[0])
            else:
                sub_query: str = ' |> filter(fn: (r) => '
                for i, measurement in enumerate(measurements):
                    if i == len(measurements) - 1:
                        sub_query += ' r["_measurement"] == "{}" )'.format(
                            measurement)
                    else:
                        sub_query += ' r["_measurement"] == "{}" or'.format(
                            measurement)
                query += sub_query

        query += ' |> filter(fn: (r) => r["_field"] == "value")'
        query += ' |> aggregateWindow(every: {}, fn: mean, createEmpty: false)'.format(
            interval)
        query += ' |> yield(name: "mean")'
        logging.info(query)
        df = InfluxDb.query_df(query)
        return df


    def get_magic_eden_collections_measurements_df(
            model: str,
            measurements: List[str] = [],
            collections: List[str] = [],
            start: str = "-30d",
            end: str = "now()",
            interval: str = "1m") -> pd.DataFrame:

        dataset: str = "magic_eden"

        df: pd.DataFrame = None

        query: str = 'from(bucket: "{}")'.format(InfluxDb.BUCKET)
        query += ' |> range(start: {}, stop: {})'.format(
            start,
            end)
        query += ' |> filter(fn: (r) => r["dataset"] == "{}")'.format(dataset)
        query += ' |> filter(fn: (r) => r["model"] == "{}")'.format(model)

        if measurements:
            if len(measurements) == 1:
                query += ' |> filter(fn: (r) => r["_measurement"] == "{}") '.format(
                    measurements[0])
            else:
                sub_query: str = ' |> filter(fn: (r) => '
                for i, measurement in enumerate(measurements):
                    if i == len(measurements) - 1:
                        sub_query += ' r["_measurement"] == "{}" )'.format(
                            measurement)
                    else:
                        sub_query += ' r["_measurement"] == "{}" or'.format(
                            measurement)
                query += sub_query

        if collections:
            if len(collections) == 1:
                query += ' |> filter(fn: (r) => r["collection"] == "{}") '.format(
                    collections[0])
            else:
                sub_query: str = ' |> filter(fn: (r) => '
                for i, collection in enumerate(collections):
                    if i == len(collections) - 1:
                        sub_query += ' r["collection"] == "{}" )'.format(
                            collection)
                    else:
                        sub_query += ' r["collection"] == "{}" or'.format(
                            collection)
                query += sub_query
        query += ' |> filter(fn: (r) => r["_field"] == "value")'
        query += ' |> aggregateWindow(every: {}, fn: mean, createEmpty: false)'.format(
            interval)
        query += ' |> yield(name: "mean")'
        logging.info(query)
        df = InfluxDb.query_df(query)
        return df

    def get_serum_markets_measurements_df(
            model: str,
            measurements: str = [],
            addresses: str = [],
            start: str = "-30d",
            end: str = "now()",
            interval: str = "1m") -> pd.DataFrame:

        dataset: str = "serum"

        df: pd.DataFrame = None

        query: str = 'from(bucket: "{}")'.format(InfluxDb.BUCKET)
        query += ' |> range(start: {}, stop: {})'.format(
            start,
            end)
        query += ' |> filter(fn: (r) => r["dataset"] == "{}")'.format(dataset)
        query += ' |> filter(fn: (r) => r["model"] == "{}")'.format(model)

        if measurements:
            if len(measurements) == 1:
                query += ' |> filter(fn: (r) => r["_measurement"] == "{}") '.format(
                    measurements[0])
            else:
                sub_query: str = ' |> filter(fn: (r) => '
                for i, measurement in enumerate(measurements):
                    if i == len(measurements) - 1:
                        sub_query += ' r["_measurement"] == "{}" )'.format(
                            measurement)
                    else:
                        sub_query += ' r["_measurement"] == "{}" or'.format(
                            measurement)
                query += sub_query

        if addresses:
            if len(addresses) == 1:
                query += ' |> filter(fn: (r) => r["address"] == "{}") '.format(
                    addresses[0])
            else:
                sub_query: str = ' |> filter(fn: (r) => '
                for i, collection in enumerate(addresses):
                    if i == len(addresses) - 1:
                        sub_query += ' r["address"] == "{}" )'.format(
                            collection)
                    else:
                        sub_query += ' r["address"] == "{}" or'.format(
                            collection)
                query += sub_query
        query += ' |> filter(fn: (r) => r["_field"] == "value")'
        query += ' |> aggregateWindow(every: {}, fn: mean, createEmpty: false)'.format(
            interval)
        query += ' |> yield(name: "mean")'
        logging.info(query)
        df = InfluxDb.query_df(query)
        return df
