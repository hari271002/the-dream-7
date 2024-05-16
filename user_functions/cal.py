import sqlite3


def calculate(arr):
    res=[]
    conn = sqlite3.connect(r'C:\Users\DEVELOPER--3\Desktop\projects\dream-7\player.db') # connecting to the database
    c=conn.cursor()
    c.execute("SELECT * FROM teamplayers")  
    data = c.fetchall()
    for i in arr:
        score=0
        for j in data:
            if i==j[0]:
                score+=j[1]*2 # for every run scored 2 points are added to the score
                if j[1]>=50:
                    score+=10  # if the score is more 50 extra 10 points are added to the score
                if j[3]>=200:
                    score+=10  # if strike rate is more 200 extra 10 points are added to the score
                if j[6]>=1:
                    score+=(j[6]*10) # for every wicket taken 10 points are added to the score
                if j[7]>=1:
                    score+=(j[7]*7) # for every catch 10 points are added to the score
                if j[8]>=1:
                    score+=(j[8]*5) # for every run out 5 points are added to the score
                score+=2 # if the selected player is playing 2 points are added to the score
        res.append(score) # the individual player score is added into the res array
    for i in range(7):
        print(arr[i],'-',res[i]) # printing the score of individual players
    print(f'the total score is {sum(res)}')

    return sum(res) # adding every individual score in the res array



