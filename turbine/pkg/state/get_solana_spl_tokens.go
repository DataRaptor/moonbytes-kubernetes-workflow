package state

import (
	"encoding/json"
	"net/http"
	"time"
	"turbine/config"
	"turbine/pkg/models"
	"turbine/server/logger"
)

func GetSolanaSplTokens() []models.SolanaSplToken {

	url := config.StateUrl + "/turbine/serum/markets"

	transport := &http.Transport{
		MaxIdleConns:       10,
		IdleConnTimeout:    30 * time.Second,
		DisableCompression: true,
	}
	client := &http.Client{Transport: transport}

	request, err := http.NewRequest("GET", url, nil)

	if err != nil {
		logger.Error("pkg::state::GetSolanaSplTokensBody could not instantiate request")
	}

	response, err := client.Do(request)
	if err != nil {
		logger.Error("pkg::state::GetSolanaSplTokensBody get request failed")
	}

	decoder := json.NewDecoder(response.Body)
	var getSolanaSplTokensBody models.GetSolanaSplTokensBody

	if err := decoder.Decode(&getSolanaSplTokensBody); err != nil {
		logger.Error("pkg::state::GetSolanaSplTokensBody could not decode.")
	}

	serumMarkets := getSolanaSplTokensBody.Data

	// logger.Info("pkg::state::GetSerumMarkets received " + strconv.Itoa(len(serumMarkets)) + " markets")

	return serumMarkets

}
