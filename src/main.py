import sqlite3
from requests_oauthlib import OAuth1Session
import os
import tweepy
import json
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def create_tweets_table(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS tweets(text VARCHAR(280))')


def add_tweet(cursor, message):
    cursor.execute("INSERT INTO tweets (text) VALUES(?)", ([message]))


def get_all_tweets(cursor):
    cursor.execute("SELECT text FROM tweets")

    rows = cur.fetchall()
    return rows[0]
    # for row in rows:
    #    print(row)


def post_tweet(tweet):
    consumer_key = os.getenv("CONSUMER_KEY")
    consumer_secret = os.getenv("CONSUMER_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_secret = os.getenv("ACCESS_SECRET")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    api.update_status(tweet)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        con = sqlite3.connect("tweet-scheduler.db")
        cur = con.cursor()
        create_tweets_table(cur)
        tweet = get_all_tweets(cur)
        post_tweet(tweet)
        # commit the changes to db
        con.commit()
        # close the connection
        con.close()
    except Exception as e:
        print(f'Error: {e}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
