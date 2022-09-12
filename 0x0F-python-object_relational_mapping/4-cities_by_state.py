#!/usr/bin/python3

"""
A script that takes in an argument and displays all values
in the states table of hbtn-0e_0_usa where name matches the argument
and is safe from SQL Injection.
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
    cmd = """SELECT cities.id, cities.name, states.name
             FROM states
             INNER JOIN cities ON states.id = cities.state_id
             ORDER BY cities.id ASC;"""
    c.execute(cmd)
    cities = c.fetchall()

    for city in cities:
        print(city)

    c.close()
    my_db.close()
