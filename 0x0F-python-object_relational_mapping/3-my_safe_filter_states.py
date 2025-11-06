#!/usr/bin/python3
"""
takes in arguments and displays all values
in the states table of hbtn_0e_0_usa where
name matches the argument. But this time,
write one that is safe from MySQL injections!
"""
import MySQLddb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        host=3306,
        usr=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
        )

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE BINARY name = %s"
                "ORDER BY id ASC", (sys.argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
