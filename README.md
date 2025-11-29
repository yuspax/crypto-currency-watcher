# Crypto-Currency-Watcher

Simple real-time monitoring of any cryptocurrency trading pair on Binance. Fetches the latest price every 10 seconds and prints it to the console.

## Quick Start

**With Docker (recommended):**

```bash
git clone https://github.com/yuspax/Crypto-Currency-Watcher.git

# Build image
docker build -t crypto-currency-watcher .

# Run
docker run --rm crypto-currency-watcher
```

**Local (without Docker):**

```bash
git clone https://github.com/yuspax/Crypto-Currency-Watcher.git
python main.py
```

## What It Does

Fetches the real-time price of a selected Binance trading pair (e.g., **BTCUSDT**, **ETHUSDT**) every 10 seconds:

```
[2025-11-29 21:10:00] BTCUSDT: 68952.12
[2025-11-29 21:10:10] BTCUSDT: 68948.90
[2025-11-29 21:10:20] BTCUSDT: 68955.33
```

## Configuration

Edit the trading pair in `main.py`:

```python
symbol = "BTCUSDT"
```

Then restart:

```bash
docker run --rm crypto-currency-watcher
# or run main.py locally
```

## Useful Commands

**Docker:**

```bash
docker build -t crypto-currency-watcher .   # Build
docker run --rm crypto-currency-watcher     # Run
```

**Local:**

```bash
python main.py                              # Run locally
```

## Structure

```
Crypto-Currency-Watcher/
├── main.py          # Main script
├── Dockerfile       # Docker image
└── requirements.txt # Dependencies 
```
