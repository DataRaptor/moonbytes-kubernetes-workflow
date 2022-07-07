import os 
import logging

LOG_LEVEL: int = logging.INFO
INFLUX_HOST: str = os.environ.get(
    "INFLUXDB_HOST", 
    "https://europe-west1-1.gcp.cloud2.influxdata.com")
INFLUX_TOKEN: str = os.environ.get(
    'INFLUXDB_TOKEN', 
    "4rn6Ktx2Oe4BH3qRVQ9Apmy4nd1BK4vqWmepXYFZzZwIaTflBGx7RpyVN3quSIkHbsVkOuBcHO2LFvc7-RxavA==")
INFLUX_ORG: str = os.environ.get(
    "INFLUXDB_ORG", 
    "trycelebshot@gmail.com")
INFLUX_BUCKET: str = os.environ.get(
    "INFLUXDB_BUCKET", 
    "gradient-dev")