package batching

import "sync"

type convert func(string) (bool, error)

func BatchExecuteRequests(urls []string, executeRequest convert) ([]bool, error) {
	batchCh := make(chan bool)
	errs := make(chan error)
	responses := []bool{}

	var wg sync.WaitGroup
	for _, url := range urls {
		wg.Add(1)
		go func(url string) {
			defer wg.Done()
			resps, err := executeRequest(url)
			if err != nil {
				errs <- err
				return
			}
			batchCh <- resps
		}(url)
	}

	go func() {
		wg.Wait()
		close(batchCh)
	}()

	for resps := range batchCh {
		responses = append(responses, resps)
	}

	select {
	case err := <-errs:
		return nil, err
	default:
		return responses, nil
	}
}
