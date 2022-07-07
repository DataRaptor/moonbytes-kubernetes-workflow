package models

type GetMagicEdenCollectionsBody struct {
	Ok   bool                  `json:"ok"`
	Data []MagicEdenCollection `json:"data"`
}

type MagicEdenCollection struct {
	Symbol  string `json:"symbol"`
	Twitter string `json:"twitter"`
}
