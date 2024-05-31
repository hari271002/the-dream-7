import sqlite3

conn=sqlite3.connect('player.db')

c=conn.cursor() #created a cursor

#creating a table
# c.execute(""" CREATE TABLE teamplayers(
#           name TEXT,
#           runs_scored INTEGER,
#           balls_faced INTEGER,
#           strike_rate REAL,
#           no_of_overs_bowled INTEGER,
#           runs_given INTEGER,
#           wickets INTEGER,
#           catch_taken INTEGER,
#           run_outs INTEGER
# )
# """)


# c.execute("INSERT INTO teamplayers VALUES ('dhoni',20,4,500,0,0,0,1,2)")
# c.execute("INSERT INTO teamplayers VALUES ('kohli',54,27,200,0,0,0,1,0)")
# c.execute("INSERT INTO teamplayers VALUES ('rohit',23,23,100,0,0,0,1,0)")
# c.execute("INSERT INTO teamplayers VALUES ('dhawan',12,10,120,0,0,0,2,0)")
# c.execute("INSERT INTO teamplayers VALUES ('rahane',28,14,200,0,0,0,3,0)")
# c.execute("INSERT INTO teamplayers VALUES ('ruturaj',100,54,185.18,0,0,0,1,1)")
# c.execute("INSERT INTO teamplayers VALUES ('gill',66,30,220,0,0,0,2,0)")
# c.execute("INSERT INTO teamplayers VALUES ('bumrah',0,0,0,4,22,2,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('siraj',0,0,0,4,28,1,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('umesh',2,1,200,4,36,0,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('deshpande',0,0,0,4,24,2,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('shardul',0,1,0,4,40,3,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('starc',0,0,0,4,36,1,0,0)")
# c.execute("INSERT INTO teamplayers VALUES ('cummins',20,10,200,4,32,2,0,0)")

# c.execute("SELECT * from teamplayers")
# data=c.fetchall()
# print(data)

conn.commit()

conn.close()