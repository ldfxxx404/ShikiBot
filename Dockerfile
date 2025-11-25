FROM alpine:latest

RUN apk add --no-cache python3 py3-pip bash curl uv

WORKDIR /app

COPY . .

CMD ["uv", "run", "src/main.py"]
