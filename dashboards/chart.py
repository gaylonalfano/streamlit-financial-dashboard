import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# import db


def main():
    st.write("This is the charts.py simple text")
    # symbol = st.sidebar.text_input(
    #     "Symbol", value="MSFT", max_chars=None, key=None, type="default"
    # )

    # data = pd.read_sql(
    #     """
    #     select date(day) as day, open, high, low, close
    #     from daily_bars
    #     where stock_id = (select id from stock where UPPER(symbol) = %s)
    #     order by day asc""",
    #     db.connection,
    #     params=(symbol.upper(),),
    # )

    # st.subheader(symbol.upper())

    # fig = go.Figure(
    #     data=[
    #         go.Candlestick(
    #             x=data["day"],
    #             open=data["open"],
    #             high=data["high"],
    #             low=data["low"],
    #             close=data["close"],
    #             name=symbol,
    #         )
    #     ]
    # )
    # Exclude weekends using type=category
    # fig.update_xaxes(type="category")
    # fig.update_layout(height=700)

    # st.plotly_chart(fig, use_container_width=True)

    # st.write(data)
