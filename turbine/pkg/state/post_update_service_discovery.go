package state

import (
	"fmt"
	"net/http"
	"turbine/config"
	"turbine/server/logger"
)

func PostUpdateServiceDiscovery() bool {

	url := config.StateUrl + "/turbine/services/discovery/update"

	response, err := http.Post(
		url,
		"application/json",
		nil,
	)

	if err != nil {
		fmt.Println(err)
		logger.Error(fmt.Sprintf("HTTP post error - %+v", err))
	}

	if response.StatusCode != 200 {
		logger.Error(fmt.Sprintf("%+v", response))
		logger.Error("Failed to update service discovery")
	}

	// TODO parse the response body to a models.StateResponse (not needed for now)
	return true

}
