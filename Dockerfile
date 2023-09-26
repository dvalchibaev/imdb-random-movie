FROM ubuntu:latest
LABEL authors="alchibaevdv"

ENTRYPOINT ["top", "-b"]

FROM python:3.10.12

ENV VIRTUAL_ENV=venv
RUN python3 -m venv VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src .
