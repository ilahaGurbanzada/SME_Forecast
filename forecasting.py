import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_revenue(df):
    df = df.copy()
    df['TimeIndex'] = np.arange(len(df))
    y = df['Net_Income'] if 'Net_Income' in df.columns else df.iloc[:, 1]
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

def generate_advice(forecast_df):
    trend = forecast_df['Forecast_Net_Income'].diff().mean()
    max_month = forecast_df.loc[forecast_df['Forecast_Net_Income'].idxmax(), 'Month']
    min_month = forecast_df.loc[forecast_df['Forecast_Net_Income'].idxmin(), 'Month']
    if trend > 0:
        return f"Доходы растут 📈. Рекомендуем вложиться в развитие в {max_month}. Следите за расходами в {min_month}."
    elif trend < 0:
        return f"Доходы снижаются 📉. Пересмотрите стратегию перед {min_month}. Попробуйте снизить издержки."
    else:
        return "Доходы стабильны. Поддерживайте текущую стратегию и следите за изменениями рынка."
