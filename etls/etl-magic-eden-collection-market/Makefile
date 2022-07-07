env:
	python3 -m venv ./.venv 

ping:
	@echo "Pinging Service"
	python3 ./tests/ping.py

docker-compose:
	@echo "🐋 Docker-Composing Services"
	docker-compose up --build 

docker:
	@echo "🐋 Containerizing Service"
	docker build -t etl-magic-eden-collection-market . 
	docker run -t etl-magic-eden-collection-market -p 8080:8080