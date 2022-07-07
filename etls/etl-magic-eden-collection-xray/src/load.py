import datetime
from typing import Any, List
from influxdb_client import Point, WritePrecision
from src.db import mongo

class MagicEdenLoader:

    def collection_activity(collection_symbol: str, data: Any) -> List[mongo.MagicEdenCollectionActivity]:
        def _generate_activity_hash(activity: mongo.MagicEdenCollectionActivity):
            return "{}-{}-{}-{}-{}".format(
                activity.mint,
                activity.action,
                activity.buyer,
                activity.seller,
                activity.price)

        def _generate_activity_hash_set(
            collection_activities: List[mongo.MagicEdenCollectionActivity]) -> str:
            hash_set = set()
            for activity in collection_activities:
                hash_set.add(_generate_activity_hash(activity))
            return hash_set

        created: datetime.DateTime = datetime.datetime.utcnow()

        collection_activities = mongo.MagicEdenCollectionActivity.objects(
            collection_symbol=collection_symbol)
        collection_activities_hash_set = _generate_activity_hash_set(
            collection_activities)
        
        models: List[mongo.MagicEdenCollectionActivity] = []
        for event in data:
            activity = mongo.MagicEdenCollectionActivity(
                collection_symbol=collection_symbol,
                mint=event['mint'],
                action=event['action'],
                buyer=event['buyer'],
                seller=event['seller'],
                price=event['price'],
                created=created)
            activity_hash: str = _generate_activity_hash(
                activity)
            if activity_hash not in collection_activities_hash_set:
                models.append(activity)
        
        return models


    def collection_listings(collection_symbol: str, data: Any) -> List[mongo.MagicEdenCollectionListing]:

        def _generate_listing_hash(listing: mongo.MagicEdenCollectionListing):
            return "{}-{}-{}-{}-{}".format(
                listing.token,
                listing.mint,
                listing.seller,
                listing.price,
                listing.created)

        def _generate_listing_hash_set(
            collection_listings: List[mongo.MagicEdenCollectionListing]) -> str:
            hash_set = set()
            for listing in collection_listings:
                hash_set.add(_generate_listing_hash(listing))
            return hash_set

        created: datetime.DateTime = datetime.datetime.utcnow()

        collection_listings = mongo.MagicEdenCollectionListing.objects(
            collection_symbol=collection_symbol)
        collection_listings_hash_set = _generate_listing_hash_set(
            collection_listings)
        
        models: List[mongo.MagicEdenCollectionListing] = []
        for event in data:
            listing = mongo.MagicEdenCollectionListing(
                collection_symbol=collection_symbol,
                token=event['token'],
                mint=event['mint'],
                seller=event['seller'],
                price=event['price'],
                created=created)
            listing_hash: str = _generate_listing_hash(
                listing)
            if listing_hash not in collection_listings_hash_set:
                models.append(listing)

        return models