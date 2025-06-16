"""Simple TradingView client using `tradingview_ta` for analysis."""
from __future__ import annotations

from tradingview_ta import TA_Handler, Interval

class TradingViewClient:
    """Wrapper around :mod:`tradingview_ta` to fetch indicators."""

    def __init__(self, symbol: str, exchange: str = "NASDAQ", screener: str = "america", interval: Interval = Interval.INTERVAL_1_DAY) -> None:
        self.handler = TA_Handler(symbol=symbol, exchange=exchange, screener=screener, interval=interval)

    def get_analysis(self) -> dict:
        """Return raw indicator analysis from TradingView."""
        analysis = self.handler.get_analysis()
        return analysis.indicators
