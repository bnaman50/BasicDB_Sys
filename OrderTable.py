import sqlite3
conn = sqlite3.connect('Student.db')
c = conn.cursor()
                
def ordertable():
       print 'Attribute to which table is odered'
       print '1. ROLL_NO'
       print '2. NAME'
       print '3. BRANCH'
       print '4. AGE'
       print '5. EMAIL'
       n=raw_input('Enter your choice:')
       if (n=='1'):
           c.execute("SELECT * FROM student ORDER BY ROLL_NO")
           rows = c.fetchall()
           print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"   
           for row in rows:
              print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
           print ' '
       elif (n=='2'):
           c.execute("SELECT * FROM student ORDER BY NAME")
           rows = c.fetchall()
           print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"   
           for row in rows:
              print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
           print ''
       elif (n=='3'):
             c.execute("SELECT * FROM student ORDER BY BRANCH")
             rows = c.fetchall()
             print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
             for row in rows:
                print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
             print ''
       elif (n=='4'):
             c.execute("SELECT * FROM student ORDER BY AGE")
             rows = c.fetchall()
             print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"   
             for row in rows:
                print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
             print ''
       elif (n=='5'):
             c.execute("SELECT * FROM student ORDER BY EMAIL")
             rows = c.fetchall()
             print "\nROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"   
             for row in rows:
                print "%010d"%row[0]+"     "+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+"     "+row[4]
       else:
             print 'Invalid choice\nAgain try ordering table\n'
             ordertable()



