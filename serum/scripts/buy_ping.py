import requests 
import json 
import os 

def execute():
    path = os.path.join('scripts', 'meta', 'data.json')
    with open(path, 'r') as f:
        data = json.load(f)
    url = "http://localhost:8080/executeBuyTrade"
    headers = {'content-type': 'application/json'}
    response = requests.post(
        url, 
        data=json.dumps(data), 
        headers=headers)
    body = response.json()
    if body['ok']:
        print('🧪 Buy Trade Executed Successfully')
    else:
        print('💀 Buy Trade Executed Unsucessfully')
        print(body)

if __name__ == "__main__":
    print(execute())