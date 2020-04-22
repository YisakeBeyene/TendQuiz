import sqlite3
import pandas as pd
import sys
import random

def LoginPage():
    print(""" Welcome to the Trendy Game:
                1)Login
                2)Sign Up
                3)Quit
    """)
    userInput = input("Enter Option: ")
    if userInput == '1':
        Login()
    elif userInput == '2':
        NewAccount()
    elif userInput == '3':
        closeGame()
    else:
        LoginPage()


def closeGame():
    sys.exit(0)


def NewAccount():
    print("Input your Credentials")
    dname = input('Input your Display Name')
    email = input('Input your email')
    score=0
    password=""
    passwordCheck = False
    while not passwordCheck:
        password = input('input password')
        password2 = input('input your password again')
        if password == password2:
            passwordCheck = True
            password=password2
        else:
            input('passwords were not the same')
    
    # if display name taken loop
    
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              INSERT INTO userData VALUES
              (?,?,?,?);''')
    
    paramarray=[password,email,dname,score]
    c.execute(param,paramarray,)
    conn.close()
    input('Done!')
    # store to database
    Login()


def Login():
    username = input("Email:")
    password = input("Password:")
    
    if usernameCheck(username,password):# Check SQL for username and password, return with true or false:
        mainPage(username)
    else:
        input("Login Failed, Press Enter to Try again")
        Login()

def usernameCheck(email,password):
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * from userData WHERE useremail = ? ;''')

    paramarray=[str(email)]
    c.execute(param,paramarray,)
    userdata=c.fetchall()
    conn.close()
    if str(userdata[0][0])==password:
        return True
    else:
        return False
    
    
    
    


def mainPage(username):
    print("To play game press P:")
    print("To see highscore press H:")
    print("TO change personal credentials press C:")
    print("To quit press Q:")
    value = input("Enter your input here:")
    value=value.capitalize()

    if value == 'P':
        score=playGame()
        updateHighscore(score,username)
    elif value == 'H':
        seeHighScore()
    elif value == 'C':
        changeCredentials()
    elif value == 'Q':
        closeGame()

def updateHighscore(score,email):
    print(score)
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * from userData WHERE useremail = ? ;''')

    paramarray=[str(email)]
    c.execute(param,paramarray,)
    masteruser=c.fetchall()
    conn.close()
    
    
    
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * from highscore WHERE userDisplay = ? ;''')

    paramarray=[masteruser[0][2]]
    c.execute(param,paramarray,)
    user=c.fetchall()
    conn.close()
    if not user:
        
        conn=sqlite3.connect('database.db',isolation_level=None)
        c= conn.cursor()
        
        paramarray=[masteruser[0][2],score]
        c.execute('''
              INSERT INTO highscore VALUES
              (?,?);''',paramarray)
        conn.close()
        
    elif user[0][1]<score:
        
        conn=sqlite3.connect('database.db',isolation_level=None)
        c= conn.cursor()
        paramarray=[score,masteruser[0][2]]
        c.execute('''
              UPDATE highscore SET highscore=? WHERE userDisplay=?;''',paramarray)
        conn.close()
    seeHighScore()
    
    

def seeHighScore():
    print("The top five highscores are:")
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * from highscore;''')

    
    c.execute(param,)
    user=c.fetchall()
    conn.close()
    for row in user:
        print(row)


def playGame():
    
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * from categories;''')
    c.execute(param,)
    cats=c.fetchall()
    conn.close()
    

    
    usedTerms=[]
    score=0
    for i in range(10):
        choice = random.choice(cats)
        displayOptions=(createQuestion(usedTerms,choice))
        displayOptions[0]=str(displayOptions[0])
        displayOptions[0] = displayOptions[0].replace('(', '')
        displayOptions[0] = displayOptions[0].replace(')', '')
        displayOptions[0] = displayOptions[0].replace('(', '')
        displayOptions[0] = displayOptions[0].replace('\'', '')
        print(displayOptions[0])
        useranswer=input(("Input your selection: "))
        usedTerms.append(displayOptions[2])

        if useranswer=='1':
            if displayOptions[3][0]==displayOptions[1]:
                score += 1
                print("You got the right answer")
            else:
                print("You didn't get the right answer. The right answer was " + displayOptions[1])
        if useranswer=='2':
            if displayOptions[3][1]==displayOptions[1]:
                score+=1
                print("You got the right answer")
            else:
                print("You didn't get the right answer. The right answer was " + displayOptions[1])
        if useranswer=='3':
            if displayOptions[3][2]==displayOptions[1]:
                score+=1
                print("You got the right answer")
            else:
                print("You didn't get the right answer. The right answer was " + displayOptions[1])
        if useranswer=='4':
            if displayOptions[3][3]==displayOptions[1]:
                score+=1
                print("You got the right answer")
            else:
                print("You didn't get the right answer. The right answer was " + displayOptions[1])
    return(score)



def createQuestion(used,choice):
    
    conn=sqlite3.connect('database.db',isolation_level=None)
    c= conn.cursor()
    param=('''
              SELECT * FROM searchTerms WHERE cat = ?;''')
    
    c.execute(param,choice,)
    results=c.fetchall()
    conn.close()
    for row in results:
        answer=row[2]
        options=[row[2].strip(),row[3].strip(),row[4].strip(),row[5].strip()]
        random.shuffle(options)
        if row[0] in used:
            pass
        else:
            
            question=(""""The category is :"""+str(choice)+"""
In Which Country was """+str(row[0])+""" the most searched term:"""+"""
                    
                    1) """+str(options[0])+"""
                    2) """+str(options[1])+"""
                    3) """+str(options[2])+"""
                    4) """+str(options[3]))
            answerarray=[question,answer,row[0],options]
            return answerarray
            
    
    


def changeCredentials():
    print(""" What do you want to change:
                    1)Name
                    2)Email
                    3)Password
                    4)Quit
        """)

    # This might need other additional helping methods
LoginPage()