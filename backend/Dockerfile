FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

RUN mkdir -p /app/static 
RUN chown -R 1000:1000 /app/static

CMD ["/start-reload.sh"]