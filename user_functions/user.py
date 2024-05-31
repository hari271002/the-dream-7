import sqlite3

def user_selection(team_no):
    conn = sqlite3.connect('./player.db') # connecting to the database
    c=conn.cursor()  # creating a cursor
    c.execute('SELECT * FROM teamplayers') # retriving data from the table
    players_list=c.fetchall() # this will return the data in array with all stats 
    players_availble=[]  # this will store only the names
    print('-----------------')
    for i in players_list: 
        print(i[0])   # this will print the every player who are available for the selection
        players_availble.append(i[0])
    print('-----------------')
    selected_players=[] # this array will store the selected players
    count=0 # this is used to count the no. of selected players only 7 are allowed
    while(count<7):
        user_in=input('select a player from the player_list:  ') 
        try:
            if user_in in players_availble and (user_in not in selected_players):
                selected_players.append(user_in)
                players_availble.remove(user_in)
                count+=1
                print('the players to be selected more {}'.format(7-count)) # this shows the user how many are selected
                print('-----------------')
                print('\n'.join([i for i in players_availble])) # this will print the availble players who are not still selected
                print('-----------------')
                print(f"The players in the team no. {team_no}")
                print('\n'.join([i for i in selected_players])) # this will print the selected players
                print('-----------------')
            else:
                if user_in in selected_players:
                    print('The player is already selected')
                else:
                    print('The player is not available')
        except Exception as e:
            print("An error occurred:", e)
    conn.close()
    return selected_players # this will return the selected players in a array