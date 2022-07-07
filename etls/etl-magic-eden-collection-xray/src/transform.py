from typing import Any, List
from src.utils import lamports_to_sol
from src.utils import safe_get as get


class MagicEdenTransformer:

    def collection_activity(data: Any) -> Any:
        transformed_data: Any = []
        for activity_item in data:
            mint: str = get(activity_item, "tokenMint")
            action: str = get(activity_item, "type")
            buyer: str = get(activity_item, "buyer")
            seller: str = get(activity_item, "seller")
            price: str = get(activity_item, "price")
            transformed_data.append({
                "mint": mint,
                "action": action,
                "buyer": buyer,
                "seller": seller,
                "price": price
            })
        return transformed_data

    def collection_listings(data: Any) -> Any:
        transformed_data: Any = []
        for listing_item in data:
            token: str = get(listing_item, "tokenAddress")
            mint: str = get(listing_item, "tokenMint")
            seller: str = get(listing_item, "seller")
            price: float = get(listing_item, "price")
            transformed_data.append({
                "token": token,
                "mint": mint,
                "seller": seller,
                "price": price
            })
        return transformed_data

    def collection_metrics(data: Any) -> Any:
        results = data["results"]
        volume_all: float = lamports_to_sol(
            get(results, "volumeAll"))
        volume_24hr: float = lamports_to_sol(
            get(results, "volume24hr"))
        listed_count: int = lamports_to_sol(
            get(results, "listedCount"))
        price_average_24hr: float = lamports_to_sol(
            get(results, "avgPrice24hr"))
        price_floor: float = lamports_to_sol(
            get(results, "floorPrice"))

        attributes: List[Any] = []
        for attribute in attributes:
            attribute_data: Any = get(attribute, "attribute")
            attribute_trait_type: str = get(attribute_data, "trait_type")
            attribute_trait_value: str = get(attribute_data, "trait_value")
            attribute_listed_count: int = get(attribute_data, "value")
            attribute_price_floor: float = lamports_to_sol(
                get(attribute_data, "floor"))
            attributes.append({
                "trait_type": attribute_trait_type,
                "value": attribute_trait_value,
                "listed_count": attribute_listed_count,
                "price_floor": attribute_price_floor
            })

        return {
            'volume_all': volume_all,
            'volume_24hr': volume_24hr,
            'listed_count': listed_count,
            'price_average_24hr': price_average_24hr,
            'price_floor': price_floor,
            'attributes': attributes
        }


# class TwitterTransformer:

#     CONSUMER_KEY: str = "H6621iKuL4x0rISBtecFZycMf"
#     CONSUMER_SECRET: str = "sKQ9cYUf7ngx9ZsUXopSvDvqnXlUc08u5lDQmvU84EX99pH8k1"
#     ACCESS_TOKEN_KEY: str = "1507127205675114503-95OGnIWSPNdBExOzX9tSmg3hGWpkbf"
#     ACCESS_TOKEN_SECRET: str = "5nEsqejvdezqcCVEsph1YAGFjqy9laur6mGaufxu0yIJp"

#     client = twitter.Api(
#         consumer_key=CONSUMER_KEY,
#         consumer_secret=CONSUMER_SECRET,
#         access_token_key=ACCESS_TOKEN_KEY,
#         access_token_secret=ACCESS_TOKEN_SECRET)


#     def get_user_metrics(screen_name: str):
#         pass
