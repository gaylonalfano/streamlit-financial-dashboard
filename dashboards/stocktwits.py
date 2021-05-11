import streamlit as st
import requests


# # Assign a function then inside main.py run with dashboards.stocktwits.main()
def main():
    # Add a input box to search for a symbol
    symbol = st.sidebar.text_input("Symbol", value="AAPL", max_chars=10)

    r = requests.get(f"https://api.stocktwits.com/api/2/streams/symbol/{symbol}.json")
    data = r.json()

    for message in data["messages"]:
        st.image(message["user"]["avatar_url"])
        st.write(message["user"]["username"])
        st.write(message["created_at"])
        st.write(message["body"])


# Go with out a function - ERROR. Doesn't load
# r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/AAPL.json")
# data = r.json()

# for message in data["messages"]:
#     st.image(message["user"]["avatar_url"])
#     st.write(message["user"]["username"])
#     st.write(message["created_at"])
#     st.write(message["body"])
