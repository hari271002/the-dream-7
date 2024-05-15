import sqlite3

def viewing():
    conn=sqlite3.connect('player.db') # connecting to the database
    c=conn.cursor()
    c.execute('SELECT * FROM teamplayers') # retriving the data from the teamplayers
    data=c.fetchall() # gives total data in list form
    user_player_input=int(input("press 1 to display stats of all player or press 2 to display indiviual player stats: "))
    while user_player_input!=1 and user_player_input!=2: # this loop will ensure user only enters either 1 or 2 
        print('wrong input please 1 or 2')
        user_player_input=int(input("press 1 or 2 or if you like to exist pls press 3  "))
        if user_player_input==3: # if 3 is pressed we are exited
            return 
    if user_player_input==1:
        print("name,runs_scored,bls_faced,strike_rate,overs,runs_given,wickets,catches,run_outs")
        for i in data:
            for j in i:
                print(j,end="\t") #printing the individual player stats
            print()
    else: #if the user only just want to a individual player stat
        temp=True
        while temp:
            input_player_stat=input('enter the name of player to view his stat: ') 
            for i in data:
                if i[0]==input_player_stat:
                    print(i)
                    temp=False
                    break
            else:
                print('There is no player with the given name. pls try again')
        
    conn.close()
    return 

