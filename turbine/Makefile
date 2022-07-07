default:
	make dev

dev:
	go run ./server/main.go

docker:
	docker build -t turbine .
	docker run -p 8080:8080 -t turbine

build:
	go build -o ./turbine ./server/main.go 

start:
	./turbine