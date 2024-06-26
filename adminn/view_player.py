import sqlite3

def viewing():
    conn = sqlite3.connect('./player.db') # connecting to the database
    c=conn.cursor()
    c.execute('SELECT * FROM teamplayers') # retriving the data from the teamplayers
    data=c.fetchall() # gives total data in list form
    while True:
        try:
            user_player_input=int(input('please enter 1 to view all player stats or press 2 to view individual player stat:-'))
            break
        except ValueError:
            print('Only 1 or 2 is allowed to enter')
    if user_player_input==1:
        print("name,runs_scored,bls_faced,strike_rate,overs,runs_given,wickets,catches,run_outs")
        for i in data:
            for j in i:
                print(j,end="\t") #printing the individual player stats
            print()
    else: #if the user only just want to a individual player stat
        temp=True
        while temp:
            print_stat=['name','runs_scored','balls_faced','strike_rate','no_of_overs','runs_given','wickets','catches','runs_outs']
            input_player_stat=input('enter the name of player to view his stat: ') 
            for i in data:
                if i[0]==input_player_stat:
                    for j in range(len(i)):
                        print(print_stat[j],'-',i[j])
                    temp=False
                    break
            else:
                print('There is no player with the given name. pls try again')
        
    conn.close()
    return 


