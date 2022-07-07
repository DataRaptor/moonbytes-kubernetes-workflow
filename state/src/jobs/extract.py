from src.transport import http_client
from requests import Response
from typing import Any

class MagicEdenApi:

    PUBLIC_API_URL: str = "https://api-mainnet.magiceden.dev/v2"
    RPC_API_URL: str = "https://api-mainnet.magiceden.io"
    HEADERS: Any = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    def popular_collections(time_range) -> Any:
        url: str = "{}/popular_collections?timeRange={}&edge_cache=true".format(
            MagicEdenApi.RPC_API_URL, time_range)
        response: Response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data


    def collections(
            max_offset: int = 5000,
            limit: int = 500) -> Any:
        url: str = "{}/all_collections_with_escrow_data?edge_cache=true".format(
            MagicEdenApi.RPC_API_URL)
        response: Response = http_client.get(
            url,
            headers=MagicEdenApi.HEADERS)
        data: Any = response.json()
        return data


class RaydiumApi:

    SDK_API_URL: str = "https://api.raydium.io/v2/sdk"
    HEADERS: Any = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

    def token_list():
        url: str = "{}/token/raydium.mainnet.json".format(
            RaydiumApi.SDK_API_URL)
        response = http_client.get(
            url,
            headers=RaydiumApi.HEADERS)
        if response.status_code == 200:
            return response.json()
        raise Exception('Could not raydium token_list')


class SolscanApi:

    PUBLIC_API_URL: str = "https://api.solscan.io"
    HEADERS: Any = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36"
    }

    def markets_from_mint(mint: str):
        url: str = "{}/amm/market?address={}&sort_by=liquidity&sort_type=desc".format(
            SolscanApi.PUBLIC_API_URL,
            mint)
        response = http_client.get(
            url,
            headers=SolscanApi.HEADERS)
        if response.status_code == 200:
            return response.json()
        raise Exception('Could not get markets_from_mint with mint: {} - Error: {}'.format(
            mint,
            response.content
        ))
