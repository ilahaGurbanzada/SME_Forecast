import streamlit as st
from data_utils import load_data
from forecasting import forecast_revenue
from visuals import plot_revenue, plot_forecast

st.set_page_config(page_title="SME Revenue Forecast", layout="wide")
st.title("📈 Прогнозирование доходов малого бизнеса")

uploaded_file = st.file_uploader("Загрузите CSV с финансовыми данными", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.subheader("📊 Визуализация доходов")
    st.plotly_chart(plot_revenue(df), use_container_width=True)

    st.subheader("🔮 Прогноз доходов")
    forecast_df = forecast_revenue(df)
    st.plotly_chart(plot_forecast(forecast_df), use_container_width=True)

    with st.expander("📥 Скачать прогноз"):
        st.download_button("Скачать как CSV", forecast_df.to_csv(index=False), file_name="forecast.csv")
