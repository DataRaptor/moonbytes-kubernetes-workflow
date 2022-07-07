import pandas as pd
from typing import List 
import requests

API_URL: str = "http://api:8080"
API_VERSION: str = "v1"

def get_magic_eden_collections():
    url: str = "{}/{}/magic_eden/collections".format(
        API_URL,
        API_VERSION)
    response = requests.get(
        url,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        # logging.info('[get_magic_eden_collections] >>> {}'.format(response.json()))
        return response.json()['data']
    raise Exception('Could not get magic eden collections - {}'.format(
        response.content
    ))


def get_serum_markets():
    url: str = "{}/{}/serum/markets".format(
        API_URL,
        API_VERSION)
    response = requests.get(
        url,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        return response.json()['data']
    raise Exception('Could not get serum markets - {}'.format(
        response.content
    ))

def get_solana_tokens():
    url: str = "{}/{}/solana/tokens".format(
        API_URL,
        API_VERSION)
    response = requests.get(
        url,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        return response.json()['data']
    raise Exception('Could not get solana spl tokens - {}'.format(
        response.content
    ))


def get_df(
    dataset: str,
    model: str,
    ids: List[str],
    measurements: List[str]
):
    url: str = "{}/{}/{}/{}/{}/{}".format(
        API_URL,
        API_VERSION,
        dataset,
        model,
        ",".join(ids),
        ",".join(measurements)
    )
    response = requests.get(
        url,
        headers={'Content-Type': 'application/json'}
    )
    if response.status_code == 200:
        return pd.DataFrame(response.json()['data'])
    raise Exception("Could not get df for dataset: {}, model: {}, ids: {}, measurements: {}".format(
        dataset,
        model,
        ids,
        measurements
    ))










