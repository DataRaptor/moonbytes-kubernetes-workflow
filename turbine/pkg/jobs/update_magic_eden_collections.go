package jobs

import (
	"fmt"
	"time"
	"turbine/config"
	"turbine/pkg/state"
	"turbine/server/logger"
)

func UpdateMagicEdenCollections() {

	scaledWaitSeconds := config.SlowETLFactor * config.UpdateMagicEdenCollectionsJobWaitSeconds

	logger.Info("[Job] 🏗️ UpdateMagicEdenCollectionsJob started")

	for {

		status := state.PostUpdateMagicEdenCollections()

		// remove this later, when we implement the StateResponse.
		// right now we're going to just log the status so that go
		// doesn't bitch.

		fmt.Println(status)

		logger.Debug("UpdateMagicEdenCollections slowed")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}
}
