#!/bin/bash

exec gunicorn shirt_processing_api:app --workers $NUM_WORKERS --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:${PORT}