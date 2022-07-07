from typing import Any, List
from src.utils import lamports_to_sol
from src.utils import safe_get as get


class MagicEdenTransformer:

    def collection_metrics(data: Any) -> Any:
        results = data["results"]
        volume_all: float = lamports_to_sol(
            get(results, "volumeAll"))
        volume_24hr: float = lamports_to_sol(
            get(results, "volume24hr"))
        listed_count: int = get(results, "listedCount")
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
