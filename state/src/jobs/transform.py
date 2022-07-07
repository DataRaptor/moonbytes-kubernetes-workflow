import logging
from typing import Any
from src.utils import safe_get as get

class RaydiumTransformer:

    def token_list(data: Any) -> Any:
        tokens = data["official"]
        transformed_data: Any = []
        for token in tokens:
            transformed_data.append({
                "symbol": get(token, "symbol"),
                "name": get(token, "name"),
                "mint": get(token, "mint"),
                "decimals": get(token, "decimals"),
                "extensions": get(token, "extensions"),
                "icon": get(token, "icon")
            })
        return transformed_data

class SolscanTransformer:

    def markets_from_mint(data: Any) -> Any:
        markets = data["data"]
        transformed_data: Any = []
        for market in markets:
            try:
                transformed_data.append({
                    "_id": get(market, "_id"),
                    "address": get(market, "address"),
                    "amm_id": get(market, "ammdId"),
                    "program_id": get(market, "programId"),
                    "autodetect": get(market, "autodetect", cast=bool),
                    "name": get(market, "name"),
                    "source": get(market, "source"),
                    "liquidity": get(market, "liquidity"),
                    "exchange_rate": get(market, "price"),
                    "volume_24hr": get(market, "volume24h"),
                    "volume_7d": get(market, "volume7d"),
                    "liquidity_pct_change_24h": get(market, "liquidityChangePercentage24h"),
                    "volume_pct_change_24h": get(market, "volume24hChangePercentage24h"),
                    "base_amount": get(market, "amountBase"),
                    "base_symbol": get(get(market, "base"), "symbol"),
                    "base_mint": get(get(market, "base"), "address"),
                    "base_icon": get(get(market, "base"), "icon"),
                    "base_twitter": get(get(market, "base"), "twitter"),
                    "base_decimals": get(get(market, "base"), "decimals"),
                    "base_coingecko_id": get(get(market, "base"), "coingeckoId"),
                    "quote_amount": get(market, "amountQuote"),
                    "quote_symbol": get(get(market, "quote"), "symbol"),
                    "quote_mint": get(get(market, "quote"), "address"),
                    "quote_icon": get(get(market, "quote"), "icon"),
                    "quote_twitter": get(get(market, "quote"), "twitter"),
                    "quote_decimals": get(get(market, "quote"), "decimals"),
                    "quote_coingecko_id": get(get(market, "quote"), "coingeckoId"),
                })
            except Exception as e:
                logging.error("Could not parase market: {}".format(e))
                pass
        return transformed_data


class MagicEdenTransformer:

    def collections(data: Any) -> Any:

        data = data['collections']
        transformed_data: Any = []
        for collection in data:
            categories = get(collection, "categories")
            transformed_data.append({
                "symbol": get(collection, "symbol"),
                "categories": [category for category in categories if category] if categories else [],
                "created_at": get(collection, "createdAt"),
                "derivative_details_origin_name": get(get(collection, "derivativeDetails"), "originName"),
                "derivative_details_origin_link": get(get(collection, "derivativeDetails"), "originLink"),
                "description": get(collection, "description"),
                "discord": get(collection, "discord"),
                "enabled_attributes_filters": get(collection, "enabledAttributesFilters"),
                "image": get(collection, "image"),
                "is_derivative": get(collection, "isDerivative"),
                "name": get(collection, "name"),
                "total_items": get(collection, "totalItems"),
                "twitter": get(collection, "twitter"),
                "website": get(collection, "website"),
                "updated_at": get(collection, "updatedAt"),
                "watchlist_count": get(collection, "watchlistCount"),
                "volume_all": get(collection, "volumeAll")
            })
        return transformed_data

    # TODO: Figure out how to handle popular collections and new collections
    # Not sure storing it in mongo each time is a good idea. On the other hand
    # if we update the models in the Db we lose information about what was historically
    # in the new and popular collections.
    #
    # def popular_collections(data: Any) -> Any:
    #     data = data['collections']
    #     transformed_data: Any = []
    #     for collection in data:
    #         transformed_data.append({
    #             "symbol": get(collection, "symbol"),
    #             "candy_machine_ids": get(collection, "candyMachineIds"),
    #             "name": get(collection, "name"),
    #             "categories": get(collection, "categories"),
    #             "description": get(collection, "description"),
    #             "created_at": get(collection, "createdAt"),
    #             "enabled_attributes_filters": get(collection, "enabledAttributesFilters"),
    #             "isDraft": get(collection, "isDraft"),
    #             "website": get(collection, "website"),
    #             "twitter": get(collection, "twitter"),
    #             "discord": get(collection, "discord"),
    #             "derivatives_details": get(collection, "derivativesDetails"),
    #             "is_derivative": get(collection, "isDerivative"),
    #             "nft_image_type": get(collection, "nftImageType"),
    #             "rarity": get(collection, "rarity"),
    #             "updated_at": get(collection, "updatedAt"),
    #             "watchlist_count": get(collection, "watchlistCount"),
    #             "on_chain_collection_address": get(collection, "onChainCollectionAddress")
    #         })
    #     return transformed_data




