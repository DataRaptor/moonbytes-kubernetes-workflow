import logging
from typing import List
from flask import jsonify
import pandas as pd
from src.v1.interfaces.influx import (
    InfluxDbInterface
)
from src.v1.interfaces.mongo import (
    MongoDbInterface
)

def v1_query_dataset(
    dataset: str, 
    model: str, 
    measurements: str):
    
    try:
        measurements: List[str] = measurements.split(",")
        
        logging.info("MEASUREMENT: {}".format(measurements))

        if not len(measurements):
            return {
                "ok": False,
                "message": "failed, detected {} ids  measurements".format(
                    len(measurements)
                ),
                "data": None
            }
        df: pd.DataFrame = pd.DataFrame()
        if dataset == "magic_eden":
            df = InfluxDbInterface.get_magic_eden_global_measurements_df(
                model=model,
                measurements=measurements)
            df.set_index("_time", inplace=True)
            df = df[["_measurement", "_value"]]
            df.columns = ["Metric", "Value"]
            df.index.name = "Datetime"
            df.index = list(map(lambda x: str(x), df.index))
        return jsonify({
            "ok": True,
            "message": "success",
            "data": df.to_dict()
        })
    except Exception as e:
        return {
            "ok": False,
            "message": "failed, could not get dataframe - {}".format(e),
            "data": None
        }



def v1_query_dataset_ids(
    dataset: str, 
    model: str, 
    ids: str, 
    measurements: str):
    
    try:
        measurements: List[str] = measurements.split(",")
        ids: List[str] = ids.split(",")
        
        logging.info("MEASUREMENT: {}".format(measurements))
        logging.info("IDS {}".format(ids))

        if not len(measurements) or not len(ids):
            return {
                "ok": False,
                "message": "failed, detected {} ids and {} measurements".format(
                    len(ids),
                    len(measurements)
                ),
                "data": None
            }
        df: pd.DataFrame = pd.DataFrame()
        if dataset == "magic_eden":
            # Dayummmm Son... This is so freaking Yanky needs a refactor at some point...
            if "list" in measurements or "bid" in measurements or "cancelBid" in measurements or "buyNow" in measurements or "delist" in measurements:
                df = MongoDbInterface.get_magic_eden_collections_activity(
                    measurements=measurements,
                    collections=ids)
                if "seller" in df.columns and "buyer" in df.columns:
                    df = df[['created.$date', 'mint', 'price', 'seller', 'buyer']]
                    df.columns = ['created', 'mint', 'price', 'seller', 'buyer']
                elif 'seller' in df.columns:
                    df = df[['created.$date', 'mint', 'price', 'seller']]
                    df.columns = ['created', 'mint', 'price', 'seller']
                elif 'buyer' in df.columns:
                    df = df[['created.$date', 'mint', 'price', 'buyer']]
                    df.columns = ['created', 'mint', 'price', 'buyer']
                else:
                    df = df[['created.$date', 'mint', 'price']]
                    df.columns = ['created', 'mint', 'price']
                df.set_index('created', inplace=True)
                df.index.name = 'Created'
                df.index = list(map(lambda x: str(x), df.index))
            elif "listings" in measurements:
                df = MongoDbInterface.get_magic_eden_collections_listings(
                    measurements=measurements,
                    collections=ids)
                df = df[['created.$date', 'mint', 'price', 'seller', 'token']]
                df.columns = ['created', 'mint', 'price', 'seller', 'token']
                df.set_index('created', inplace=True)
                df.index.name = 'Created'
                df.index = list(map(lambda x: str(x), df.index))
            else:
                df = InfluxDbInterface.get_magic_eden_collections_measurements_df(
                    model=model,
                    measurements=measurements,
                    collections=ids)
                df.set_index("_time", inplace=True)
                df = df[["collection", "_measurement", "_value"]]
                df.columns = ["Collection", "Metric", "Value"]
                df.index.name = "Datetime"
                df.index = list(map(lambda x: str(x), df.index))
        if dataset == "serum":
            df = InfluxDbInterface.get_serum_markets_measurements_df(
                model=model,
                measurements=measurements,
                addresses=ids)
            df.set_index("_time", inplace=True)
            df = df[["address", "_measurement", "_value"]]
            df.columns = ["address", "Metric", "Value"]
            df.index.name = "Datetime"
            df.index = list(map(lambda x: str(x), df.index))
            pass
        return jsonify({
            "ok": True,
            "message": "success",
            "data": df.to_dict()
        })
    except Exception as e:
        return {
            "ok": False,
            "message": "failed, could not get dataframe - {}".format(e),
            "data": None
        }

