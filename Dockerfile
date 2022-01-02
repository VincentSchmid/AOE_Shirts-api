FROM python:3.8-slim
WORKDIR /app
ENV PYTHONUNBUFFERED True \
    PORT \
    NUM_WORKERS

EXPOSE ${PORT}

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt -f https://download.pytorch.org/whl/cpu/torch_stable.html

COPY src src
COPY [\
    "shirt_processing_api.py", \
    "entrypoint.sh", \
    "./"]

RUN chmod +x ./entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]