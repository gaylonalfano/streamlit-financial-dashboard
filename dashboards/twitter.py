import config
import streamlit as st
import pandas as pd
import tweepy


# ==== USING STATIC SAMPLE FROM CSV
def main():
    tweets = pd.read_csv("./data/tweets.csv", nrows=100)
    # Rename columns so we can use dot notation
    tweets.columns = tweets.columns.str.replace(" ", "_")
    st.header("Header from within main() inside dashboards/twitter.py")
    # st.dataframe(tweets)
    # st.write(tweets.columns)
    for tweet in tweets.itertuples():
        # st.image(row.Profile_URL)
        # st.write(tweet.Profile_URL)
        if "@" in tweet.Tweet_Content:
            words = tweet.Tweet_Content.split(" ")
            for word in words:
                if word.startswith("@") and word[1:].isalpha():
                    mention = word[1:]
                    st.subheader(mention)
                    st.write(tweet.Tweet_Content)
                    # Let's also out the FINVIZ chart
                    # By ticker: https://finviz.com/quote.ashx?t=AAPL
                    # By name: https://finviz.com/search.ashx?p=FORBES
                    st.image(f"https://finviz.com/quote.ashx?p={mention}")


# # ==== USING TWITTER API + TWEEPY
# TWITTER_USERNAMES = [
#     "traderstewie",
#     "the_chart_life",
#     "canuck2usa",
#     "sunrisetrader",
#     "tmltrader",
#     "krugermacro",
# ]

# # Authenticate with Twitter API
# auth = tweepy.OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
# auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)


# def main():
#     st.header("Header from within main() inside dashboards/twitter.py")

#     # Loop through all the users we wish to watch
#     for username in TWITTER_USERNAMES:
#         # Get the timeline for a single user to explore the data
#         user = api.get_user(username)
#         tweets = api.user_timeline(username)
#         # Display the user's avatar image
#         st.subheader(username)
#         st.image(user.profile_image_url)

#         for tweet in tweets:
#             # Only look for tweets that mention some symbol with $ sign
#             if "$" in tweet.text:
#                 # Split up all the words in the tweet to find the mention
#                 words = tweet.text.split(" ")
#                 for word in words:
#                     # Find those words like $AAPL $COIN
#                     if word.startswith("$") and word[1:].isalpha():
#                         symbol = word[1:]
#                         st.write(symbol)
#                         st.write(tweet.text)
#                         # Let's also out the FINVIZ chart: https://finviz.com/quote.ashx?t=AAPL
#                         st.image(f"https://finviz.com/quote.ashx?t={symbol}")
