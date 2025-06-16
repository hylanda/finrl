"""Example training script for NASDAQ-100 stocks using FinRL."""
from __future__ import annotations

import pandas as pd
from finrl.meta.data_processor import DataProcessor
from finrl.meta.env_stock_trading.env_stocktrading_np import StockTradingEnv
from finrl.config_tickers import NAS_100_TICKER
from finrl.config import INDICATORS
from stable_baselines3 import PPO
from stable_baselines3.common.vec_env import DummyVecEnv


START_DATE = "2018-01-01"
END_DATE = "2020-12-31"


def create_env() -> DummyVecEnv:
    dp = DataProcessor("yahoofinance")
    data = dp.download_data(NAS_100_TICKER, START_DATE, END_DATE, "1D")
    data = dp.clean_data(data)
    data = dp.add_technical_indicator(data, INDICATORS)
    data = dp.add_vix(data)
    price_array, tech_array, turbulence_array = dp.df_to_array(data, if_vix=True)
    env_config = {
        "price_array": price_array,
        "tech_array": tech_array,
        "turbulence_array": turbulence_array,
        "if_train": True,
    }
    return DummyVecEnv([lambda: StockTradingEnv(config=env_config)])


def train_agent() -> None:
    env = create_env()
    model = PPO("MlpPolicy", env, verbose=1)
    model.learn(total_timesteps=10_000)
    model.save("nasdaq_ppo")


if __name__ == "__main__":
    train_agent()
