# NASDAQ RL Sample

This directory contains a minimal example for training a reinforcement learning agent on NASDAQ‑100 data using [FinRL](https://github.com/AI4Finance-Foundation/FinRL).

## Installation

Use [uv](https://github.com/astral-sh/uv) to create a virtual environment and install dependencies:

```bash
uv venv .venv
source .venv/bin/activate
uv pip install -r requirements.uv
```

## Training

Run the training script to download data from Yahoo Finance and train a PPO agent:

```bash
python train.py
```

The trained model is stored in `nasdaq_ppo.zip`.

## TradingView Client

`tradingview_client.py` provides a thin wrapper around `tradingview_ta` so you can query TradingView indicators for any NASDAQ ticker. Network access to TradingView may require additional configuration in restricted environments.
