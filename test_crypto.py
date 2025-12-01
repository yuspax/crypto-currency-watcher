import pytest
from main import get_binance_price
import os

def test_get_binance_price_returns_float():
    price = get_binance_price()
    if price is not None:
        assert isinstance(price, float)
        assert price > 0

def test_symbol_env_variable(monkeypatch):
    monkeypatch.setenv('SYMBOL', 'ETHUSDT')
    from main import SYMBOL
    assert SYMBOL == 'ETHUSDT'
