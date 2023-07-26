##########################################
install:
	@sudo apt-get update -y
	@sudo apt-get install -y git g++ gcc pkg-config make cmake m4 libgmp-dev libsodium-dev libsecp256k1-dev
	@pip install --upgrade pip==23.1.2
	@pip install poetry==1.5.1
	@poetry env info
	@poetry install
##########################################
aleph-install:
	@pip install eth_account aleph-client
	@aleph whoami
	@aleph --install-completion
aleph-who-am-i:
	@aleph whoami
aleph-in-docker:
	@docker run --rm -ti -v $(pwd)/data:/data ghcr.io/aleph-im/aleph-client/aleph-client:master --help
##########################################
run-docker:
	@docker-compose down
	@docker rmi -f aleph-vortex-app-indexer
	@docker-compose up -d
##########################################
run:
	@poetry run uvicorn main:app
##########################################