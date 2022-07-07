import requests


def execute():
    data = {
        'baseSymbol': 'WOOF',
        'quoteSymbol': 'USDC',
        'marketAddress': 'CwK9brJ43MR4BJz2dwnDM7EXCNyHhGqCJDrAdsEts8n5',
        'programId': '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
    }
    url = 'http://localhost:8080/getMarketData'
    r = requests.post(
        url,
        headers={},
        json=data)
    if r.status_code == 200:
        print(r.json())
    print('done')


if __name__ == '__main__':
    execute()
