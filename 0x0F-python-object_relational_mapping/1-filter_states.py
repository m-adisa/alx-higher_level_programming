#!/usr/bin/python3

"""
A script that lists all states with name starting with N
from database hbtn-0e_0_usa
"""

import MySQLdb
import sys

if __name__ == '__main__':
    my_db = MySQLdb.connect(user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3],
                            host='localhost',
                            port=3306)
    c = my_db.cursor()
    cmd = """SELECT id, name
             FROM states
             WHERE name LIKE BINARY 'N%'
             ORDER BY id ASC;"""
    c.execute(cmd)
    states = c.fetchall()

    for state in states:
        print(state)

    c.close()
    my_db.close()
