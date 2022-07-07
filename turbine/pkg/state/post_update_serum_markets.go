package state

import (
	"fmt"
	"net/http"
	"turbine/config"
	"turbine/server/logger"
)

func PostUpdateSerumMarkets() bool {

	url := config.StateUrl + "/turbine/serum/markets/update"

	response, err := http.Post(
		url,
		"application/json",
		nil,
	)

	if err != nil {
		logger.Error(fmt.Sprintf("HTTP post error - %+v", err))
	}

	if response.StatusCode != 200 {
		logger.Error("Failed to update SerumMarket markets update")
	}

	// TODO parse the response body to a models.StateResponse (not needed for now)
	return true

}
