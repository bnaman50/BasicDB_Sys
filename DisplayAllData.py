import sqlite3
conn = sqlite3.connect('Student.db')
c = conn.cursor()
def display_all_data():
    c.execute("SELECT * FROM student")
    rows = c.fetchall()
    print "ROLLNO         NAME                     BRANCH              AGE     EMAIL               \n"
    for row in rows:
       print "%010d"%row[0]+'     '+row[1]+'     '+row[2]+'     '+"%03d"%row[3]+'     '+row[4]
    print ' '
