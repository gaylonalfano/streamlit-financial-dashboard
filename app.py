import streamlit as st
import pandas as pd
import numpy as np
import requests
import dashboards.chart
import dashboards.stocktwits
import dashboards.twitter
import dashboards.wallstreetbets
import dashboards.pattern

# st.title("This is the title")
# st.header("This is the header")
# st.subheader("Subheader")
# st.write("This is some text")

# """
# # markdown
# ## also works here
# """

# # Can even use magic method to pretty print to the screen directly
# # {"k1": "v1", "k2": "v2"}

# # Or, save to var and print/write like usual
# some_dictionary = {"k1": "v1", "k2": "v2"}
# some_list = [1, 2, 3]
# st.write(some_dictionary)
# st.write(some_list)

# Add content to the sidebar
st.sidebar.title("Options")

option = st.sidebar.selectbox(
    "Which dashboard?",
    ("twitter", "wallstreetbets", "stocktwits", "chart", "pattern"),
    2,
)

st.title("https://github.com/hackingthemarkets/streamlit-dashboards")
st.header(option)

# Display different content based on option
if option == "stocktwits":
    # r = requests.get("https://api.stocktwits.com/api/2/streams/symbol/AAPL.json")
    # data = r.json()

    # for message in data["messages"]:
    #     st.image(message["user"]["avatar_url"])
    #     st.write(message["user"]["username"])
    #     st.write(message["created_at"])
    #     st.write(message["body"])

    # IMPORTING FROM MODULE
    # 1. Where module has a def main()
    dashboards.stocktwits.main()
    # 2. Where module has NO function - ERROR
    # dashboards.stocktwits

if option == "twitter":
    dashboards.twitter.main()

if option == "wallstreetbets":
    dashboards.wallstreetbets.main()

if option == "chart":
    # dashboards.charts.st.subheader("subheader from within main.py")
    dashboards.chart.main()

if option == "pattern":
    dashboards.pattern.main()


# Can add DFs as well
# df = pd.DataFrame(np.random.randn(50, 20), columns=("col %d" % i for i in range(20)))
# st.dataframe(df)

# And images
# st.image(
#     "https://static.coindesk.com/wp-content/uploads/2020/02/EthDepositsInDefiLendingAndPrice2019-2020_CoindeskResearch.png"
# )
