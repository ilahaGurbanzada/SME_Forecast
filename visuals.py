import plotly.express as px

def plot_revenue(df):
    y_col = 'Net_Income' if 'Net_Income' in df.columns else df.columns[1]
    fig = px.line(df, y=y_col, title="Доход по времени")
    return fig

def plot_forecast(forecast_df):
    fig = px.bar(forecast_df, x='Month', y='Forecast_Net_Income', title="Прогноз доходов")
    return fig
