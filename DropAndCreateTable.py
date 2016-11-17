import sqlite3
from sqlite3 import OperationalError
conn = sqlite3.connect('Student.db')
c = conn.cursor()
def droptable():
   c.execute(" DROP TABLE student ")

def createtable():
   try:
      c.execute("CREATE TABLE student ( ROLL_NO INT PRIMARY KEY, NAME VARCHAR(20), BRANCH CHAR(5), AGE INT, EMAIL VARCHAR(20))")
   except OperationalError:
      print 'Table already exists.\n'
