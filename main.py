

def mainPage():
    print("To play game press S:")
    print("To see highscore press H:")
    print("TO change personal credentials press C:")
    print("To quit press Q:")
    value = input("Enter your input here:")

    if value == 'S':
        print("The function for questions page")
    elif value == 'H':
        print("The function for highscore page")
    elif value == 'C':
        print("The function for changeing credentials page")
    elif value == 'Q':
        print("The function for quiting")
