import pandas as pd
from typing import Dict

def compute_inventory_parameters(forecast: pd.Series, df: pd.DataFrame, lead_time: int = 1, service_level: float = 0.95) -> Dict[str, float]:
    """Compute simple safety stock and reorder point."""
    demand_std = df['demand'].std()
    safety_stock = demand_std * (lead_time ** 0.5) * service_level
    reorder_point = forecast.iloc[0] * lead_time + safety_stock
    return {
        'safety_stock': round(safety_stock, 2),
        'reorder_point': round(reorder_point, 2),
    }
