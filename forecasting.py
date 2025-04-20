import pandas as pd
import numpy as np

def forecast_revenue(df):
    # Генерируем реалистичный ручной сценарий (имитация)
    forecast_values = [4.5, 3.7, 4.0, 4.2, 3.8, 4.3, 4.6, 4.4, 4.9, 5.0, 4.7, 5.2]
    forecast_df = pd.DataFrame({
        'Month': [f'Месяц {i+1}' for i in range(12)],
        'Forecast_Net_Income': forecast_values
    })
    return forecast_df

def generate_advice(forecast_df):
    diffs = forecast_df['Forecast_Net_Income'].diff()
    trend = diffs.mean()
    max_val = forecast_df['Forecast_Net_Income'].max()
    min_val = forecast_df['Forecast_Net_Income'].min()
    max_month = forecast_df.loc[forecast_df['Forecast_Net_Income'] == max_val, 'Month'].values[0]
    min_month = forecast_df.loc[forecast_df['Forecast_Net_Income'] == min_val, 'Month'].values[0]

    advice = ""
    if trend > 0:
        advice += f"✅ В целом, наблюдается восходящий тренд (+{trend:.2f} млн в среднем).\n"
    else:
        advice += f"⚠️ Внимание: общая динамика отрицательная ({trend:.2f} млн).\n"

    drop_moments = forecast_df[diffs < -0.5]
    if not drop_moments.empty:
        month = drop_moments.iloc[0]['Month']
        amount = drop_moments.iloc[0]['Forecast_Net_Income']
        advice += f"📉 В {month} зафиксировано резкое падение дохода до {amount:.2f} млн.\n"
        advice += "💡 Рекомендуем: увеличить маркетинг, пересмотреть затраты, усилить клиентскую лояльность.\n"

    advice += f"🔺 Максимум ожидается в {max_month} ({max_val:.2f} млн), минимум — в {min_month} ({min_val:.2f} млн)."

    return advice
