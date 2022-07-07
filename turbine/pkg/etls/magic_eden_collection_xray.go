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

func RunMagicEdenCollectionXrayETL() {

	logger.Info("[ETL] 📦 MagicEdenCollectionXrayETL started")

	url := config.MagicEdenCollectionXrayETLUrl

	scaledWaitSeconds := config.SlowETLFactor * config.MagicEdenCollectionXrayETLWaitSeconds

	for {

		collections := state.GetMagicEdenCollections()

		rand.Shuffle(len(collections), func(i, j int) {
			collections[i], collections[j] = collections[j], collections[i]
		})

		logger.Debug("Received " + strconv.Itoa(len(collections)) + " magic eden nft collections")

		for i := 0; i < len(collections); i++ {
			PostMagicEdenCollectionToXrayETL(url, collections[i])
		}

		logger.Debug("MagicEdenCollectionXrayETL sleeping for " + strconv.Itoa(scaledWaitSeconds) + " s")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}

}

func PostMagicEdenCollectionToXrayETL(url string, collection models.MagicEdenCollection) {
	body, err := json.Marshal(collection)
	if err != nil {
		fmt.Printf("Marshal Error %+v\n", err)
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
		logger.Error(fmt.Sprintf("Could not decode execution response %+v", err))
	}

	if etlExecutionResponse.Ok {
		logger.Info(fmt.Sprintf("[ETL] MagicEdenCollectionXray:: %+v", etlExecutionResponse))
	} else {
		logger.Error(fmt.Sprintf("[ETL] MagicEdenCollectionXray:: %+v", etlExecutionResponse))
	}
}
