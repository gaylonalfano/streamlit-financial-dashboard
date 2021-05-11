import streamlit as st

# import db


def main():
    st.subheader("wallstreetbets from dashboard/wallstreetbets.py with Postgres")

    # # Bind slider value to num_days variable to filter
    # num_days = st.sidebar.slider("Number of days", 1, 30, 3)

    # db.cursor.execute(
    #     """
    #     SELECT COUNT(*) AS num_mentions, symbol
    #     FROM mention JOIN stock ON stock.id = mention.stock_id
    #     WHERE date(dt) > current_date - interval '%s day'
    #     GROUP BY stock_id, symbol
    #     HAVING COUNT(symbol) > 10
    #     ORDER BY num_mentions DESC
    # """,
    #     (num_days,),
    # )

    # counts = db.cursor.fetchall()

    # for count in counts:
    #     st.write(count)

    # db.cursor.execute(
    #     """
    #     SELECT symbol, message, url, dt, username
    #     FROM mention JOIN stock ON stock.id = mention.stock_id
    #     ORDER BY dt DESC
    #     LIMIT 100
    # """
    # )

    # mentions = db.cursor.fetchall()

    # for mention in mentions:
    #     st.text(mention["dt"])
    #     st.text(mention["symbol"])
    #     st.text(mention["message"])
    #     st.text(mention["url"])
    #     st.text(mention["username"])

    # rows = db.cursor.fetchall()

    # st.write(rows)
