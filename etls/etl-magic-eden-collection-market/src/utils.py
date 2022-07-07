from typing import Any

def extract_collection_symbol(request: Any) -> str:
    data: Any = request.get_json()
    return safe_get(data, "symbol")

def safe_get(dict_like, key):
    if not dict_like:
        return None
    if key not in dict_like:
        return None
    return dict_like[key]


def lamports_to_sol(lamports: int):
    if not lamports:
        return None
    return lamports / 1e+9
