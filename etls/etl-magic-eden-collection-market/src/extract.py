from typing import Any, List
import logging
import requests
from src.transport import http_client
from requests import Response
# import twitter
from src.utils import lamports_to_sol


class MagicEdenApi:

    RPC_API_URL: str = "https://api-mainnet.magiceden.io"
    HEADERS: Any = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Connection': 'close'
    }

    def collection_metrics(collection_symbol: str) -> Any:
        url: str = "{}/rpc/getCollectionEscrowStats/{}?edge_cache=true".format(
            MagicEdenApi.RPC_API_URL,
            collection_symbol)
        # logging.trace('MagicEdenApi::Get::{}'.format(url))
        response: Response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data
