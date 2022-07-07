from typing import Any
from flask import jsonify
from src.v1.db import mongo

def v1_magic_eden_collections():
    magic_eden_collections: Any = mongo.MagicEdenCollection.objects.order_by('-volume_all')
    return jsonify({
        "ok": True if len(magic_eden_collections) > 0 else False,
        "data": [
            {
                "categories": collection.categories,
                "created": collection.created,
                "derivative_details_origin_link": collection.derivative_details_origin_link,
                "derivative_details_origin_name": collection.derivative_details_origin_name,
                "description": collection.description,
                "discord": collection.discord,
                "enabled_attributes_filters": collection.enabled_attributes_filters,
                "image": collection.image,
                "is_derivative": collection.is_derivative,
                "name": collection.name,
                "symbol": collection.symbol,
                "total_items": collection.total_items,
                "twitter": collection.twitter,
                "volume_all": collection.volume_all,
                "website": collection.website,
                "watchlist_count": collection.watchlist_count
            } for collection in magic_eden_collections
        ]
    })