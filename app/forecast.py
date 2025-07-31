import pandas as pd

def forecast_demand(df: pd.DataFrame, periods: int) -> pd.Series:
    """Very basic moving average forecast."""
    if 'demand' not in df.columns:
        raise ValueError('CSV must contain a "demand" column')
    rolling = df['demand'].rolling(window=3, min_periods=1).mean()
    last_value = rolling.iloc[-1]
    forecast = pd.Series([last_value] * periods, name='forecast')
    return forecast
