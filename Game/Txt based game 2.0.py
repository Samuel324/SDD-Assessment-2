
# SAM'S MEDIEVAL FIGHTING GAME
import time
import sys
from time import sleep
import random
import os
from typing import ClassVar

_inventory1 = ["Inventory", "Inv", "I"]
_fight = ["ATTACK", "A"]
_block = ["BLOCK", "B"]
_run = ["RUN", "R"]

_monsters1 =["Comically Large Snail :O", "Swarm Of Gentle Bees :)", "angry ladybug D:<", "A Living Trumpet (how!?)", "The Colour Purple (I think its angry)"]
_monsters2 =["wild Dog", "Pit Of Snakes", "Bandit", "Wolf", "Stray Cat", "Hog"]
_monsters3 =["Small dragon", "Medium dragon", "Firebreathing Dragon", "Icebreathing Dragon", "Pack Of Wolves"]

_randevents =["Street Brawl", "Drowning Peasant", "Lost Animal"]

_locations =["Bexley", "Aerlion", "Walden"]

_BexleyLocations =["Butter pond", "Snow Bushes", "Golden Groves"]
_AerlionLocations =["Wolves lair", "Hogs Pines", " Murkey River"]
_WaldenLocations =["CullField", "Myrefall", "Black Hallows"]

class Monster:
    def __init__(self, name, health):
        self.health = health
        self.name = name

class Player:
    def __init__(self, name, health):
        self.name = name
        self.health = health

p = Player(1, 20)

def Attack(m1):
     x = (1)
     m1.health -= x
     slowtype("You hit the " + m1.name + " for " + str(x))

def CritHit(m1):
    x = random.ranint(2,3)
    m1.health -=x
    slowtype("You just crit hit the" + m1.name + " for " + str(x))

def Damaged(m1):
    x = random.int(1,2)
    p.health -= x
    slowtype("The" + m1.name + "hit you for " + str(x))


def Fight1():
    x = _monsters1[random.choice(0,4)]
        

        
def dead():
    slowtype("You died, better luck next time.") 
    time.sleep(1)
    exit 

def _help():
    print("\nYou can fast travel between major cities with [fasttravel x], but you must be in a major city to do so.")
    print("You can travel so sub locations to fight monsters by using [travel to x]")
    print("You can access your inventory with [i]")
    print("When asked a question, ie 'can you come here?' use the command [goto x] to go that person (or monster)")
    print("To pick stuff up use the [pickup x] command")
    print("To place or drop an item in your inventory, [drop x]")

def slowtype(text):
    for char in text:
        sleep(0.05)
        sys.stdout.write(char)
def fastype(text):
    for char in text:
        sleep(0.005)
        sys.stdout.write(char)

def fasttravel():
    while True:
        x = input("> ")
        if x =="Bexley".lower:
            slowtype("you have fast travelled to Bexley")
        elif x =="Aerlion".lower:
            slowtype("you have fast travelled to Aerlion")
        elif x == "Walden".lower:
            slowtype("you have fast travelled to Walden")
        else:
            print("thats not a location you can fast travel to...")
        break

slowtype("What is your characters name? ")
PlayerName = input("\n> ").capitalize()
slowtype("Lets get started then.\n")
time.sleep(0.5)
slowtype("In a world, filled with danger around every corner. . .\n")
time.sleep(0.5)
slowtype("Only one person has the power to stop this evil from taking over.\n")
time.sleep(0.5)
slowtype(PlayerName + " is that person\n")
time.sleep(0.5)
slowtype("Become " + PlayerName + " and fight monsters throughout the world.\nAnd go on grand adventures through the 3 Major Locations\n")
time.sleep(0.5)
slowtype("Bexley")
time.sleep(0.5)
slowtype("\nAerlion")
time.sleep(0.5)
slowtype("\nWalden\n")
time.sleep(1.2)

slowtype("Are you ready?")
while True:
    ready = input("\n> ")
    if ready.lower() == "y" or ready.lower()=="yes":
        slowtype ("lets go!")
        break
    elif ready.lower() == "n" or ready.lower() =="no":
        slowtype("reply 'yes' or 'y' when you are ready, the world needs you\n")

fastype("\n\n=================================================== HOW IT WORKS ============================================================\n")
time.sleep(2)
_help()
time.sleep(5)
slowtype("\ndo you understand how this game works? ")
while True:
    understand = input("\n> ")
    if understand.lower() =="yes" or understand.lower() =="y":
        break
    elif understand.lower() == "no" or understand.lower() == "n":
        slowtype("just look over the commands until you do.\n")

fastype("\n\n===================================================== PROLOGUE ==============================================================\n\n")
print("in the prologue you will have helpful tips to the right side of the screen i.e [yes] or [no]\n")
time.sleep(1)
slowtype("\n\nthe year is 1200")
time.sleep (0.5)
slowtype("\n" + PlayerName + " is just 6 years old\n")
time.sleep(1)
slowtype("FATHER: " + PlayerName + " can you come here? [goto father]\n")
while True:
    gotoFather = input("\n> ")
    if gotoFather.lower() == "goto father":
        slowtype(PlayerName + ": Yes!")
        slowtype("\n*" + PlayerName + " walked over to their father.\n")
        break
    else:
        slowtype("You must go to your father to continue the story.\n")
time.sleep(0.5)
slowtype("Father: Can you help me move this hay to our barn over there? [yes / no]\n")

while True:
    HelpFather1 = input("\n>")
    if HelpFather1.lower() == "yes" or HelpFather1.lower() == "y":
        slowtype("'Thanks, thats your pile of hay just there!'\n")
        break
    elif HelpFather1.lower() == "no" or HelpFather1.lower() == "n":
        slowtype("Mother: You idiot, not helping your father, shameful, just shameful.")
        slowtype("\n You'll get less food for dinner tonight.\n")
slowtype("You need to move the hay to the barn \nbut first you need to pick it up. [pickup hay]\n")

while True:
    PickupHay = input("\n> ")
    if PickupHay.lower() == "pickup hay":
        break
    else:
        slowtype("You have to pick up the hay\n")
slowtype("You picked up the hay [i to see in inventory]\n" )

slowtype("Move the hay to the barn [travel to barn]\n")
while True:
    Movehay = input("\n> ")
    if Movehay.lower() == "travel to barn":
        slowtype("You struggled over to the barn\n")
        break
    elif Movehay.lower() == "no" or Movehay.lower() == "n":
        slowtype("You must go to the barn to comnplete the prologue\n")

slowtype(" Place the hay down [drop hay]\n")
while True:
    PlaceHay = input("\n> ")
    if PlaceHay.lower() == "drop hay":
        slowtype("* You dropped the hay\n")
        break
    else:
        print("That's not a thing you can do\n")

slowtype("you hear a noise.\nDo you investigate? [yes / no]")
while True:
    investigate1 = input("\n> ")
    if investigate1.lower() == "yes" or investigate1.lower() == "y":
        slowtype("You chose to investigate the noise")

        break
    elif investigate1.lower() == "no" or investigate1.lower() == "n":
        slowtype("You chose to ignore the noise\n")
        slowtype("You start to return to your shack. . .\nBut then!\n")
Fight1()
