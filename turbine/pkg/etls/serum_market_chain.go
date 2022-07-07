package etls

import (
	"bytes"
	"encoding/json"
	"fmt"
	"math/rand"
	"net/http"
	"strconv"
	"time"
	"turbine/config"
	"turbine/pkg/models"
	"turbine/pkg/state"
	"turbine/server/logger"
)

func RunSerumMarketETL() {

	logger.Info("[ETL] 📦 SerumMarketETL started")

	url := config.SerumMarketETLUrl

	scaledWaitSeconds := config.SlowETLFactor * config.MagicEdenCollectionMarketETLWaitSeconds

	for {

		serumMarkets := state.GetSerumMarkets()

		rand.Shuffle(len(serumMarkets), func(i, j int) {
			serumMarkets[i], serumMarkets[j] = serumMarkets[j], serumMarkets[i]
		})

		for i := 0; i < len(serumMarkets); i++ {
			PostSerumMarketToChainETL(url, serumMarkets[i])
		}

		logger.Debug("SerumMarketETL sleeping for " + strconv.Itoa(scaledWaitSeconds) + " s")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}

}

func PostSerumMarketToChainETL(url string, serumMarket models.SerumMarket) {
	body, err := json.Marshal(serumMarket)
	if err != nil {
		fmt.Printf("Marshal Error %+v\n", err)
	}

	response, err2 := http.Post(
		url,
		"application/json",
		bytes.NewReader(body),
	)

	if err2 != nil {
		logger.Error(fmt.Sprintf("HTTP post error - %+v", err2))
	}

	decoder := json.NewDecoder(response.Body)
	var etlExecutionResponse models.ETLExecutionResponse

	if err := decoder.Decode(&etlExecutionResponse); err != nil {
		logger.Error("Could not decode execution response")
	}

	if etlExecutionResponse.Ok {
		logger.Info(fmt.Sprintf("[ETL] SerumMarket:: %+v", etlExecutionResponse))
	} else {
		logger.Error(fmt.Sprintf("[ETL] SerumMarket:: %+v", etlExecutionResponse))
	}
}
