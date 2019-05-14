import os
import random
import time


def gameMenu():
    print("")
    print("")
    print(' THIS IS A QUIZ RELATED TO PYTHON '.center(80, '*'))
    print("")
    print("")
    print("")
    print(' MENU '.center(80, '*'))
    print("")
    print("")
    print(' Press S to start the game '.center(80))
    print(' Press I to read instruction '.center(80))
    print(' Press H to see high score '.center(80))
    print(' Press C to see credits '.center(80))
    print(' Press Q to start the game '.center(80))


def instructions():
    print("1 correct answer = 1 point")
    print("1 wrong answer deducts 0.5 point")
    print("This quiz is about country and capital more menus will be added further")
    print("This quiz is not case sensitive.")
    print("")
    print("")
    print("Press M to go back to menu".center(80))
    keyInput = input().upper()
    if keyInput == "M":
        main()



def startGame():
    data = {
        "Afghanistan" : "Kabul",
        "India" : "Delhi",
        "Pakistan" : "Islamabad",
        "Bhutan" : "Thimpu",
        "Bangladesh" : "Dhaka",
        "USA" : "Washington DC",
        "Brazil" : "Rio De Jenerio",
        "China" : "Beijing",
        "Australia" : "Canberra",
        "Austria" : "Vienna",
        "Japan" : "Tokyo",
        "Russia" : "Moscow",
        "France" : "Paris",
        "Bangladesh" : "Dhaka",
        "Canada" : "Ottawa",
        "Sri Lanka" : "Colombo",
        "Belgium" : "Brussels",
        "Saudi Arabia" : "Riyadh"
    }
    question, answer = random.choice(list(data.items()))
    return question, answer


def credits():
    print(" CREATED BY ".center(80,'x'))
    print(" Abhishek Raj ".center(80))
    print(" abhishekraj272@gmail.com ".center(80))
    print("")
    print("")
    print("")
    print("Press M to go back to menu".center(80))
    keyInput = input().upper()
    if keyInput == "M":
        main()



def profile():
    global name
    print("Please enter the following details")
    fName = input("First Name: ")
    lName = input("Last Name: ")
    name = fName + " " + lName
    return name


def saveScore():
    global strPoint
    global strRtQue
    global name
    file = open("highScore.txt", "a+")
    file.write(name + " scored " + strPoint + " points and answered " + strRtQue + " question correctly")
    file.close()

def viewScore():
    file = open("highScore.txt", "r")
    fileContents = file.read()
    print(fileContents)
    file.close()
    print("")
    print("")
    print("")
    print("")
    print("Press M to go back to menu".center(80))
    keyInput = input().upper()
    if keyInput == "M":
        main()


def question():
    global strPoint
    global strRtQue

    point = 0
    rtQue = 0
    name = profile()
    os.system('cls')
    for i in range(10):
        queData, ansData = startGame()
        ansDataLower = ansData.lower()
        print("What is the capital city of " + queData + "?")
        getAns = input().lower()
        os.system('cls')
        if getAns == ansDataLower:
            print("Congratulation! " + name + " Your answer is correct.")
            point += 1
            rtQue += 1
        else:
            print("Your answer is wrong.")
            point -= 0.5
        time.sleep(1)
        os.system('cls')
        strPoint = str(point)
        strRtQue = str(rtQue)
    print("The quiz is now over")
    print("You answered " + strRtQue + " questions correctly.")
    print("You got " + strPoint + " points")
    saveScore()
    

def main():
    
    os.system('cls')
    gameMenu()
    startCmd = input().upper()
    os.system('cls')
    if startCmd == "S":
        question()

    elif startCmd == "Q":
        exit()

    elif startCmd == "H":
        viewScore()

    elif startCmd == "I":
        instructions()
    
    elif startCmd == "C":
        credits()

    #elif startCmd == "I":
    #    viewScore()

main()