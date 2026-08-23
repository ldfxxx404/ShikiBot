FROM alpine:latest AS builder

RUN apk add --no-cache \
    python3 \
    py3-pip \
    python3-dev \
    build-base

WORKDIR /app

COPY req.txt .

RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r req.txt


FROM alpine:latest

RUN apk add --no-cache python3

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv
COPY . .

ENV PATH="/opt/venv/bin:$PATH"

CMD ["python", "src/main.py"]
