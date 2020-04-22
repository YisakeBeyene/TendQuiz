import sqlite3
import pandas as pd
import sys


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
            passwword=password2
        else:
            input('passwords were not the same')
    displayName = input('Choose a display name:')
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
    username = input("Username:")
    password = input("Password:")
    usernameCheck = True  # Check SQL for username and password, return with true or false
    if usernameCheck:
        mainPage()
    else:
        input("Login Failed, Press Enter to Try again")
        Login()




def mainPage():
    print("To play game press P:")
    print("To see highscore press H:")
    print("TO change personal credentials press C:")
    print("To quit press Q:")
    value = input("Enter your input here:")

    if value == 'P':
        playGame()
    elif value == 'H':
        seeHighScore()
    elif value == 'C':
        changeCredentials()
    elif value == 'Q':
        closeGame()


def seeHighScore():
    print("The top five highscores are:")
    print("1)" + "The name from DB" + "Score from DB")
    print("2)" + "The name from DB" + "Score from DB")
    print("3)" + "The name from DB" + "Score from DB")
    print("4)" + "The name from DB" + "Score from DB")
    print("5)" + "The name from DB" + "Score from DB")


def playGame():
    for i in range(10):
        createQuestion(i)


def createQuestion(i):
    # Choses randomly from a group of questions
    print("Soemthing")


def changeCredentials():
    print(""" What do you want to change:
                    1)Name
                    2)Email
                    3)Password
                    4)Quit
        """)

    # This might need other additional helping methods
NewAccount()