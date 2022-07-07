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

def safe_cast(value, cast):
    if not value:
        return None
    return cast(value)