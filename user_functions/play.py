def play():
    print('Welcome :-)')
    print('please, enter 1 if you are a admin or enter 2 if you are a player')
    user_int=int(input())
    while(user_int!=1 and user_int!=2):
        user_int=int(input()) # the user can be only a player or a user
    if user_int==1:
        admin_username=input('enter the user name')
    while admin_username!='admin@123':
        print('wrong user name please try again')
