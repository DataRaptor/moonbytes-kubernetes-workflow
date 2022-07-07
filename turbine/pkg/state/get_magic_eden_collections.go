package state

import (
	"encoding/json"
	"net/http"
	"time"
	"turbine/config"
	"turbine/pkg/models"
	"turbine/server/logger"
)

func GetMagicEdenCollections() []models.MagicEdenCollection {

	// logger.Info("pkg::state::GetMagicEdenCollections started")

	url := config.StateUrl + "/turbine/magic_eden/collections"

	transport := &http.Transport{
		MaxIdleConns:       10,
		IdleConnTimeout:    30 * time.Second,
		DisableCompression: true,
	}
	client := &http.Client{Transport: transport}

	request, err := http.NewRequest("GET", url, nil)

	if err != nil {
		logger.Error("pkg::state::GetMagicEdenCollections Could not instantiate magic_eden collections request")
	}

	response, err := client.Do(request)
	if err != nil {
		logger.Error("pkg::state::GetMagicEdenCollections Could not get magic_eden collections.")
	}

	decoder := json.NewDecoder(response.Body)
	var getMagicEdenCollectionsBody models.GetMagicEdenCollectionsBody

	if err := decoder.Decode(&getMagicEdenCollectionsBody); err != nil {
		logger.Error("pkg::state::GetMagicEdenCollections Could not decode.")
	}

	magicEdenCollections := getMagicEdenCollectionsBody.Data

	// logger.Info("pkg::state::GetMagicEdenCollections received " + strconv.Itoa(len(magicEdenCollections)) + " collections")

	return magicEdenCollections

}
