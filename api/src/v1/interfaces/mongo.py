import json
import pandas as pd 
from typing import List
from src.v1.db.mongo import (
    MagicEdenCollectionListing,
    MagicEdenCollectionActivity
)

class MongoDbInterface:

    def get_magic_eden_collections_activity(
        measurements: List[str],
        collections: List[str]) -> pd.DataFrame:

        activities = MagicEdenCollectionActivity.objects(
            collection_symbol__in=collections,
            action__in=measurements)
        
        json_data = json.loads(activities.to_json())

        return pd.json_normalize(json_data)

    def get_magic_eden_collections_listings(
        measurements: List[str],
        collections: List[str]) -> pd.DataFrame:

        listings = MagicEdenCollectionListing.objects(
            collection_symbol__in=collections)

        json_data = json.loads(listings.to_json())

        return pd.json_normalize(json_data)