<br/>
<p align="center">
    <a>
        <img alt="Solana" src="https://avatars.githubusercontent.com/u/104286117?s=200&v=4" width="100"/>
    </a>
</p>
<h1 align="center"> Moonbytes </h1>
<br/>
<br/>

# ⚫ moonbytes-gargantuan

## Notice: This documentation is a little hold and should be updated soon.

## Overview

moonbytes-gargantuan is a collection of micro-services for streaming and consuming data from moonbytes datasources.

The `turbine` service (batching[TODO]) sends http requests to ETL services invoking the start of a job. Each ETL can be thought of as a function:

<b><p align="center">f: X -> Y</p></b>

Some ETLs require no input, X. The `turbine` is agnostic to the output of the ETLs, that is to say that the `turbine` doesn't care or process the output Y.
Y is instead loaded to it's appropriate long-term storage db. Each ETL is a single post endpoint flask server.

Sometimes, ETLs or the `turbine` might require additional data to process a job. In such cases these services can invoke requests to the `state`
service. The `state` service holds global data regarding our datasets. For example: the addresses of all serum markets or all magic eden collections ids.
The `turbine` will ocassionally send http requests to the `state` to update this global data.

The collection of services runs as a workload on a kubernetes cluster.

Two services are exposed to the internet, namely the `api` and `client`.

## Requirements

1. [Make](https://www.gnu.org/software/make/)
2. [Python3](https://www.python.org/downloads/)
3. [Golang](https://go.dev/)
4. [NodeJS](https://nodejs.org/en/)
5. [Docker](https://docs.docker.com/compose/install/)
6. [Docker-Compose](https://docs.docker.com/compose/install/)

## Datasets and Datasources

1. **_🦾 Solana_**
   a) **solana-rpc** - solana public rpc api

2. **_🖼️ Magic Eden_**

a) **magic-eden-rpc** - magic eden private rpc api
b) **magic-eden-public** - magic eden public api

3. **_🪣 Serum_**

a). **solscan** - serum market amm statistics and metadata
b). **solana-rpc** - serum public rpc api

## Data Schema

We use InfluxDB for time series data and mongodb for documents.

### InfluxDb

It is useful to think of our data as being primarily partitionable on the following influxDb tags: `Dataset`, `Model` and `Measurement`. We should note that a given measurement can (and often will) contain additional influxDb tags.

Loosely speaking, here are the definitions:

a)`Dataset` - Highest level of data binning, namespace of a dataset (eg. magic_eden, serum, solana, ...).

b) `Model` - Mid level astraction, useful for defining objects, areas or partions (eg: markets, collections, ...).

c) `Measurement` - metric of interest (eg: volume, price, listing_count, ...).

The following is a sample representation of our schema.

Visual

```json
{
    "Dataset_1": {
        "Model_1": [
            "Measurement_x",
            "Measurement_y",
        ],
        "Model_2": {
            "Measurement_y"
        }
    },
    "Dataset_2": {
        "Model_1": [
            "Measurement_x",
            "Measurement_y"
        ],
        "Model_3": [
            "Measurement_y",
            "Measurement_z"
        ]
    },
    ...
}
```

The following the the current working schema.

```json
{
  "Solana": {
    "global": [
      "price_usdt[TODO]",
      "sol_staked[TODO]",
      "sol_staked_percentage[TODO]",
      "phantom_users[TODO]"
    ],
    "tokens": ["price_usdt[TODO]", "volume_usdt[TODO]", "unique_holders[TODO]"]
  },
  "MagicEden": {
    "global": ["volume_all", "volume_total"],
    "markets": [
      "volume_all",
      "volume_24hr",
      "listed_count",
      "price_average_24hr",
      "price_floor"
    ],
    "activity": [
      "bid_price",
      "list_price",
      "buyNow_price",
      "delist_price",
      "cancelBid_price"
    ],
    "listings": ["listing_price"],
    "attributes": ["price_floor", "listed_count"]
  },
  "Serum": {
    "markets": [
      "price_usdt[TODO]",
      "volume_usdt[TODO]",
      "liquidity[TODO]",
      "liquidity_pct_change_24hr[TODO]",
      "exchange_rate[TODO]",
      "volume_7d[TODO]",
      "volume_24hr[TODO]",
      "volume_24hr_pct_change_24hr[TODO]"
    ]
  },
  "Twitter": {
    "projects": ["followers[TODO]", "engagement[TODO]"],
    "influencers": ["followers[TODO]", "engagement[TODO]"]
  }
}
```

## Development

When creating other services it is best to test them in their own custom environments.
You may then network them together and test using docker-compose.

#### 1. Environment Variables and Influx

Create an `.env` file in the root directory with the following entries:

```bash
# Logging
LOG_LEVEL="info"

# ETL Switches
SLOW_ETLS=true
ENABLE_MAGIC_EDEN_COLLECTION_MARKET_ETL=true
ENABLE_MAGIC_EDEN_COLLECTION_XRAY_ETL=true
ENABLE_MAGIC_EDEN_GLOBAL_ETL=true
ENABLE_SERUM_MARKET_ETL=true
ENABLE_SOLANA_GLOBAL_ETL=true
ENABLE_SOLANA_SPL_TOKEN_ETL=true

# TODO: Job Switches here would be nice too
ENABLE_UPDATE_MAGIC_EDEN_COLLECTIONS_JOB=true
ENABLE_UPDATE_SOLANA_SPL_TOKENS_JOB=true
ENABLE_UPDATE_SERUM_MARKETS_JOB=true

# Influx DB Config
INFLUXDB_ORG="gradient"
INFLUXDB_BUCKET="gradient-prod"
DOCKER_INFLUXDB_INIT_ADMIN_TOKEN="dR-dqUJTS6tz-PdkMh6vRxgCY3qwNAzGkb_UqqymCaVothz8NIziCkhUSfXIcw61A6EvfFa9pB8vTvbaRzYk3A=="
DOCKER_INFLUXDB_INIT_USERNAME="root"
DOCKER_INFLUXDB_PASSWORD="dR-dqUJTS6tz-PdkMh6vRxgCY3qwNAzGkb_UqqymCaVothz8NIziCkhUSfXIcw61A6EvfFa9pB8vTvbaRzYk3A=="
DOCKER_INFLUXDB_INIT_ORG=${INFLUXDB_ORG}
DOCKER_INFLUXDB_INIT_BUCKET=${INFLUXDB_BUCKET}
INFLUXDB_TOKEN=${DOCKER_INFLUXDB_INIT_ADMIN_TOKEN}
```

## Production

The gargantuan is run as a workload on a Kubernetes cluster. We use Containerd as our container
runtime environment. To start the services in production run:

    make

## Exposed Services

The `api` service is exposed to the world.
