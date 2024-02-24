FROM python:3.10-slim-buster

EXPOSE 8501


RUN apt-get update && apt install awscli -y

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "streamlit","run","app.py","--server.port-8501","--server.address=0.0.0" ]



