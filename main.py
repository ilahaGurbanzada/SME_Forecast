import streamlit as st
from data_utils import load_data
from forecasting import forecast_revenue, generate_advice
from visuals import plot_revenue, plot_forecast

st.set_page_config(page_title="🤖 AI Прогноз Доходов", layout="wide")
st.title("📊 Прогноз доходов малого бизнеса с AI-помощником")

st.sidebar.header("🔧 Параметры анализа")
uploaded_file = st.sidebar.file_uploader("Загрузите CSV", type=["csv"])

if uploaded_file:
    df = load_data(uploaded_file)
    st.success("✅ Данные успешно загружены!")
    
    st.subheader("📈 Исторические доходы")
    st.plotly_chart(plot_revenue(df), use_container_width=True)

    st.subheader("🔮 Прогноз на 12 месяцев")
    forecast_df = forecast_revenue(df)
    st.plotly_chart(plot_forecast(forecast_df), use_container_width=True)

    st.subheader("💡 AI-рекомендации")
    st.info(generate_advice(forecast_df), icon="📌")

    with st.expander("📥 Скачать прогноз"):
        st.download_button("Скачать как CSV", forecast_df.to_csv(index=False), file_name="ai_forecast.csv")
else:
    st.warning("👈 Пожалуйста, загрузите CSV-файл слева для начала анализа.")
