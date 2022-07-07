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

def generate_uuid4():
    return "0ec7a087-82ee-46c3-bb32-7102a7e11e63"


def lamports_to_sol(lamports: int):
    if not lamports:
        return None
    return lamports / 1e+9

