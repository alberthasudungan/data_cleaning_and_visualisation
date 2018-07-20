#import pandas and sqllite3
import pandas as pd
import sqlite3

#syntax to create database
query="""CREATE TABLE tests(a VARCHAR(20), b VARCHAR(20), c REAL, d INTEGER);"""

#connecting to sqllite3
con=sqlite3.connect('mydata.sqlite')
con.execute(query)
con.commit()

#insert a few rows of data
data = [('Atlanta', 'Georgia', 1.25, 6),('Tallahassee', 'Florida', 2.6, 3),('Sacramento', 'California', 1.7, 5)]
stmt = "INSERT INTO tests VALUES(?,?,?,?)"

#execute all tupples
con.executemany(stmt, data)
con.commit()

#returning a list of tuples
cursor = con.execute('select * from tests')
rows = cursor.fetchall()
rows

#describing cursor
cursor.description

#displaying table according to columns' name
pd.DataFrame(rows, columns=[x[0] for x in cursor.description])
