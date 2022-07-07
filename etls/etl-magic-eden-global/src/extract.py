from typing import Any, List
import logging
from src.transport import http_client
import requests
from requests import Response


class MagicEdenApi:

    RPC_API_URL: str = "https://api-mainnet.magiceden.io"
    HEADERS: Any = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def volume():
        url = "{}/volumes?edge_cache=false".format(MagicEdenApi.RPC_API_URL)
        # logging.info('MagicEdenApi::Get::{}'.format(url))
        response: Response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data
