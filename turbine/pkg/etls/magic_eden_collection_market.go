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

func RunMagicEdenCollectionMarketETL() {

	logger.Info("[ETL] 📦 MagicEdenCollectionMarketETL started")

	url := config.MagicEdenCollectionMarketETLUrl

	scaledWaitSeconds := config.SlowETLFactor * config.MagicEdenCollectionMarketETLWaitSeconds

	for {

		collections := state.GetMagicEdenCollections()

		rand.Shuffle(len(collections), func(i, j int) {
			collections[i], collections[j] = collections[j], collections[i]
		})

		logger.Info("Received " + strconv.Itoa(len(collections)) + " magic eden nft collections")

		for i := 0; i < len(collections); i++ {

			PostMagicEdenCollectionToMarketETL(url, collections[i])
			time.Sleep(time.Millisecond * 1500)
		}

		logger.Debug("MagicEdenCollectionMarketETL sleeping for " + strconv.Itoa(scaledWaitSeconds) + " s")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}

}

func PostMagicEdenCollectionToMarketETL(url string, collection models.MagicEdenCollection) {
	body, err := json.Marshal(collection)
	if err != nil {
		logger.Error("JSON marshal error")
	}

	response, err2 := http.Post(
		url,
		"application/json",
		bytes.NewBuffer(body),
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
		logger.Info(fmt.Sprintf("[ETL] MagicEdenCollectionMarket:: %+v", etlExecutionResponse))
	} else {
		logger.Error(fmt.Sprintf("[ETL] MagicEdenCollectionMarket:: %+v", etlExecutionResponse))
	}

}
