#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
Where name matches the argument.
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

    sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(sql, sys.argv[4])

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()
