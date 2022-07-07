package jobs

import (
	"fmt"
	"time"
	"turbine/config"
	"turbine/pkg/state"
	"turbine/server/logger"
)

func UpdateSerumMarkets() {

	scaledWaitSeconds := config.SlowETLFactor * config.UpdateSerumMarketsJobWaitSeconds

	logger.Info("[Job] 🏗️ UpdateSerumMarketsJob started")

	for {

		status := state.PostUpdateSerumMarkets()

		// remove this later, when we implement the StateResponse.
		// right now we're going to just log the status so that go
		// doesn't bitch.

		fmt.Println(status)

		logger.Debug("UpdateSerummarket slowed")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}
}
