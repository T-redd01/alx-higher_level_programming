#!/home/otto/Documents/ORM-venv/venv/bin/python3
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
            user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    arg = sys.argv[4].partition(';')[0].replace("'", "")
    cur.execute("SELECT cities.name FROM cities JOIN states \
ON cities.state_id = states.id WHERE \
states.name='{}' ORDER BY cities.id ASC".format(arg))
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[0])
    print(", ".join(cities))
    cur.close()
    conn.close()
