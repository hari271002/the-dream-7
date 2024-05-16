import sqlite3 #importing sqlite package


from adminn import add_player
from adminn import delete_player
from adminn import view_player
from adminn import update_player

def admin_operations():  
    admin_id=input('please, enter the admin user id :)  ') # takes input from the user to verify the admin id
    while admin_id!='admin@123': # this loop will not allow to user give wrong admin id and if user want to exist he/she press 1
        print('wrong user name please try again :)  ')
        admin_id=input('please, enter the admin user id :) or if you like exit pls enter 1  ')
        if admin_id=='1':
            return 
    admin_password=input('please, enter the password :)  ') 
    while admin_password!='123$5678': # takes input from the user to verify the password
        print('sorry , wrong password please try again :) or if you like exit pls enter 1  ')
        admin_password=input('please, enter the password :)  ')
        if admin_password=='1':
            return
    print('You have successfully logined :)')
    while True:  # this loop will helps the admin to run the functions as many times as he want
        print("These are the operations you can perform")
        print("------------------------")
        print("1. Update Player stats.")
        print("2. view player stats.")
        print("3. Add a player.")
        print("4. Delete a Player.")
        print("5. Log Out")
        operation_input=int(input('pls enter a number between 1 and 5 ')) # this takes input for the operation to perform
        while operation_input not in range(1,6): # this will ensure it only takes correct input 
            print('wrong input pls try again ')
            operation_input=int(input('pls try again or if you like exist pls enter 10  '))
            if operation_input==10:
                return
        if operation_input==1:
            update_player.updating()
        elif operation_input==2:
            view_player.viewing()
        elif operation_input==3:
            add_player.adding()
        elif operation_input==4:
            delete_player.deleting()
        else:
            print('Logging out')
            break

    return 



    

