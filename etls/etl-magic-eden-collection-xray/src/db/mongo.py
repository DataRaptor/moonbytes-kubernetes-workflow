import logging
import datetime
from typing import Any, List
from mongoengine import (
    Document,
    StringField,
    FloatField,
    IntField,
    ReferenceField,
    ListField,
    BooleanField,
    DateTimeField
)

class SerumMarket(Document):
    meta = {'collection': 'serum_markets'}
    address = StringField()
    amm_id = StringField()
    program_id = StringField()
    autodetect = BooleanField()
    name = StringField()
    source = StringField()
    base_mint = StringField()
    quote_mint = StringField()
    base_symbol = StringField()
    quote_symbol = StringField()
    base_icon = StringField()
    quote_icon = StringField()
    base_twitter = StringField()
    quote_twitter = StringField()
    base_decimals = IntField()
    quote_decimals = IntField()
    base_coingecko_id = StringField()
    quote_coingecko_id = StringField()
    created = DateTimeField(default=datetime.datetime.utcnow)

class MagicEdenCollection(Document):
    meta = {'collection': 'magic_eden_collections'}
    symbol = StringField(required=True)
    categories = ListField(StringField(), default=[])
    created_at = DateTimeField()
    derivative_details_origin_name = StringField()
    derivative_details_origin_link = StringField()
    description = StringField()
    discord = StringField()
    enabled_attributes_filters = BooleanField()
    image = StringField()
    is_derivative = BooleanField()
    name = StringField()
    total_items = FloatField()
    twitter = StringField()
    website = StringField()
    updated_at = StringField()
    watchlist_count = IntField()
    volume_all = FloatField()
    created = DateTimeField(default=datetime.datetime.utcnow)


class MagicEdenCollectionActivity(Document):
    meta = {'collection': 'magic_eden_collection_activities'}
    collection_symbol = StringField()
    mint = StringField()
    action = StringField()
    buyer = StringField()
    seller = StringField()
    price = FloatField()
    created = DateTimeField(default=datetime.datetime.utcnow)

class MagicEdenCollectionListing(Document):
    meta = {'collection': 'magic_eden_collection_listing'}
    collection_symbol = StringField()
    token = StringField()
    mint = StringField()
    seller = StringField()
    price = FloatField()
    created = DateTimeField(default=datetime.datetime.utcnow)

class SplToken(Document):
    meta = {'collection': 'solana_spl_tokens'}
    symbol = StringField()
    name = StringField()
    mint = StringField()
    decimals = IntField()
    extensions = StringField()
    icon = StringField()

def write_models(models: List[Any]) -> bool:
    success: bool = True
    # This is super inefficient. We should be using the insert many 
    # documents call here. 
    for model in models:
        try:
            model.save()
        except Exception as e:
            success = False
            logging.error("could not save model: {} - {} ".format(
                model,
                e
            ))
            pass
    return success

