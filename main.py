import sys, math, random, time, pygame

def userInput():
    userChoice = input()
    try:
        userChoice = int(userChoice)
        print('you have chosen number')
    except:
        print('you have chosen word')

    print(userChoice)

running = True
while running:
    
    print('would you like to store a number or word?')
    userInput()

    break