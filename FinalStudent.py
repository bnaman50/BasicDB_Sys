import sqlite3
## Remove error if primary key is same
from sqlite3 import IntegrityError
## Remove error if table already exists
from sqlite3 import OperationalError

conn = sqlite3.connect('Student.db')
c = conn.cursor()
from InsertData import *
from DisplayAllData import *
from DisplayRow import *
from OrderTable import *
from DeleteRow import *
from Update import *
from DropAndCreateTable import *


z=0
while(True):
      print "1. CREATE TABLE"
      print "2. INSERT DATA"
      print "3. DISPLAY TABLE"
      print "4. DISPLAY ROW"
      print "5. ORDER TABLE"
      print "6. UPDATE TABLE"
      print "7. DELETE SOME ENTRY"
      print "8. DROP TABLE"
      print "9. EXIT"
      z=raw_input("Select an option:")
      if(z=='1'):
            createtable()
      elif(z=='2'):
            insertdata()
      elif(z=='3'):
            display_all_data()
      elif(z=='4'):
            displayrow()
      elif(z=='5'):
            ordertable()
      elif(z=='8'):
            droptable()
      elif(z=='7'):
            deleterow()
      elif(z=='6'):
            update()
      elif (z=='9'):
         break
      else:
         print 'You entered a wrong value \nTry again'
         
            
