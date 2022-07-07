from typing import Any, List
from src.db.mongo import MongoDb


class MagicEdenLoader:

    def collections(data: Any) -> List[MongoDb.MagicEdenCollection]:

        models: List[MongoDb.MagicEdenCollection] = []

        existing_symbols: List[str] = list(map(
            lambda token: token.symbol,
            MongoDb.MagicEdenCollection.objects.all()
        ))

        for collection in data:
            if collection['symbol'] not in existing_symbols:
                magic_eden_collection = MongoDb.MagicEdenCollection(
                    symbol=collection['symbol'],
                    categories=collection['categories'],
                    created_at=collection['created_at'],
                    derivative_details_origin_name=collection['derivative_details_origin_name'],
                    derivative_details_origin_link=collection['derivative_details_origin_link'],
                    description=collection['description'],
                    discord=collection['discord'],
                    enabled_attributes_filters=collection['enabled_attributes_filters'],
                    image=collection['image'],
                    is_derivative=collection['is_derivative'],
                    name=collection['name'],
                    total_items=collection['total_items'],
                    twitter=collection['twitter'],
                    website=collection['website'],
                    updated_at=collection['updated_at'],
                    watchlist_count=collection['watchlist_count'],
                    volume_all=collection['volume_all'])
                models.append(magic_eden_collection)
        return models



class RaydiumLoader:

    def token_list(data: Any) -> List[MongoDb.SplToken]:

        models: List[MongoDb.SplToken] = []

        existing_mints: List[str] = list(map(
            lambda token: token.mint,
            MongoDb.SplToken.objects.all()
        ))
        for token in data:
            if token['mint'] not in existing_mints:
                spl_token = MongoDb.SplToken(
                    symbol=token['symbol'],
                    name=token['name'],
                    mint=token['mint'],
                    decimals=token['decimals'],
                    extensions=str(token['extensions']),
                    icon=token['icon'])
                models.append(spl_token)
                
        return models

class SolscanLoader:

    def markets_from_mint(data: Any) -> List[MongoDb.SerumMarket]:
        models: List[MongoDb.SerumMarket] = []

        existing_serum_markets: List[MongoDb.SerumMarket] = MongoDb.SerumMarket.objects.all()
        existing_serum_market_addresses: List[str] = list(map(
            lambda serum_market: serum_market['address'],
            existing_serum_markets))

        for market in data:
            address: str = market['address']
            source: str = market['source']
            if (source == "serum") and (address not in existing_serum_market_addresses):
                serum_market = MongoDb.SerumMarket(
                    address=market["address"],
                    amm_id=market["amm_id"],
                    program_id=market["program_id"],
                    autodetect=market["autodetect"],
                    name=market["name"],
                    source=market["source"],                
                    base_symbol=market["base_symbol"],
                    base_mint=market["base_mint"], 
                    base_icon=market["base_icon"],
                    base_twitter=market["base_twitter"],
                    base_decimals=market["base_decimals"],
                    base_coingecko_id=market["base_coingecko_id"],
                    quote_symbol=market["quote_symbol"],
                    quote_mint=market["quote_mint"],
                    quote_icon=market["quote_icon"],
                    quote_twitter=market["quote_twitter"],
                    quote_decimals=market["quote_decimals"],
                    quote_coingecko_id=market["quote_coingecko_id"])
                models.append(serum_market)
        
        return models
