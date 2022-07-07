import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

retry_strategy = Retry(
    total=10,
    status_forcelist=[413, 429, 503, 502, 504],
    backoff_factor=2,
    method_whitelist=["HEAD", "GET", "POST", "OPTIONS"]
)

adapter = HTTPAdapter(max_retries=retry_strategy)
http_client = requests.Session()
http_client.mount("https://", adapter)
http_client.mount("http://", adapter)
