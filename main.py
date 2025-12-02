import time
import requests
import os
import sys

SYMBOL = os.getenv('SYMBOL', 'ETHUSDT').upper()

def get_binance_price():
    url = "https://api.binance.com/api/v3/ticker/price"
    params = {'symbol': SYMBOL}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        price = float(data['price'])
        return price
    except requests.exceptions.HTTPError as err:
        print(f"HTTP Error: {err} (Check if symbol '{SYMBOL}' exists)", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return None

def main():
    print(f"Starting Tracker for: {SYMBOL}...")
    while True:
        price = get_binance_price()
        if price:
            print(f"[{time.strftime('%H:%M:%S')}] {SYMBOL} Price: ${price:,.2f}")
        time.sleep(10)

if __name__ == "__main__":
    main()