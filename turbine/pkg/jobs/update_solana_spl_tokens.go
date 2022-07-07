package jobs

import (
	"fmt"
	"time"
	"turbine/config"
	"turbine/pkg/state"
	"turbine/server/logger"
)

func UpdateSolanaSplTokens() {

	scaledWaitSeconds := config.SlowETLFactor * config.UpdateSolanaSplTokenJobWaitSeconds

	logger.Info("[Job] 🏗️ UpdateSolanaSplTokens started")

	for {

		status := state.PostUpdateSolanaSplTokens()

		// remove this later, when we implement the StateResponse.
		// right now we're going to just log the status so that go
		// doesn't bitch.

		fmt.Println(status)

		logger.Debug("UpdateSolanaSplTokens slowed")
		time.Sleep(time.Second * time.Duration(scaledWaitSeconds))

	}
}
