#!/usr/bin/python3
"""preventing sql injections"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    arg = sys.argv[4].partition(';')[0].replace("'", "")
    cur.execute("SELECT * FROM states WHERE name='{}' \
ORDER BY id ASC".format(arg))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
