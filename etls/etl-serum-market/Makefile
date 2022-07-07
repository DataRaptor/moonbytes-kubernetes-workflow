env:
	python3 -m venv ./.venv 

ping:
	@echo "Pinging Service"
	python3 ./tests/ping.py

docker:
	@echo "🐋 Containerizing Service"
	docker build -t etl-serum-market . 
	docker run -t etl-serum-market -p 8080:8080