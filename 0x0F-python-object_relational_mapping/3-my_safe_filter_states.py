#!/usr/bin/python3

"""
This lists all states from the database hbtn_0e_0_usa
"""

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=argv[1], passwd=argv[2],
            db=argv[3], host="localhost", port=3306)
    cur = db.cursor()
    cur.execute(
            """SELECT * FROM states
            WHERE states.name = %s ORDER BY states.id
            """, (argv[4], )
    )
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
