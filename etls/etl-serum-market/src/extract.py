from typing import Any
import logging
import requests
from requests import Response
from src.transport import http_client
from src.config import SERUM_URL 

class SerumServiceApi:

    def market_data(
        market_address: str,
        program_id: str,
        base_symbol: str,
        quote_symbol: str):
        url = "{}/market_data".format(SERUM_URL)
        # logging.info('SerumServiceApi::market_data::Post::{}'.format(url))
        response: Response = http_client.post(
            url,
            json={
                "marketAddress": market_address,
                "programId": program_id,
                "baseSymbol": base_symbol,
                "quoteSymbol": quote_symbol
            })
        if response.status_code == 200:
            # logging.info(response.json())
            return response.json()
        
        raise Exception('Could not get market_data for market with address: {}'.format(
            market_address
        ))



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

    def amm_statistics(market_address: str):
        url: str = "{}/amm/read?address={}".format(
            SolscanApi.PUBLIC_API_URL,
            market_address)
        # logging.info('SerumServiceApi::amm_statistics::GET::{}'.format(url))
        response = http_client.get(
            url,
            headers=SolscanApi.HEADERS)
        if response.status_code == 200:
            return response.json()
        raise Exception('Could not get amm statistics for market with address: {} - {}'.format(
            market_address,
            response.content
        ))


