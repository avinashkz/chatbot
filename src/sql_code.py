import sqlite3 as sql

import json

from datetime import datetime

timeframe = ["2010-01"]

sql_transaction = []

connection = sql.connect('{}.db'.format(timeframe))
c = connection.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS main_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
     comment TEXT,subreddit TEXT, unix INT, score INT)""")


if __name__ == "__main__":
    create_table()
    # How many rows have we interated through in the file
    row_counter = 0
    # How many parent and child pairs are made
    paired_rows = 0

    with open("../data/RC_{}".format(timeframe), buffering=1000) as f:
        for row in f:
            row_counter += 1
            row = json.loads(row)
            parent_id = row['parent_id']
            body = format_data(row['body'])
            created_utc = row['created_utc']
            subreddit = row['subreddit']


