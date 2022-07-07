env:
	python3 -m venv ./.venv 

ping:
	@echo "Pinging Service"
	python3 ./tests/ping.py

docker:
	@echo "🐋 Containerizing Service"
	docker build -t etl-magic-eden-collection-xray . 
	docker run -t etl-magic-eden-collection-xray -p 8080:8080