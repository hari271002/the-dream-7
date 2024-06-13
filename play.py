import sqlite3
# In play.py
from adminn import admin
# from adminn.add_player import add_player
# from adminn.delete_player import delete_player
# from adminn.update_player import update_player
# from adminn.view_player import view_player
from user_functions.cal import calculate
from user_functions.user import user_selection


conn = sqlite3.connect('player.db') # connecting to the database
c=conn.cursor() # creating the cursor
c.execute("SELECT * FROM teamplayers")  # retreving the data from the table
data = c.fetchall() # storing the data in form of a list
c.close() # closing the connection


def play():
    print('Welcome the dream-7 :) ')
    while True:
        try:
            print('please enter 1 for admin login')
            print('please enter 2 to play the game')
            user_int=int(input()) # the user can enter only a number as a input
            break
        except ValueError:
            print('pls enter only a number')
    while user_int!=1 and user_int!=2:
        user_int=int(input('pls enter either 1 or 2 ')) # 1 or 2 is allowed
    if user_int==1:
        print('Hi admin :) welcome back ')
        admin.admin_operations()
    else:
        print('Welcome to the dream-7 game')
        print(f'In this game a user can select a maximum of 7 members out of {len(data)} members availble ')
        print('The selected 7 members are in a team and based on every individual player performance the total team score is calculated')
        print('The individual score of the player is calculated as given below ')
        print('--------------------------------')
        print('For every run scored 2 points are added to the score')
        print('If the batsman score is more than 50 extra 10 points are added to the score')
        print('If strike rate is more 200 extra 10 points are added to the score')
        print('For every wicket taken 10 points are added to the score')
        print('For every catch 10 points are added to the score')
        print('For every run out 5 points are added to the score')
        while True:
            try:
                no_of_users=int(input('enter the no.of players who want to play the game  ')) # the user is allowed only a number
                break
            except ValueError:
                print('enter only a number as input')
        while no_of_users<1:
            no_of_users=int(input("the minimum no.of users should be 1 ")) # the no. players should be greater than 0
        selected_teams=[] # this array stores the players teams
        for i in range(no_of_users):
            selected_teams.append(user_selection(i+1))
        res=[] # this array stores the total score
        for i in range(no_of_users):
            if(i>0):
                print('--------------')
            print(f"team {i+1}")
            res.append(calculate(selected_teams[i]))
        print(f"Player {res.index(max(res))+1} won the game")
    return
play()
