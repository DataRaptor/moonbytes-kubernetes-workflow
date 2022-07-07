package models

type GetSolanaSplTokensBody struct {
	Ok   bool             `json:"ok"`
	Data []SolanaSplToken `json:"data"`
}

type SolanaSplToken struct {
	Symbol string `json:"symbol"`
	Mint   string `json:"mint"`
}
