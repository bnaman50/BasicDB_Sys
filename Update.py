import sqlite3
from sqlite3 import IntegrityError
from InsertData import isNum
from InsertData import isString


conn = sqlite3.connect('Student.db')
c = conn.cursor()

def update():
      while(True):
         n=raw_input("Enter the Roll number:")
         print isNum(n)
         if isNum(n)=='invalid':
            continue
         else:
            n=int(n)
            break
      c.execute("SELECT * FROM student")
      rows = c.fetchall()
      print "ROLLNO         NAME                     BRANCH              AGE     EMAIL               "
      count=0
      for row in rows:
          if(row[0]==n):
               count+=1
               print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
      if(count==0):
         print"\nNo such data exists\n"
      else:   
      ##Input Name
         while(True):
            d2=raw_input("Name: (Press Enter for no change)")
            if(d2==''):
               d2=row[1]
               break
            else:
               print isString(d2)
               if isString(d2)=='invalid':
                  continue
            a=20-len(d2)
            for i in range(a):
               d2+=" "
            break   

               
      ## Input Branch
         i=0
         while(True):
            d3=raw_input("Branch: (Press Enter for no change)")
            if(d3==''):
               d3=row[2]
               break
            else:
               print isString(d3)
               if isString(d3)=='invalid':
                  continue
            a=15-len(d3)
            for i in range(a):
               d3+=" "
            break

      ##Input Age
         while(True):
            d4=raw_input("Age: (Press Enter for no change)")
            if(d4==''):
               d4=row[3]
               break
            else:
               
               numbers='0123456789'
               b=len(d4)
               z=b
               for a in d4:
                  if a not in numbers:
                     z=z-1
               if(z!=b):
                   print 'invalid'
               else:
                   d4= int(d4)
                   break
               break
             
      ##Input Email And Check
         i=0
         d=0
         while(i==0):
            d5=raw_input("Email: (Press Enter for no change)")
            if(d5==''):
               d5=row[4]
               break
            else:
               
               if '@' in d5:
                  i+=1
               else:
                  print "Invalid"
            a=20-len(d5)
            for i in range(a):
                      d5+=" "
            break          
         c.execute(" UPDATE student set NAME='%s' ,BRANCH='%s',AGE ='%s',EMAIL ='%s' where ROLL_NO='%s' "%(d2,d3,d4,d5,n)) 
         conn.commit()                
         
   

