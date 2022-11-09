#!/usr/bin/python3
import random

from bot import Bot

vilains = ['X', 'Y', 'Z']
droids = ['Octa', "Neo", "Alpha"]

def newDroid():
    droid = random.choice(droids)
    new_droid = Bot(droid)
    return new_droid

def getGame():
    while True:
        print("Available villains: ",end="")
        print(*vilains, sep=" ")

        vilain = input("select your villain: ")

        if vilain == 'q':
            print("Exiting... Done")
            break

        elif vilain not in vilains:
            print("Select villain from given choices.")
            continue
        else:
            new_vilain = Bot(vilain)
            
            if new_vilain:
                new_droid = newDroid()
                print("Communist Detected, Initializing {}".format(new_droid))
                while True:
                    victim = random.choice([new_droid, new_vilain])

                    if victim == new_droid:
                        print(f"{new_droid} deals {new_vilain} 10 points!")
                        new_vilain.life -= 10

                    else:
                        print(f"{new_vilain} deals {new_droid} 10 points!")
                        new_droid.life -= 10

                    if new_vilain.life == 0:
                        print(f"Good job soldier, {new_vilain} is down")
                        break

                    elif new_droid.life == 0:
                        print(f"{new_droid} is down...")
                        new_droid = newDroid()
                        print(f"{new_vilain} still in play! Initializing new droid... {new_droid}")
                        continue
        
        print("\nAlien down, select new one to play")
        continue

getGame()
    