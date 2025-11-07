#!/usr/bin/python3
"""
Takes in the name of a state as an
argument and lists all cities of that state
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = (
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
        )

    cur = db.cursor()

    query = ("SELECT cities.name "
             "FROM states "
             "JOIN cities ON (%s).id = cities.state_id "
             "ORDER BY cities.id ASC", (sys.argv[4],))

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
