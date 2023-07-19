# ##########################################
# install-linux:
# 	@sudo apt-get update -y
# 	@sudo apt-get install -y git g++ gcc pkg-config make cmake m4 libgmp-dev libsodium-dev libsecp256k1-dev
# 	@pip install --upgrade pip==23.1.2
# 	@pip install fastapi uvicorn
# 	@pip install eth_account aleph-client
# 	@aleph whoami
# 	@aleph --install-completion

# install-macos:
# 	@brew tap cuber/homebrew-libsecp256k1
# 	@brew install libsecp256k1 squashfs
# 	@pip install --upgrade pip==23.1.2
# 	@pip install eth_account aleph-client
# 	@aleph whoami
# 	@aleph --install-completion
# ##########################################
# test-linux:
# 	@vagrant up --provider=docker --provision
# 	@vagrant ssh
# 	# @uvicorn main:app --reload --host=0.0.0.0

# test-macos:
# 	@vagrant up --provider=docker --provision
# 	@vagrant ssh
# 	# @uvicorn main:app --reload --host=0.0.0.0

# test-stop:
# 	@vagrant halt
# ##########################################
# aleph-who-am-i:
# 	@aleph whoami

# aleph-in-docker:
# 	@docker run --rm -ti -v $(pwd)/data:/data ghcr.io/aleph-im/aleph-client/aleph-client:master --help
# ##########################################
run-docker:
	@clear && docker-compose down && docker rmi -f aleph-vortex-app-indexer && docker-compose up
# ##########################################
# run:
# 	@rm -rf data/*
# 	@poetry run uvicorn main:app