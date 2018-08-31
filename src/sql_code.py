import sqlite3 as sql

import json

from datetime import datetime

timeframe = '2010-01'

sql_transaction = []

connection = sql.connect('../data/{}.db'.format(timeframe))
c = connection.cursor()


def create_table():
    c.execute("""CREATE TABLE IF NOT EXISTS main_reply
    (parent_id TEXT PRIMARY KEY, comment_id TEXT UNIQUE, parent TEXT,
     comment TEXT,subreddit TEXT, unix INT, score INT)""")


def format_data(data):
    # \n is new line
    # \r is return
    # " is ' because both are same
    data = data.replace("\n", " newlinechar ").replace("\r", " newlinechar ").replace('"', "'")
    return data

def find_parent(pid):
    try:
        # LIMIT 1 so that we select only parent(Technically there should only be one parent)
        sql = "SELECT comment FROM parent_reply WHERE comment_id = '{}' LIMIT 1".format(pid)
        c.execute(sql)
        result = c.fetchone()
        if result != None:
            return result[0]
        else:
            return False
    except Exception as e:
        #print("find_parent", e)
        return False

def

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
            score = row['score']
            subreddit = row['subreddit']

            parent_data = find_parent(parent_id)

            if score >= 2:
                existing_comment_score = find_exisiting_score(parent_id)


