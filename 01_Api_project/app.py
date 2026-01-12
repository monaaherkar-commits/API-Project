import streamlit as st
from utils import StockAPI
st.set_page_config(page_title="Stock Market Project")
@st.cache_resource
def get_stock_client():
    return StockAPI()   

client = StockAPI()

@st.cache_data
def get_company_symbol(company: str):
    return client.get_symbol(company)

@st.cache_data
def get_stock_data(symbol: str):
    return client.get_daily_prices(symbol)  


st.title("Stock Market Project")
st.subheader("by Mona Aherkar")

company = st.text_input("Enter Company Name: ")

if company:
    search_df = client.get_symbol(company)
    symbols = search_df["1. symbol"].tolist()
    sel_symbol = st.selectbox("Select Symbol:", options=symbols)
    sel_df = search_df[search_df["1. symbol"] == sel_symbol]
    st.dataframe(sel_df)

    button = st.button("Plot chart", type="primary")
    if button:
        stock_df = client.get_daily_prices(sel_symbol)
        st.dataframe(stock_df.head())
        fig = client.plot_candlestick(stock_df)
        st.plotly_chart(fig)
        




