#!/home/otto/Documents/ORM-venv/venv/bin/python3
"""List states satrting with 'N'"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        if row[1].startswith('N'):
            print(row)
    cur.close()
    conn.close()
