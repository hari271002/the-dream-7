import sqlite3

def deleting():
    conn = sqlite3.connect('./player.db')#creating connection with the player data base
    c=conn.cursor() #creating the cursor
    c.execute('SELECT * FROM teamplayers') # fecting the details fromt the teamplayers table
    data=c.fetchall() # return data in list
    if len(data)==0:
        print("There are no players in data base")
        return
    delete_player=input('enter the player name to delete ') # user has to enter the name of the player he wants to delete
    temp=True
    while temp: # this loop will ensure the user can enter only a correct name
        for i in data:
            if delete_player==i[0]:
                temp=False
                break
        else:
            delete_player=input('pls enter the correct name or available player ')
    c.execute("DELETE FROM teamplayers where name=?",(delete_player,)) # deleting the row
    print('Successfuly deleted ')

    conn.commit()
    conn.close()
    return 


