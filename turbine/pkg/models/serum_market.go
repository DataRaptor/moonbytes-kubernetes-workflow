package models

type GetSerumMarketsBody struct {
	Ok   bool          `json:"ok"`
	Data []SerumMarket `json:"data"`
}

type SerumMarket struct {
	Address     string `json:"address"`
	ProgramId   string `json:"program_id"`
	BaseSymbol  string `json:"base_symbol"`
	QuoteSymbol string `json:"quote_symbol"`
}
