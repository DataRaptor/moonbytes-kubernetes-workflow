import logging
from typing import List, Any

def get_collection_symbols(collections: List[Any]):
    extract_symbol = lambda c: c['symbol']
    return list(map(extract_symbol, collections))


