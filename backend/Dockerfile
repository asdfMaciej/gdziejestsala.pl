FROM tiangolo/uvicorn-gunicorn-fastapi:python3.10-slim

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# This is needed - but it doesn't seem to work on a mounted volume
#   using a different approach by putting an empty .gitignore in /static/
# RUN mkdir -p /app/static 
# RUN chown -R 1000:1000 /app/static

EXPOSE 80

CMD ["/start-reload.sh"]