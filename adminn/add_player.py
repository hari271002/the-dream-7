import sqlite3
def adding():
    conn=sqlite3.connect('player.db') # connecting to the database
    c=conn.cursor()  # creating a cursor
    
    player_name=input('enter the player name ') 

    while True:
        try:
            runs_scored = int(input("enter the no. of runs scored "))
            break  
        except ValueError:
            print("Please enter a number only.")

    while True:
        try:
            balls_faced=int(input('enter the no. of balls faced '))
            break  
        except ValueError:
            print("Please enter a number only.")

    while True:
        try:
            no_overs=int(input('enter the no. of overs bowled '))
            break  
        except ValueError:
            print("Please enter a number only.")

    while True:
        try:
            runs_given=int(input('enter the no. of runs given '))
            break  
        except ValueError:
            print("Please enter a number only.")
    
    while True:
        try:
            wickets=int(input('enter the no. of wickets taken '))
            break  
        except ValueError:
            print("Please enter a number only.")

    while True:
        try:
            catches=int(input('enter the no. of catches taken '))
            break  
        except ValueError:
            print("Please enter a number only.")

    while True:
        try:
            run_outs=int(input('enter the no. of run outs '))
            break  
        except ValueError:
            print("Please enter a number only.")
    
    strike_rate=(runs_scored/balls_faced)*100
    player_stat=[(player_name,runs_scored,balls_faced,strike_rate,no_overs,runs_given,wickets,catches,run_outs)]
    c.executemany("INSERT INTO teamplayers VALUES (?,?,?,?,?,?,?,?,?)",player_stat)
    
    conn.commit()
    conn.close()
    return