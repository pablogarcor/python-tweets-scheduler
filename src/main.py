import sqlite3


# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def create_tweets_table(cursor):
    cursor.execute('CREATE TABLE IF NOT EXISTS tweets(text VARCHAR(280))')


def add_tweet(cursor, message):
    cursor.execute("INSERT INTO tweets (text) VALUES(?)", (message))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        con = sqlite3.connect("tweet-scheduler.db")
        cur = con.cursor()
        create_tweets_table(cur)

        # commit the changes to db
        con.commit()
        # close the connection
        con.close()
    except Exception as e:
        print(f'Error: {e}')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
