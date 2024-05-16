import sqlite3



    
    
def user_selection():
    conn = sqlite3.connect(r'C:\Users\DEVELOPER--3\Desktop\projects\dream-7\player.db') # connecting to the database
    c=conn.cursor()  # creating a cursor
    c.execute('SELECT * FROM teamplayers')
    players_list=c.fetchall()
    print('-----------------')
    for i in players_list:
        print(i[0])
    print('-----------------')
    # selected_players=[]
    # count=0
    # while(count<7):
    #     user_in=input('select a player from the player_list:  ')
    #     try:
    #         if user_in in players_list and user_in not in selected_players:
    #             selected_players.append(user_in)
    #             players_list.remove(user_in)
    #             count+=1
    #             print('the players to be selected more {}'.format(7-count))
    #             print('-----------------')
    #             print('\n'.join([i for i in players_list]))
    #             print('-----------------')
    #             print('\n'.join([i for i in selected_players]))
    #             print('-----------------')
    #         else:
    #             if user_in in selected_players:
    #                 print('The player is already selected')
    #             else:
    #                 print('The player is not available')
    #     except Exception as e:
    #         print("An error occurred:", e)
    conn.close()
    # return selected_players

def calculate(arr):
    res=[]
    conn=sqlite3.connect('player.db')
    c=conn.cursor()
    c.execute("SELECT * FROM teamplayers")  
    data = c.fetchall()
    for i in arr:
        score=0
        for j in data:
            if i==j[0]:
                score+=j[1]*2
                if j[1]>=50:
                    score+=10
                if j[3]>=200:
                    score+=10
                if j[6]>=1:
                    score+=(j[6]*10)
                if j[7]>=1:
                    score+=(j[7]*7)
                if j[8]>=1:
                    score+=(j[8]*5)
                score+=2
        res.append(score)
    for i in range(7):
        print(arr[i],'-',res[i])

    return sum(res) 

def play():
    print('Welcome to the game :)')
    print('These game is played between 2 persons')
    print('A player can choose a maximum of 7 players')
    player_1=user_selection()
    player_2=user_selection()
    total_1=calculate(player_1)
    total_2=calculate(player_2)
    print('team_1_total:-',total_1)
    print('team_2_total:-',total_2)
    if(total_1>total_2):
        return 'player_1_wins'
    return 'player_2_wins'
user_selection()
