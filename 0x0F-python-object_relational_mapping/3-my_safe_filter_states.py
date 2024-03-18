#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
Where name matches the argument.
Safe from MySQL injection.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()

    state_name = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name LIKE %s", (state_name, ))

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
