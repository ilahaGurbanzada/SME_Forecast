import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_revenue(df):
    df = df.copy()
    df['TimeIndex'] = np.arange(len(df))
    if 'Net_Income' in df.columns:
        y = df['Net_Income']
    else:
        y = df.iloc[:, 1]  # fallback
    X = df[['TimeIndex']]
    model = LinearRegression()
    model.fit(X, y)
    future_periods = 12
    future_X = pd.DataFrame({'TimeIndex': np.arange(len(df), len(df)+future_periods)})
    future_y = model.predict(future_X)
    forecast_df = pd.DataFrame({
        'Month': [f'Месяц {i+1}' for i in range(future_periods)],
        'Forecast_Net_Income': future_y
    })
    return forecast_df
