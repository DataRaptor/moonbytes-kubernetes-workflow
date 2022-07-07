default:
	make dev

.PHONY: new
new:
	make clean
	make dev

.PHONY: setup
setup:
	make install-kompose
	make install-kind

.PHONY: workers
workers:
	python3 ./workers/service_discovery/main.py & 

.PHONY: kill
kill:
	docker kill $(docker ps -q)

.PHONY: clean
clean:
	docker container prune -f 
	docker image prune -f
	docker system prune -f
	docker volume prune -f 

.PHONY: purge
purge:
	# make uninstall-helm-charts
	docker container prune -f 
	docker image prune -f -a
	docker system prune -f -a
	docker volume prune -f 

.PHONY: dev
dev:
	docker-compose up --build --remove-orphans

.PHONY: start
	docker-compose up --build --remove-orphans


.PHONY: kubernetes
kubernetes:
	# make create-kubernetes-cluster
	make build-docker-images
	make create-cluster-docker-image-registry
	make push-docker-images-to-cluster-registry
	make install-helm-charts

.PHONY: update-kubernetes
update-kubernetes:
	make build-docker-images
	make push-docker-images-to-cluster-registry
	make uninstall-helm-charts
	make install-helm-charts

.PHONY: install-kompose
install-kompose:
	curl -L https://github.com/kubernetes/kompose/releases/download/v1.26.0/kompose-darwin-amd64 -o kompose
	chmod +x kompose
	sudo mv ./kompose /usr/local/bin/kompose

.PHONY: install-kind
install-kind:
	go install sigs.k8s.io/kind@v0.12.0 

.PHONY: helm
helm:
	make production-env
	kompose convert -f docker-compose.yaml -o ./kubernetes -c --multiple-container-mode
	make development-env
	python3 ./scripts/apply_helm_values.py

.PHONY: production-env
production-env:
	python3 ./scripts/toggle_docker_compose_to_production.py

.PHONY: development-env
development-env:
	python3 ./scripts/toggle_docker_compose_to_development.py

.PHONY: create-kubernetes-cluster
create-kubernetes-cluster:
	kind create cluster

.PHONY: build-docker-images
build-docker-images:
	docker build -f ./api/Dockerfile ./api -t gargantuan/api
	docker build -f ./client/Dockerfile ./client -t gargantuan/client
	docker build -f ./turbine/Dockerfile ./turbine -t gargantuan/turbine
	docker build -f ./state/Dockerfile ./state -t gargantuan/state
	docker build -f ./serum/Dockerfile ./serum -t gargantuan/serum
	docker build -f ./etls/etl-magic-eden-collection-market/Dockerfile ./etls/etl-magic-eden-collection-market -t gargantuan/etl-magic-eden-collection-market
	docker build -f ./etls/etl-magic-eden-collection-xray/Dockerfile ./etls/etl-magic-eden-collection-xray -t gargantuan/etl-magic-eden-collection-xray
	docker build -f ./etls/etl-magic-eden-global/Dockerfile ./etls/etl-magic-eden-global -t gargantuan/etl-magic-eden-global
	docker build -f ./etls/etl-serum-market/Dockerfile ./etls/etl-serum-market -t gargantuan/etl-serum-market
	docker build -f ./etls/etl-solana-global/Dockerfile ./etls/etl-solana-global -t gargantuan/etl-solana-global

.PHONY: create-cluster-docker-image-registry
create-cluster-docker-image-registry:
	./docker/create_image_registry.sh

.PHONY: push-docker-images-to-cluster-registry
push-docker-images-to-cluster-registry:
	docker tag gargantuan/api localhost:5001/gargantuan/api
	docker tag gargantuan/client localhost:5001/gargantuan/client
	docker tag gargantuan/turbine localhost:5001/gargantuan/turbine
	docker tag gargantuan/state localhost:5001/gargantuan/state
	docker tag gargantuan/serum localhost:5001/gargantuan/serum
	docker tag gargantuan/etl-magic-eden-collection-market localhost:5001/gargantuan/etl-magic-eden-collection-market 
	docker tag gargantuan/etl-magic-eden-collection-xray localhost:5001/gargantuan/etl-magic-eden-collection-xray 
	docker tag gargantuan/etl-magic-eden-global localhost:5001/gargantuan/etl-magic-eden-global 
	docker tag gargantuan/etl-serum-market localhost:5001/gargantuan/etl-serum-market 
	docker tag gargantuan/etl-solana-global localhost:5001/gargantuan/etl-solana-global 

	docker push localhost:5001/gargantuan/api
	docker push localhost:5001/gargantuan/client
	docker push localhost:5001/gargantuan/turbine
	docker push localhost:5001/gargantuan/state
	docker push localhost:5001/gargantuan/serum
	docker push localhost:5001/gargantuan/etl-magic-eden-collection-market
	docker push localhost:5001/gargantuan/etl-magic-eden-collection-xray 
	docker push localhost:5001/gargantuan/etl-magic-eden-global 
	docker push localhost:5001/gargantuan/etl-serum-market 
	docker push localhost:5001/gargantuan/etl-solana-global 

.PHONY: list-docker-images-loaded-to-cluster
list-docker-images-loaded-to-cluster:
	docker exec -it kind-control-plane crictl images

.PHONY: install-helm-charts
install-helm-charts:
	helm install gargantuan ./kubernetes

.PHONY: uninstall-helm-charts
uninstall-helm-charts:
	helm uninstall gargantuan

.PHONY: get-cluster-pods
get-cluster-pods:
	kubectl get pods

.PHONY: watch-kubernetes
watch-kubernetes:
	watch make get-cluster-pods

.PHONY: get-cluster-services
get-cluster-services:
	kubectl get services
