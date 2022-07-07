from typing import Any

def extract_market_address(request: Any) -> str:
    data: Any = request.get_json()
    return safe_get(data, "address")

def safe_cast(value, cast):
    if not value:
        return None
    return cast(value)


def safe_get(dict_like, key, cast=None):
    if not dict_like:
        return None
    if key not in dict_like:
        return None
    if cast:
        if dict_like[key]:
            return cast(dict_like[key])
        return None
    return dict_like[key]


def lamports_to_sol(lamports: int):
    if not lamports:
        return None
    return lamports / 1e+9

