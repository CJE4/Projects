import random
import time

#choice of activity
acivity = int(input("Chose 1 of 2 options. \n 1: Create a random strong password \n 2: Test current password strength\n 1 or 2? "))
if acivity == 1:

    #directions
    print("\nThis code will generate a very strong password using an algorithm based on your information and the website its for.\n ")
    print("This algorithm will use the: \n 2nd letter of your favortite color \n 1st letter of the website's name \n 3rd letter of your name \n How old you are (and add +10)")
    print("\nAfter that it will take a random letter from: \n Your favortite color \n The website's name \n Your name \n ")
    print("Then it will count up the amount of letters in: \n Your favortite color \n The website's name \n Your name \n")
    print("Then it will take a random letter from: \n Your favortite color \n The website's name \n Your name \n")
    print("Then after that it will generate a random symbol to pur into your password. ")
    print("\nFinally it will randomize the order of everything if you would like (will make it stronger) and then send your strong password.\n")
    time.sleep(2)

    randomized = False

    #questions
    color = input("What is your favorite color? ")
    company = input("\nType the name of the website: ")
    name = input("\nWhat is your name? ")
    age = int(input("\nHow old are you? (ex. 12, 15...) "))
    randomize = input("\nWould you like your end password in a randomized order? (yes or no)").lower()
    if randomize == "yes":
        randomized = True
    elif randomized == "no":
        randomized = False
    else:
        print("Not a valid answer, your password order will not be randomized")
        randomized == False

    # seperate letters
    companyl = [x for x in company]
    colorsl = [x for x in color]
    namel = [x for x in name]

    #vowel count
    colorcount = 0 
    lettercount = 0
    namecount = 0 

    newage = 0 #age number add


    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']
    #amount of letters
    numcompany = len(companyl) 
    numcolor = len(colorsl)
    numname = len(namel) 

    #adds number for add
    newage = age + 10
    
    # Counts amount of vowels in words
    for letter in color:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            colorcount = colorcount + 1

    for letter in companyl:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            lettercount = lettercount + 1

    for letter in namel:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'y':
            namecount = namecount + 1

    # Picks letter from word
    firstcompany = company[0] #1st letter 
    secondcolor = color[1] #2nd letter 
    thirdname = name[2] #3rd letter 

    # random letter from
    randomcolor = random.choice(color)
    randomname = random.choice(name)
    randomletter = random.choice(company)
    randomsymbol = random.choice(symbols)

    #PASSWORD
    password= [
        secondcolor,
        firstcompany, 
        thirdname,
        str(newage),
        randomcolor,
        randomletter, 
        randomname,
        str(numcolor),
        str(numcompany),
        str(numname),
        str(colorcount),
        str(lettercount), 
        str(namecount), 
        randomsymbol]

    #sees if user wants password order randomized
    if randomized == True:
        random.shuffle(password)
    else:
        pass

    password_str= "".join(password)

    print(f"\n Password = {password_str}")
else:
    given = input("\nEnter password to test: ")
