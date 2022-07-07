import logging
import os 
from typing import List

def load_user_agents() -> List[str]:
    user_agents: List[str] = []
    with open(os.path.join("bin", "useragents.txt"), 'r') as f:
        lines = f.readlines()
        for user_agent in lines:
            logging.info(user_agent)
            user_agents.append(str(user_agent).replace('\n', ''))
    return user_agents

if __name__ == '__main__':
    user_agents: List[str] = load_user_agents()
    print(user_agents)