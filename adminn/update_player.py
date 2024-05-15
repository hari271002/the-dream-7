import sqlite3 #importing sqlite database

def updating():
    conn=sqlite3.connect('player.db') #command to connect to the data base
    c=conn.cursor() #creating a cursor for the data base
    c.execute("SELECT * FROM teamplayers")  #sql command to retrive the data
    data = c.fetchall() #this command return data in table in a list 
    i=1
    print('These are the players available')
    for player in data:
        print(i,".",player[0]) #printing the availble player
        i=i+1
    player_input=input('enter the name of player you want update ')
    temp=True
    while temp: #this while loop helps to take correct input from the player
        for i in data:
            if player_input==i[0]:
                temp=False
                break
        else:
            player_input=input('pls enter the correct name or available player ')
    # this dictionary maps 1 to 8 to the entities in the table
    updating_para={1:'runs_scored',2:'balls_faced',3:'strike_rate',4:'no_of_overs_bowled',5:'runs_given',6:'wickets',7:'catch_taken',8:'run_outs'}
    for key,value in updating_para.items():
        print(key," ",value) # this will print the entities with numbering
    player_stat=int(input('select the stat you want to update,enter the no. between 0 to 8 '))
    while player_stat not in range(1,9): # this loop will check if the player_stat input is correct or not
        player_stat=int(input('enter the correct input or if you like exist pl enter 10 '))
        if player_stat==10:
            return 
    player_new_stat=input('enter the new value for the stat ') # this takes new stat from the user 
    if player_stat in [1,2,4,5,6,7,8]: # based on the player_stat we are converting in its data type
        player_new_stat=int(player_new_stat)
    elif player_stat==3:
        player_new_stat=float(player_new_stat)
    try:
        query = f"UPDATE teamplayers SET {updating_para[player_stat]} = ? WHERE name = ?" # this the query to update the table '?' are placeholders
        c.execute(query, (player_new_stat, player_input))
        print('Successfully updated.')

        conn.commit()
    except Exception as e:
        print(f"An error occurred: {e}")
        conn.rollback()
    finally:
        conn.close()
    return

