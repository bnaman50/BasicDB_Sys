import sqlite3

conn = sqlite3.connect('Student.db')
c = conn.cursor()
from InsertData import isNum
from InsertData import isString

def deleterow():
      print 'Attribute to which row is to be deleted'
      print '1. ROLL_NO'
      print '2. NAME'
      print '3. BRANCH'
      print '4. AGE'
      print '5. EMAIL'
      n=raw_input("Enter the value:")
##Delete by Roll NO.
      if(n=='1'):
          print 'Enter the constraint'
          print '1. Equal to'
          print '2. Greater than'
          print '3. Less than'
          print '4. Enter the range [x,y]'
          a=raw_input('Enter the option:')
          if (a=='1'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break
              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
              for row in rows:
                  if (row[0]==p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[0]==p):                     
                           query=" DELETE FROM student WHERE ROLL_NO='%d'"%row[0]
                           c.execute(query)
                           conn.commit()
          elif (a=='2'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break

              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"              
              for row in rows:
                  if (row[0]>p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[0]>p):                     
                           query=" DELETE FROM student WHERE ROLL_NO>'%d'"%p
                           c.execute(query)
                           conn.commit()
              
                  
          elif (a=='3'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break

              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"              
              for row in rows:
                  if (row[0]<p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[0]<p):                     
                           query=" DELETE FROM student WHERE ROLL_NO<'%d'"%p
                           c.execute(query)
                           conn.commit()

                  
          elif (a=='4'):
              count=0
              while(True):
                 l=raw_input('Enter the lower value:')
                 print isNum(l)
                 if isNum(l)=='invalid':
                    continue
                 else:
                     l=int(l)
                     break

              while(True):
                 u=raw_input('Enter the upper value:')
                 print isNum(u)
                 if isNum(u)=='invalid':
                    continue
                 else:
                     u=int(u)
                     break
                  
              if (l>u):
                 print "Invalid Entry"
                 deleterow()
              else:
                 c.execute("SELECT * FROM student")
                 rows = c.fetchall()
                 print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
                 for row in rows:
                    if (row[0]>=l and row[0]<=u):
                       count+=1
                       print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
                 if (count==0):
                    print 'No such data exists\n'
                 else: 
                    d=raw_input('Above rows will be deleted, do you wish to continue(y/n):')
                    if (d=='y' or d=='Y'):
                       for row in rows:
                          if(row[0]>=l and row[0]<=u):                     
                             query=" DELETE FROM student WHERE ROLL_NO='%d'"%row[0]
                             c.execute(query)
                             conn.commit()
          else:
             print '\nYou entered wrong value\nAgain try deleting row\n'
             deleterow()
          

                  
##Delete by Name                    
      elif(n=='2'):
          count=0
          m=(raw_input( "Enter the name or part of it:"))
          
          c.execute("SELECT * FROM student")
          rows = c.fetchall()
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                if (m.lower() in row[1].lower()):
                   count+=1
                   print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if(count==0):
             print 'No such data exists'
          else:
               d=raw_input('Above rows will be deleted, do you wish to continue(y/n):')
               if (d=='y' or d=='Y'):
                  for row in rows:
                     if(m.lower() in row[1].lower()):                     
                        query=" DELETE FROM student WHERE NAME='%s'"%row[1]
                        c.execute(query)
                        conn.commit()

      

                   
##Delete by Branch
      elif(n=='3'):
          count=0
          m=(raw_input( "Enetr the branch or part of it:"))
          c.execute("SELECT * FROM student")
          rows = c.fetchall()
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                if (m.lower() in row[2].lower()):
                   count+=1
                   print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if(count==0):
             print 'No such data exists'
          else:
               d=raw_input('Above rows will be deleted, do you wish to continue(y/n):')
               if (d=='y' or d=='Y'):
                  for row in rows:
                     if(m.lower() in row[2].lower()):                     
                        query=" DELETE FROM student WHERE BRANCH='%s'"%row[2]
                        c.execute(query)
                        conn.commit()
                   
##Delete by Age
      elif(n=='4'):
          print 'Enter the constraint'
          print '1. Equal to'
          print '2. Greater than'
          print '3. Less than'
          print '4. Enter the range [x,y]'
          a=raw_input('Enter the option:')
          if (a=='1'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break

              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
              for row in rows:
                  if (row[3]==p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[3]==p):                     
                           query=" DELETE FROM student WHERE AGE='%d'"%p
                           c.execute(query)
                           conn.commit()
                  

          elif (a=='2'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break

              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "ROLLNO         NAME                     BRANCH              AGE     EMAIL               "
              for row in rows:
                  if (row[3]>p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[3]>p):                     
                           query=" DELETE FROM student WHERE AGE>'%d'"%p
                           c.execute(query)
                           conn.commit()
              
                      
    
          elif (a=='3'):
              count=0
              while(True):
                 p=raw_input('Enter the value:')
                 print isNum(p)
                 if isNum(p)=='invalid':
                    continue
                 else:
                     p=int(p)
                     break

              c.execute("SELECT * FROM student")
              rows = c.fetchall()
              print "ROLLNO         NAME                     BRANCH              AGE     EMAIL               "
              for row in rows:
                  if (row[3]<p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
              else: 
                  d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                  if (d=='y' or d=='Y'):
                     for row in rows:
                        if(row[3]<p):                     
                           query=" DELETE FROM student WHERE AGE<'%d'"%p
                           c.execute(query)
                           conn.commit()
                      
          elif (a=='4'):
              count=0
              while(True):
                 l=raw_input('Enter the lower value:')
                 print isNum(l)
                 if isNum(l)=='invalid':
                    continue
                 else:
                     l=int(l)
                     break

              while(True):
                 u=raw_input('Enter the upper value:')
                 print isNum(u)
                 if isNum(u)=='invalid':
                    continue
                 else:
                     u=int(u)
                     break
              if (l>u):
                  print "Invalid Entry"
                  deleterow()
              else:
                 c.execute("SELECT * FROM student")
                 rows = c.fetchall()
                 print "ROLLNO         NAME                     BRANCH              AGE     EMAIL               "
                 for row in rows:
                    if (row[3]>=l and row[3]<=u):
                       count+=1
                       print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
                 if (count==0):
                    print 'No such data exists\n'
                 else: 
                    d=raw_input('Above rows satisfy the criteria, you sure you want to delete(y/n):')
                    if (d=='y' or d=='Y'):
                       for row in rows:
                          if(row[3]>=l and row[3]<=u):                     
                             query=" DELETE FROM student WHERE AGE='%d'"%row[3]
                             c.execute(query)
                             conn.commit()
          else:
             print '\nYou entered wrong value\nAgain try deleting row\n'
             deleterow()


##Delete by Email
                  
      elif(n=='5'):
          count =0
          m=(raw_input( "Enetr email or part of it:"))
          c.execute("SELECT * FROM student")
          rows = c.fetchall()
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                if (m.lower() in row[4].lower()):
                   count+=1
                   print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if(count==0):
             print 'No such data exists'
          else:
               d=raw_input('Above rows will be deleted, do you wish to continue(y/n):')
               if (d=='y' or d=='Y'):
                  for row in rows:
                     if(m.lower() in row[4].lower()):                     
                        query=" DELETE FROM student WHERE EMAIL='%s'"%row[4]
                        c.execute(query)
                        conn.commit()
      else:
         print '\nYou entered wrong value\nAgain try deleting row\n'
         deleterow()
