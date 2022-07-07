import requests


def execute():
    data = {
        'baseSymbol': 'WOOF',
        'quoteSymbol': 'USDC',
        'marketAddress': 'CwK9brJ43MR4BJz2dwnDM7EXCNyHhGqCJDrAdsEts8n5',
        'programId': '9xQeWvG816bUx9EPjHmaT23yvVM2ZWbrrpZb9PusVFin',
        'side': 'sell',
        'price': 0.000358,
        'quantity': 1
    }
    url = 'http://localhost:8080/market_data'
    r = requests.post(
        url,
        headers={},
        json=data)
    if r.status_code == 200:
        print(r.json())
    print(r.content)
    print('done')


if __name__ == '__main__':
    execute()
