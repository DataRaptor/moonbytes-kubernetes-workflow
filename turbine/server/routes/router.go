package routes

import (
	"github.com/gin-gonic/gin"
	"github.com/zsais/go-gin-prometheus"
)

func CreateRouter() *gin.Engine {

	router := gin.Default()

	router.ForwardedByClientIP = true

	metrics := ginprometheus.NewPrometheus("gin")
	metrics.Use(router)

	return router

}
