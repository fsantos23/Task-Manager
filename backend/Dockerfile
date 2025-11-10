FROM python:3.12-slim

WORKDIR /app

RUN apt-get update

# only for production
# COPY . .

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

CMD [ "sh", "entrypoint.sh" ]