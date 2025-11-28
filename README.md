# ShikiBot - Shikimori Telegram Bot

> ### Before starting, you need to create a bot via [@BotFather](https://t.me/BotFather) in Telegram and follow the instructions

## Dependencies

1. Python 3
2. Docker
3. Docker Compose

## Installation

1. Clone the repository:

```bash
git clone git@github.com:ldfxxx404/ShikiBot.git
```

2. Configure Docker APT repository:

```bash
# Add Docker's official GPG key:
sudo apt update
sudo apt install -y ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/debian/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to APT sources:
sudo tee /etc/apt/sources.list.d/docker.list <<EOF
deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable
EOF

sudo apt update
```

3. Install Docker:

```bash
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

4. Start Docker service:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

---

## Build and Run

1. Change to the cloned repository:

```bash
cd ~/ShikiBot
```

### Manual Start

1. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r req.txt
```

3. Start the bot:

```bash
python src/main.py
```

### Start via Docker

1. Build Docker image:

```bash
docker build -t shiki .
```

2. Run Docker container:

```bash
docker run -d --name shiki shiki
```

### Start via Docker Compose

```bash
docker compose build
docker compose up -d
```
