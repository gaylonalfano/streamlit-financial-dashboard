import streamlit as st

# import db


def main():
    st.subheader("https://github.com/hackingthemarkets/timescaledb-aiohttp-asyncpg")
    # pattern = st.sidebar.selectbox("Which Pattern?", ("engulfing", "threebar"))

    # if pattern == "engulfing":
    #     db.cursor.execute(
    #         """
    #         SELECT *
    #         FROM (
    #             SELECT day, open, close, stock_id, symbol,
    #             LAG(close, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_close,
    #             LAG(open, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_open
    #             FROM daily_bars
    #             JOIN stock ON stock.id = daily_bars.stock_id
    #         ) a
    #         WHERE previous_close < previous_open AND close > previous_open AND open < previous_close
    #         AND day = '2021-02-18'
    #     """
    #     )

    # if pattern == "threebar":
    #     db.cursor.execute(
    #         """
    #         SELECT *
    #         FROM (
    #             SELECT day, close, volume, stock_id, symbol,
    #             LAG(close, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_close,
    #             LAG(volume, 1) OVER ( PARTITION BY stock_id ORDER BY day ) previous_volume,
    #             LAG(close, 2) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_close,
    #             LAG(volume, 2) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_volume,
    #             LAG(close, 3) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_previous_close,
    #             LAG(volume, 3) OVER ( PARTITION BY stock_id ORDER BY day ) previous_previous_previous_volume
    #         FROM daily_bars
    #         JOIN stock ON stock.id = daily_bars.stock_id) a
    #         WHERE close > previous_previous_previous_close
    #             AND previous_close < previous_previous_close
    #             AND previous_close < previous_previous_previous_close
    #             AND volume > previous_volume
    #             AND previous_volume < previous_previous_volume
    #             AND previous_previous_volume < previous_previous_previous_volume
    #             AND day = '2021-02-19'
    #     """
    #     )

    # rows = db.cursor.fetchall()

    # for row in rows:
    #     st.image(f"https://finviz.com/chart.ashx?t={row['symbol']}")
