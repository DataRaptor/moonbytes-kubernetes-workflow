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

type EmptyRequest struct{}

func RunMagicEdenGlobalETL() {

	logger.Info("[ETL] 📦 MagicEdenGlobalETL started")

	url := config.MagicEdenGlobalETLUrl

	scaledWaitSeconds := config.SlowETLFactor * config.MagicEdenGlobalETLWaitSeconds

	for {

		PostEmptyToMagicEdenGlobalETL(url)

		logger.Debug("MagicEdenGlobalETL sleeping for " + strconv.Itoa(scaledWaitSeconds) + " s")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}

}

func PostEmptyToMagicEdenGlobalETL(url string) {
	empty := models.EmptyRequestData{}

	body, err := json.Marshal(empty)

	if err != nil {
		logger.Error("Could not mashal empty json body")
	}

	response, err2 := http.Post(
		url,
		"application/json",
		bytes.NewBuffer(body),
	)

	if err2 != nil {
		fmt.Printf("%+v", err)
		logger.Error(fmt.Sprintf("HTTP post error - %+v", err2))
	}

	decoder := json.NewDecoder(response.Body)
	var etlExecutionResponse models.ETLExecutionResponse

	if err := decoder.Decode(&etlExecutionResponse); err != nil {
		logger.Error("Could not decode execution response")
	}

	if etlExecutionResponse.Ok {
		logger.Info(fmt.Sprintf("[ETL] MagicEdenGlobal:: %+v", etlExecutionResponse))
	} else {
		logger.Error(fmt.Sprintf("[ETL] MagicEdenGlobal:: %+v", etlExecutionResponse))
	}
}
