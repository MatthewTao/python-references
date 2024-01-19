# There are various ones to choose from
# python:3.11-slim-bookworm
# python:3.12-slim
# The official base ones are not too bad in any case
FROM python:3.12

WORKDIR /app

COPY entry.sh /app/entry.sh

COPY requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

CMD [ "bash", "entry.sh" ]
