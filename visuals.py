import plotly.express as px

def plot_revenue(df):
    y_col = 'Net_Income' if 'Net_Income' in df.columns else df.columns[1]
    fig = px.line(df, y=y_col, title="Исторические доходы", markers=True)
    fig.update_layout(template="plotly_white")
    return fig

def plot_forecast(forecast_df):
    fig = px.bar(forecast_df, x='Month', y='Forecast_Net_Income', title="Прогноз на 12 месяцев", color='Forecast_Net_Income')
    fig.update_layout(template="plotly_white")
    return fig
