__author__ = 'PaleToys'

import time
global gold
global apples
apples = 0
gold =  0




def start():
    print("hellow and welcome!")
    name = input("What's your name:")
    print( "\n\nwelcome, " + name + "!")
    print ("the objective of this game is to collect apples.")
    print ("After collecting the pples you sell them. ")


    choice = input("Do you want to play Y/N?")
    choice.upper()
    if choice == "Y":
        begin()
    if choice == "N":
        print ("Okay, bye.....")


def begin():
    global apples
    print( "Let's get started")
    pick = input("Do you want to pick apples?")
    pick.upper()
    if pick == "Y":
        time.sleep(1)
        print("You pick an apple.")
        apples= apples + 1
        print ("You currently have, " + str(apples) + " apples")
        begin()
    if pick == "N":
        sell = input("Do you want to sell your apples y/n?")
        sell.upper()
        if sell  == "Y":
            global gold
            global apples
            print("You currently have," + str(apples) + " apples")
            print(" You've have sodld your apples")
            gold = apples * 10;
            apples = 0;


start()