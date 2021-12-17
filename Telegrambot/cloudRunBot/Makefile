include params.mk

# DEFINED VARIABLES:
	# SHIRT_POROCESSING_ADDRESS
	# TELEGRAM_TOKEN
	# GCLOUD_PROJECT_ID
	# CONTAINER_NAME
	# PORT
	# CONFIG_FILE

.DEFAULT_GOAL := deploy-gcloud

deploy-gcloud: ## Deploys code to gcloud and links telegram bot to deployed instance
	gcloud beta run deploy bot --source . --set-env-vars TOKEN=$(TELEGRAM_TOKEN),SHIRT_POROCESSING_ADDRESS=${SHIRT_POROCESSING_ADDRESS},CONFIG_FILE=${CONFIG_FILE} --platform managed --allow-unauthenticated --project $(GCLOUD_PROJECT_ID)
	SERVICE_URL="$(shell gcloud run services describe bot --format 'value(status.url)' --project $(GCLOUD_PROJECT_ID))"; \
	curl "https://api.telegram.org/bot${TELEGRAM_TOKEN}/setWebhook?url="$$SERVICE_URL

run-container: ## Builds the container and runs it locally
	docker build -t schmivin/$(CONTAINER_NAME) .
	-docker stop $(CONTAINER_NAME)
	-docker rm $(CONTAINER_NAME)
	docker run --env PORT=$(PORT) --env SHIRT_POROCESSING_ADDRESS=$(SHIRT_POROCESSING_ADDRESS) --env TOKEN=$(TELEGRAM_TOKEN) --env CONFIG_FILE=${CONFIG_FILE} --name $(CONTAINER_NAME) -d schmivin/$(CONTAINER_NAME)
	# docker exec -t -i $(CONTAINER_NAME) /bin/bash

run-locally: ## Runs app localy without container
	uvicorn main:app --reload --port 5000

.PHONY: help

help:  ## Display this help
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m\033[0m\n"} /^[a-zA-Z_-]+:.*?##/ { printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)
