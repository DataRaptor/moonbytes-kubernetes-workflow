package etls

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"time"
	"turbine/config"
	"turbine/pkg/models"
	"turbine/server/logger"
)

func RunSolanaGlobalETL() {

	logger.Info("[ETL] 📦 SolanaGlobalETL started")

	url := config.SolanaGlobalETLUrl

	scaledWaitSeconds := config.SlowETLFactor * config.SolanaGlobalETLWaitSeconds

	for {

		PostEmptyToSolanaGlobalETL(url)

		logger.Debug("SolanaGlobalETL sleeping for " + strconv.Itoa(scaledWaitSeconds) + " s")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}

}

func PostEmptyToSolanaGlobalETL(url string) {
	empty := models.EmptyRequestData{}

	body, err := json.Marshal(empty)

	if err != nil {
		logger.Error("Could not marshal empty request")
	}

	response, err := http.Post(
		url,
		"application/json",
		bytes.NewReader(body))

	if err != nil {
		logger.Error(fmt.Sprintf("HTTP post error - %+v", err))
	}

	decoder := json.NewDecoder(response.Body)
	var etlExecutionResponse models.ETLExecutionResponse

	if err := decoder.Decode(&etlExecutionResponse); err != nil {
		logger.Error("Could not decode execution response")
	}

	if etlExecutionResponse.Ok {
		logger.Info(fmt.Sprintf("[ETL] SolanaGlobal:: %+v", etlExecutionResponse))
	} else {
		logger.Error(fmt.Sprintf("[ETL] SolanaGlobal:: %+v", etlExecutionResponse))
	}
}
