import plotly.graph_objects as go

def plot_revenue(df):
    y_col = 'Net_Income' if 'Net_Income' in df.columns else df.columns[1]
    fig = go.Figure()
    fig.add_trace(go.Scatter(y=df[y_col], mode='lines+markers', name='Доход'))
    fig.update_layout(title='Исторические доходы', template='plotly_white')
    return fig

def plot_forecast(forecast_df):
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=forecast_df['Month'],
        y=forecast_df['Forecast_Net_Income'],
        marker_color=forecast_df['Forecast_Net_Income'],
        name='Прогноз дохода'
    ))
    fig.add_trace(go.Scatter(
        x=forecast_df['Month'],
        y=forecast_df['Forecast_Net_Income'].rolling(3).mean(),
        mode='lines',
        name='Тренд',
        line=dict(color='black', dash='dash')
    ))
    fig.update_layout(title='Прогноз на 12 месяцев', template='plotly_white')
    return fig
