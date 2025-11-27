FROM alpine:latest

RUN apk update && \
 apk add --no-cache python3 py3-pip

WORKDIR /app

COPY . .

RUN python3 -m venv .Shiki && \
source .Shiki/bin/activate && \ 
pip install --no-cache -r req.txt
