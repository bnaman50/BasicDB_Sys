import sqlite3
conn = sqlite3.connect('Student.db')
c = conn.cursor()
from InsertData import isNum
from InsertData import isString
def displayrow():
      n=raw_input("Attribute to which row is displayed\n1. ROLL_NO\n2. NAME\n3. BRANCH\n4. AGE\n5. EMAIL\nEnter the option: ")
##Display by Roll NO.
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
                     displayrow()
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
                  print"Wrong input, Please try again\n"
                  displayrow()
##Display by Name                    
      elif(n=='2'):
          m=(raw_input( "Enter the name or part of it:"))
          c.execute("SELECT * FROM student")
          rows = c.fetchall()
          count = 0
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                if (m.lower() in row[1].lower()):
                      count +=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if (count == 0):
                print "No data found\n"

                   
##Display by Branch
      elif(n=='3'):
          m=(raw_input( "Enetr the branch or part of it:"))
          c.execute("SELECT * FROM student")
          rows = c.fetchall()
          count = 0
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                if (m.lower() in row[2].lower()):
                      count +=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if (count==0):
                print "No data found\n"
                   

##Display by Age
      elif(n=='4'):
          print 'Enter the constraint'
          print '1. Equal to'
          print '2. Greater than'
          print '3. Less than'
          print '4. Enter the range (x,y)'
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
                  if (row[3]>p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
                      
    
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
                  if (row[3]<p):
                      count+=1
                      print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
              if (count==0):
                  print 'No such data exists\n'
                      
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
                    displayrow()
              else :
                    c.execute("SELECT * FROM student")
                    rows = c.fetchall()
                    print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
                    for row in rows:
                          if (row[3]>l and row[3]<u):
                                count+=1
                                print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
                    if (count==0):
                          print 'No such data exists\n'
          else:
                  print "Wrong input, please try again\n"
                  displayrow()

##Display by Email
                  
      elif(n=='5'):
          m=(raw_input( "Enetr email or part of it:"))
          c.execute("SELECT * FROM student")
          count =0
          rows = c.fetchall()
          print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
          for row in rows:
                count+=1
                if (m.lower() in row[4].lower()):
                   print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
          if (count == 0):
                print "No data found\n"
      else:
            print "Wrong input, please try again\n"
            displayrow()
            
