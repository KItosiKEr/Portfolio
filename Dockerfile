FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ADD ./requirements.txt .
ADD ./entrypoint.sh .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt

ADD . .