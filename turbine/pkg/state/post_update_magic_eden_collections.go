package state

import (
	"fmt"
	"net/http"
	"turbine/config"
	"turbine/server/logger"
)

func PostUpdateMagicEdenCollections() bool {

	url := config.StateUrl + "/turbine/magic_eden/collections/update"

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
		logger.Error("Failed to update MagicEdenCollection")
	}

	// TODO parse the response body to a models.StateResponse (not needed for now)
	return true

}
