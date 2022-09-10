#!/usr/bin/python3

"""
A script that takes in an argument and displays all values
in the states table of hbtn-0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    my_db = MySQLdb.connect(user=argv[1],
                            passwd=argv[2],
                            db=argv[3],
                            host='localhost',
                            port=3306)
    c = my_db.cursor()
    cmd = """SELECT *
             FROM states
             WHERE name LIKE BINARY '{}'
             ORDER BY id ASC;""".format(argv[4])
    c.execute(cmd)
    states = c.fetchall()

    for state in states:
        print(state)

    c.close()
    my_db.close()
