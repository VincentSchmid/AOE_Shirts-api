server:
	-git pull
	-pkill gunicorn
	gunicorn shirt_processing_api:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --daemon
