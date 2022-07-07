package config

import (
	"os"
	"strconv"
)

func getEnv(key, fallback string) string {
	if value, ok := os.LookupEnv(key); ok {
		return value
	}
	return fallback
}

func stringToBool(str string) bool {
	boolValue, err := strconv.ParseBool(str)
	if err != nil {
		return false
	}
	return boolValue
}

const SlowETLFactor = 5
const SlowStateFactor = 5

var StateUrl = getEnv(
	"STATE_URL",
	"http://state:4202",
)

var MagicEdenCollectionMarketETLUrl = getEnv(
	"ETL_MAGIC_EDEN_COLLECTION_MARKET_URL",
	"http://etl-magic-eden-collection-market:4208")
var MagicEdenCollectionMarketETLEnabled = stringToBool(getEnv(
	"ENABLE_ETL_MAGIC_EDEN_COLLECTION_MARKET",
	"false",
))
var MagicEdenCollectionMarketETLWaitSeconds = 5

var MagicEdenCollectionXrayETLUrl = getEnv(
	"ETL_MAGIC_EDEN_COLLECTION_XRAY_URL",
	"http://etl-magic-eden-collection-xray:4207")
var MagicEdenCollectionXrayETLEnabled = stringToBool(getEnv(
	"ENABLE_ETL_MAGIC_EDEN_COLLECTION_XRAY",
	"false",
))
var MagicEdenCollectionXrayETLWaitSeconds = 5

var MagicEdenGlobalETLUrl = getEnv(
	"ETL_MAGIC_EDEN_GLOBAL_URL",
	"http://etl-magic-eden-global:4206")
var MagicEdenGlobalETLEnabled = stringToBool(getEnv(
	"ENABLE_ETL_MAGIC_EDEN_GLOBAL",
	"false",
))
var MagicEdenGlobalETLWaitSeconds = 5

var SerumMarketETLUrl = getEnv(
	"ETL_SERUM_MARKET_URL",
	"http://etl-serum-market:4205")
var SerumMarketETLEnabled = stringToBool(getEnv(
	"ENABLE_ETL_SERUM_MARKET",
	"false",
))
var SerumMarketETLWaitSeconds = 5

var SolanaGlobalETLUrl = getEnv(
	"ETL_SOLANA_GLOBAL_URL",
	"http://etl-solana-global:4204")
var SolanaGlobalETLEnabled = stringToBool(getEnv(
	"ENABLE_ETL_SOLANA_GLOBAL",
	"false",
))
var SolanaGlobalETLWaitSeconds = 60

var UpdateMagicEdenCollectionsJobEnabled = stringToBool(getEnv(
	"ENABLE_JOB_UPDATE_MAGIC_EDEN_COLLECTIONS",
	"false",
))
var UpdateMagicEdenCollectionsJobWaitSeconds = 1000

var UpdateSolanaSplTokensJobEnabled = stringToBool(getEnv(
	"ENABLE_JOB_UPDATE_SOLANA_SPL_TOKENS",
	"false",
))
var UpdateSolanaSplTokenJobWaitSeconds = 1000

var UpdateSerumMarketsJobEnabled = stringToBool(getEnv(
	"ENABLE_JOB_UPDATE_SERUM_MARKETS",
	"false",
))
var UpdateSerumMarketsJobWaitSeconds = 1000
