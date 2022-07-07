package state

import (
	"encoding/json"
	"net/http"
	"time"
	"turbine/config"
	"turbine/pkg/models"
	"turbine/server/logger"
)

func GetSerumMarkets() []models.SerumMarket {

	url := config.StateUrl + "/turbine/serum/markets"

	transport := &http.Transport{
		MaxIdleConns:       10,
		IdleConnTimeout:    30 * time.Second,
		DisableCompression: true,
	}
	client := &http.Client{Transport: transport}

	request, err := http.NewRequest("GET", url, nil)

	if err != nil {
		logger.Error("pkg::state::GetSerumMarkets Could not instantiate serum markets request")
	}

	response, err := client.Do(request)
	if err != nil {
		logger.Error("pkg::state::GetSerumMarkets Could not get serum markets.")
	}

	decoder := json.NewDecoder(response.Body)
	var getSerumMarketsBody models.GetSerumMarketsBody

	if err := decoder.Decode(&getSerumMarketsBody); err != nil {
		logger.Error("pkg::state::GetSerumMarkets Could not decode.")
	}

	serumMarkets := getSerumMarketsBody.Data

	// logger.Info("pkg::state::GetSerumMarkets received " + strconv.Itoa(len(serumMarkets)) + " markets")

	return serumMarkets

}
