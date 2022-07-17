before-run:
	sudo apt-get update
	sudo apt-get install build-essential gcc make

install:
	sudo apt install -y python3-pip libssl-dev libffi-dev python3-dev gunicorn
	pip install gunicorn gdown
	mkdir ~/.u2net
	cd ~/.u2net && gdown https://drive.google.com/uc?id=1ao1ovG1Qtx4b7EoskHXmi2E9rp5CHLcZ

server:
	-git pull
	-pkill gunicorn
	gunicorn shirt_processing_api:app --workers 2 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 --daemon
