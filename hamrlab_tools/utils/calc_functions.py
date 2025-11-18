import numpy as np
import pandas as pd

def cagr(series):
    total_return = series.iloc[-1] / series.iloc[0] - 1
    years = len(series) / 252
    return (1 + total_return) ** (1/years) - 1

def max_drawdown(series):
    peak = series.expanding(min_periods=1).max()
    dd = (series - peak) / peak
    return dd.min()

def monthly_returns(df):
    return df.resample("M").ffill().pct_change()
