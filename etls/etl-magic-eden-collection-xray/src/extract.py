import random
import json
import os
from typing import Any, List
import logging
import requests
from requests import Response
from src.transport import http_client
# import twitter
from src.utils import (
    load_user_agents,
)


class MagicEdenApi:

    USER_AGENTS: List[str] = load_user_agents()
    RPC_API_URL: str = "https://api-mainnet.magiceden.io"
    PUBLIC_API_URL: str = "https://api-mainnet.magiceden.dev/v2"
    HEADERS: Any = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Connection': 'close'
    }
    LIMIT: int = 20
    MAX_OFFSET: int = 21

    def collection_metrics(collection_symbol: str) -> Any:
        url: str = "{}/rpc/getCollectionEscrowStats/{}?edge_cache=true".format(
            MagicEdenApi.RPC_API_URL,
            collection_symbol)
        # logging.info('MagicEdenApi::Get::{}'.format(url))
        headers = MagicEdenApi.HEADERS
        headers["User-Agent"] = random.choice(MagicEdenApi.USER_AGENTS)
        response: Response = http_client.get(
            url,
            headers=headers)
        data: Any = response.json()
        return data

    def _get_collection_listings(
            collection_symbol: str,
            offset: int = 0,
            limit: int = 20) -> Any:
        url: str = "{}/collections/{}/listings?offset={}&limit={}".format(
            MagicEdenApi.PUBLIC_API_URL,
            collection_symbol,
            offset,
            limit)
        headers = MagicEdenApi.HEADERS
        headers["User-Agent"] = random.choice(MagicEdenApi.USER_AGENTS)
        # logging.info('MagicEdenApi::Get::{}'.format(url))
        response: Response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data

    def _get_collection_activity(
            collection_symbol: str,
            offset: int = 0,
            limit: int = 20) -> Any:
        url = "{}/collections/{}/activities?offset={}&limit={}".format(
            MagicEdenApi.PUBLIC_API_URL,
            collection_symbol,
            offset,
            limit)
        headers = MagicEdenApi.HEADERS
        headers["User-Agent"] = random.choice(MagicEdenApi.USER_AGENTS)
        # logging.info('MagicEdenApi::Get::{}'.format(url))
        response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data

    def collection_activity(collection_symbol: str) -> List[Any]:
        offset: int = 0
        collection_activities_bundle: List[Any] = []
        while offset < MagicEdenApi.MAX_OFFSET:
            collection_activities: List[Any] = MagicEdenApi._get_collection_activity(
                collection_symbol=collection_symbol,
                offset=offset,
                limit=MagicEdenApi.LIMIT)
            collection_activities_bundle += collection_activities
            offset += MagicEdenApi.LIMIT
        return collection_activities_bundle

    def collection_listings(collection_symbol: str, max_listings: int) -> List[Any]:
        offset: int = 0
        collection_listings_bundle: List[Any] = []
        while offset < max_listings:
            collection_listings: List[Any] = MagicEdenApi._get_collection_listings(
                collection_symbol=collection_symbol,
                offset=offset,
                limit=MagicEdenApi.LIMIT)
            collection_listings_bundle += collection_listings
            offset += MagicEdenApi.LIMIT
        return collection_listings_bundle


# class TwitterApi:

#     CONSUMER_KEY: str = "H6621iKuL4x0rISBtecFZycMf"
#     CONSUMER_SECRET: str = "sKQ9cYUf7ngx9ZsUXopSvDvqnXlUc08u5lDQmvU84EX99pH8k1"
#     ACCESS_TOKEN_KEY: str = "1507127205675114503-95OGnIWSPNdBExOzX9tSmg3hGWpkbf"
#     ACCESS_TOKEN_SECRET: str = "5nEsqejvdezqcCVEsph1YAGFjqy9laur6mGaufxu0yIJp"

#     client = twitter.Api(
#         consumer_key=CONSUMER_KEY,
#         consumer_secret=CONSUMER_SECRET,
#         access_token_key=ACCESS_TOKEN_KEY,
#         access_token_secret=ACCESS_TOKEN_SECRET)

#     def user_metrics(screen_name: str) -> Any:
#         pass
