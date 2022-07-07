package batching

func ChunkSlice(slice []interface{}, chunkSize int) [][]interface{} {
	var chunks [][]interface{}
	for i := 0; i < len(slice); i += chunkSize {
		end := i + chunkSize

		if end > len(slice) {
			end = len(slice)
		}

		chunks = append(chunks, slice[i:end])
	}

	return chunks
}
