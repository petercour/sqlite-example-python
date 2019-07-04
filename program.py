#!/usr/bin/python3
# -*- coding: iso-8859-1 -*-
# https://pythonbasics.org
from sqlite3 import dbapi2 as sqlite

# Create a database:
con = sqlite.connect('mydatabase.db3')
cur = con.cursor()

# Create a table:
cur.execute('create table clients (id INT PRIMARY KEY, name CHAR(60))')

# Insert a records line:
client = (2,"Alice Smith")
cur.execute("insert into clients (id, name) values (?, ?)", client )
con.commit()

# Insert several records at once:
clients = [ (3,"Thomas Edison"),
            (4,"William Conqueror"),
            (5,"Niels Bohr")
          ]
cur.executemany("insert into clients (id, name) values (?, ?)", clients )
con.commit()

cur.close()
con.close()
