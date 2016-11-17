import sqlite3
from sqlite3 import IntegrityError

conn = sqlite3.connect('Student.db')
c = conn.cursor()

def isNum(var):
      numbers='0123456789'
      b=len(var)
      z=b
      for a in var:
         if a not in numbers:
            z=z-1
      if(z!=b):
          return 'invalid'
      else:
          return ''
def isString(var):
      alphas='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. '
      b=len(var)
      z=b
      for a in var:
         if a not in alphas:
            z=z-1
      if(z!=b):
          return 'invalid'
      else:
         return ''

def insertdata():    
   print "Enter data to table:"
##Input ROll No.And Check

   while(True):
      rnum=raw_input("Roll No:")
      print isNum(rnum)
      if isNum(rnum)=='invalid':
         continue
      else:
         rnum=int(rnum)
         break
         
      
          
          

##Input Name
   while(True):
      name=raw_input("Name:")
      print isString(name)
      if isString(name)=='invalid':
         continue
      else:
         a=20-len(name)
         for i in range(a):
            name+=" "
         break

      
## Input Branch
   while(True):
      branch=raw_input("Branch:")
      print isString(branch)
      if isString(branch)=='invalid':
         continue
      else:
         a=15-len(branch)
         for i in range(a):
            branch+=" "
         break


##Input Age
   while(True):
      age=raw_input("Age:")
      print isNum(age)
      if isNum(age)=='invalid':
         continue
      else:
         age=int(age)
         if(age>100 or age==0):
               print 'invalid\n'
         else:
               break

       
##Input Email And Check
   i=0
   d=0
   while(i==0):
      eid=raw_input("Email:")
      if '@' in eid:
         i+=1
      else:
         print "Invalid"
   a=20-len(eid)
   for i in range(a):
             eid+=" "
       
   try:
      c.execute("INSERT INTO student VALUES(?,?,?,?,?)",(rnum,name,branch,age,eid) )
      conn.commit()
   except IntegrityError:
      print 'Roll No already exists\nTry inserting data\n'
      insertdata()
