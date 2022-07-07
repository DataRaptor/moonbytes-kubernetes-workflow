env:
	python3 -m venv ./.venv 

ping:
	@echo "Pinging Service"
	python3 ./tests/ping.py

test:
	pytest ./tests/*

docker:
	@echo "🐋 Containerizing Service"
	docker build -t etl-magic-eden-global . 
	docker run -t etl-magic-eden-global -p 8080:8080