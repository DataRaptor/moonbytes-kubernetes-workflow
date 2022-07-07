package models

type EmptyRequestData struct{}

type StateResponse struct {
	Ok      bool   `json:"ok"`
	Message string `json:"message"`
}

type ETLExecutionResponse struct {
	Ok            bool   `json:"ok"`
	Message       string `json:"message"`
	ModelWritten  int    `json:"models_written"`
	PointsWritten int    `json:"points_written"`
}
