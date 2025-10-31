#!/usr/bin/python3
"""
List all states from a database
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        port=3306,
        db=sys.argv[3]
    )

    cur = db.cursor()

    cur.execute(SELECT * FROM states ORDER BY id ASC)
    results = cur.fetchall()
    for row in results:
        print(row)

    cur.close()
    db.close()
