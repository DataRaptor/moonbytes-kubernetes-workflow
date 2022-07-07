from typing import Any, List
import logging
import requests
from requests import Response
from src.transport import http_client
from src.utils import generate_uuid4


class CoinGeckoApi:

    API_URL: str = "https://api.coingecko.com/api/v3"
    HEADERS: Any = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

    def token_info(coingecko_name: str = 'solana') -> Any:
        url: str = "{}/coins/{}?".format(
            CoinGeckoApi.API_URL,
            coingecko_name)
        response = http_client.get(
            url,
            headers=CoinGeckoApi.HEADERS)
        if response.status_code == 200:
            return response.json()
        raise Exception("Could not get coingecko information")

class SolanaBlockExplorerApi:

    API_URL: str = "https://explorer-api.mainnet-beta.solana.com/"
    HEADERS: Any = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

    def supply() -> Any:
        data: Any = {
            "id": generate_uuid4(),
            "method": "getSupply",
            "jsonrpc": "2.0",
            "params": [
                {
                    "excludeNonCirculatingAccountsList": True,
                    "commitment": "finalized"
                }
            ]
        }
        response = http_client.post(
            SolanaBlockExplorerApi.API_URL,
            headers=SolanaBlockExplorerApi.HEADERS,
            json=data)
        if response.status_code == 200:
            return response.json()
        raise Exception("Could not get Solana Supply")

    def epoch_info() -> Any:
        data: Any = {
            "id": generate_uuid4(),
            "method": "getEpochInformation",
            "jsonrpc": "2.0",
            "params": []
        }
        response = http_client.post(
            SolanaBlockExplorerApi.API_URL,
            headers=SolanaBlockExplorerApi.HEADERS,
            json=data)
        if response.status_code == 200:
            return response.json()
        raise Exception("Could not get Epoch Information")



class SolscanApi:

    PUBLIC_API_URL: str = "http://api.solscan.io"
    HEADERS: Any = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

    def price_and_volume_usdt(symbol: str):
        url: str = "{}/market?symbol={}".format(
            SolscanApi.PUBLIC_API_URL,
            symbol)
        # logging.info('SerumServiceApi::price_and_volume_usdt::GET::{}'.format(url))
        response = http_client.get(
            url,
            headers=SolscanApi.HEADERS)
        if response.status_code == 200:
            return response.json()
        raise Exception('Could not get spl token price and volume usdt with symbol: {} - {}'.format(
            symbol,
            response.content
        ))
