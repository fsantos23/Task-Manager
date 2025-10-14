FROM python:3.12-slim

WORKDIR /app

RUN apt-get update

COPY . .

RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD [ "sh", "entrypoint.sh" ]