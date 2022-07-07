package main

import (
	"time"
	"turbine/config"
	"turbine/pkg/etls"
	"turbine/pkg/jobs"
	"turbine/server/logger"
	"turbine/server/routes"
)

func StartTurbineLoop() {
	logger.Info("[gradient::gargantuan] turbine loop warming up")
	time.Sleep(5 * time.Second)
	logger.Info("[gradient::gargantuan] turbine loop started")

	// Run Jobs Concurrently
	if config.UpdateMagicEdenCollectionsJobEnabled {
		go jobs.UpdateMagicEdenCollections()
	}
	if config.UpdateSolanaSplTokensJobEnabled {
		go jobs.UpdateSolanaSplTokens()
	}
	if config.UpdateSerumMarketsJobEnabled {
		go jobs.UpdateSerumMarkets()
	}

	// Run ETLs Concurrently
	if config.MagicEdenCollectionMarketETLEnabled {
		go etls.RunMagicEdenCollectionMarketETL()
	}
	if config.MagicEdenCollectionXrayETLEnabled {
		go etls.RunMagicEdenCollectionXrayETL()
	}
	if config.MagicEdenGlobalETLEnabled {
		go etls.RunMagicEdenGlobalETL()
	}
	if config.SerumMarketETLEnabled {
		go etls.RunSerumMarketETL()
	}
	if config.SolanaGlobalETLEnabled {
		go etls.RunSolanaGlobalETL()
	}

	select {}
}

func main() {

	port := ":4201"
	logger.Init()
	router := routes.CreateRouter()
	logger.Info("👑 [gargantuan-turbine] started on port: " + port)
	go StartTurbineLoop()
	router.Run(port)

}
