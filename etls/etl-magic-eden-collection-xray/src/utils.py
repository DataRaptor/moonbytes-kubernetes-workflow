import os
import logging
from typing import List, Any

def extract_collection_symbol(request: Any) -> str:
    data: Any = request.get_json()
    return safe_get(data, "symbol")
    

def safe_get(dict_like, key):
    if not dict_like:
        return None
    if key not in dict_like:
        return None
    return dict_like[key]

def load_user_agents() -> List[str]:
    user_agents: List[str] = []
    with open(os.path.join("bin", "useragents.txt"), 'r') as f:
        lines = f.readlines()
        for user_agent in lines:
            logging.info(user_agent)
            user_agents.append(str(user_agent).replace('\n', ''))
    return user_agents


def lamports_to_sol(lamports: int):
    if not lamports:
        return None
    return lamports / 1e+9
