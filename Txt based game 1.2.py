#imports
#==================================================================================================
import time
from time import sleep
import sys
#defines
#==================================================================================================
def slowtype(text):
    for char in text:   # this is to type out the characters in the game slowly, this is because the function is called slowtype
        sleep(0.045)
        sys.stdout.write(char)

def fasttype(text):     # this is t type out the characters in thr game faster, the function is called fasttype
    for char in text:
        sleep(0.005)
        sys.stdout.write(char)

def _help():
    print("test for help")    #this is all the commands I want the player (you) to know

def _map():
    print("test for map")    # a map of the region you play in, can be used to see the lay of the land, there are multiple maps for the smaller regions.

def fasttravel():
    slowtype("where do you want to go?\n")     #the movement feature of the game, you can travel to some of the locations in the game after reaching a certain level.
    print("1")
    print("2")
    print("3")
    x = input ("> ")
    if x == "1":
        slowtype("you caught the train to 1")  #this is the code for going to the first major location
    elif x == "2":
        slowtype("you caught the train to 2") # this is the code for fast travelling to the second location
    elif x == "3":
        slowtype("you caught the train to 3") # for travelling to the third major area
def _gamelogo():
    slowtype("                      G E N E R I C  G A M E  T I T L E\n\n")      # this is the game logo, I thought it looked cool so i used it.
    sleep(1)
    print("                         |\                     /)")                  # I was looking for a logo that was similar to a medieval styled fighting game.
    print("                       /\_\\__               (_//")
    print("                      |   `>\-`     _._      //`)")                   # then I came across this ascii art and thought it matched my criteria so i used it.
    print("                       \ /` \\  _.-`:::`-._  //")
    print("                        `    \|`    :::    `|")                       # The creator of the art is Joan Stark, so thansk to them for this amazing ascii art.
    print("                              |     :::     |")
    print("                              |.....:::.....|")
    print("                              |:::::::::::::|")
    print("                              |     :::     |")
    print("                              \     :::     /")
    print("                               \    :::    /")
    print("                                `-. ::: .-'")
    print("                                 //`:::`\\")
    print("                                //   '   \\")
    print("                               |/         \\")
    sleep(1)
def breaker():
    fasttype("\n\n=================================================================================")   #this is used to break up text to make the game easier on the eyes

def immortal():
    if _charselect =="dave":
        _damage = "0"

def _charface(name):
        
    if name=="DAVE":
            print("               T H I S  I S  D A V E")
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")     # this is my custom ascii art for thr character dave
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄.")
            print("⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⣤⣀⣀⡤⠴⠒⠒⠶⣤⠖⠛⠛⠛⠳⠶⠚⠛⠛⠛⠲⣤⠄⠄⠄⠄⠄⠄⠄⠄")     # please don't make fun of dave he is sensitive to insults AND constructive criticism
            print("⠄⠄⠄⠄⠄⠄⡴⠋⠉⠄⠄⠄⠄⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠓⣦⠄⠄⠄⠄⠄")
            print("⠄⠄⢀⡴⠖⠛⠇⠄⠄⠄⠄⠄⠄⠄⠄⣀⣀⣤⠤⠤⠤⠤⠤⢤⣄⣀⣀⠄⠄⠄⠄⠄⠄⡴⠿⡄⠄⠄⠄⠄")     # no really don't make fun of him D:
            print("⠄⠄⠘⠦⣤⣀⡀⠄⠄⠄⢀⣠⠴⠚⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠙⠲⢦⣄⠄⠄⠄⣠⠇⠄⠄⠄.")
            print("⠄⠄⠄⢸⣅⠄⠄⠄⣠⠶⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⠟⢶⡋⠁⠄⠄⠄⠄⠄")     #you asked for this... karen... A GREAT GAME (what else did you think I was implying... smh)
            print("⠄⠄⠄⠄⠈⠉⣻⢿⣥⣄⣀⣀⣀⣀⣴⣄⡀⠄⠄⠄⠄⠄⢀⣠⡜⠲⠶⠶⠒⠛⠁⠄⠄⠘⢷⡄⠄⠄⠄⠄")
            print("⠄⠄⠄⠄⢀⣴⣣⠿⣥⣤⡬⠿⠉⠄⠄⠈⠉⠙⠓⠒⠒⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣆⠄⠄⠄")
            print("⠄⠄⠄⠄⡼⠛⠛⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣀⣀⣀⠄⠄⠄⠄⠄⠘⣇⠄⠄")
            print("⠄⠄⠄⣸⠃⠄⠄⠄⠄⠄⠄⢀⡴⠛⠛⠳⣤⠄⠄⠄⠄⠄⠄⠄⠄⠄⡼⠋⠄⠄⠉⢳⠄⠄⠄⠄⠄⢸⡄⠄")     # Dave was born in the year 1405 and is immortal but you wouldn't of picked dave because you saw
            print("⠄⠄⠄⡿⠄⠄⠄⠄⠄⠄⠄⢸⡀⠄⠄⠄⣸⠇⠄⠄⠄⠄⠄⠄⠄⠄⢳⣄⠄⠄⣀⡼⠄⠄⠄⠄⠄⠈⣇⠄")
            print("⠄⠄⠄⡇⠄⠄⠄⠄⠄⠄⠄⠄⠙⠶⠶⠞⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⣿⠄")     # Karen as a playable character, you fool, you should've checked the notes before picking your
            print("⠄⠄⠄⣿⠄⠄⠄⠄⣀⣀⣤⠶⠒⠒⠒⠲⠶⠛⠛⠛⠒⠛⠛⠛⠛⠛⠛⠛⠛⠲⢶⣤⡀⠄⠄⠄⠄⢠⡏⠄")
            print("⠄⠄⠄⠸⡆⠄⠄⠈⠻⠿⢧⣤⣄⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣤⣀⣀⣽⠿⠶⠖⠚⠃⠄⠄⠄⠄⣸⠁⠄")     #  character. You will suffer damage, dave will not, dave is a god, your character is not.
            print("⠄⠄⠄⠄⢻⡄⠄⠄⠄⠘⠛⠛⠛⠋⠉⠄⠄⠄⠉⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣰⠇⠄⠄")
            print("⠄⠄⠄⠄⠄⠹⣆⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡴⠋⠄⠄⠄")     # of course, no one knows dave is immortal, only you can find the hidden command to make dave
            print("⠄⠄⠄⠄⠄⠄⠈⠷⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⠞⠁⠄⠄⠄⠄")
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠉⠳⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⡴⠛⠁⠄⠄⠄⠄⠄⠄")    #immortal
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠓⠶⣤⣄⣀⠄⠄⠄⠄⠄⠄⠄⢀⣀⣠⡤⠖⠋⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄")
            print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠉⠉⠛⠛⠛⠋⠉⠉⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")

    elif name=="KAREN":
        print("          T H I S  I S  K A R E N")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")    # this is karen they enjoy making string ( its the midde ages she desn't know code)
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
        print("⠄⠄⠄⠄⠄⢀⣀⣀⣠⣤⣄⣀⣠⣤⣤⣤⣤⣤⣤⣴⣖⣒⠲⢦⠤⠶⠒⠒⠲⠦⢤⣀⡀⠄⠄⠄⠄⠄⠄⠄")    # karen was born on 1400 being the oldest character, since the year you play in is 
        print("⠄⣀⣠⣶⣶⣍⠉⠄⠄⣀⡤⠞⠛⠉⠉⠁⠄⠄⠄⠄⠉⠉⠙⠒⠦⣄⡀⠄⠄⠄⠄⣉⣯⣷⡄⠄⠄⠄⠄⠄")
        print("⢸⢿⣿⣿⡇⣿⢀⣴⠚⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠙⢶⣤⣤⣶⢻⢛⣻⡿⠄⠄⠄⠄⠄")    # 1430.
        print("⣸⠈⠷⢤⣤⣽⣯⠁⠄⠄⠄⠄⠄⣀⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣀⣀⣀⣀⣹⣾⠋⠉⠉⠉⡇⠄⠄⠄⠄⠄")
        print("⣷⠄⠄⣹⠋⢩⡏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢀⣾⠈⣷⠄⠄⣿⠄⠄⠄⠄⠄")    #this ascii art was not inpired by you ( i swear) you also probably picked this character 
        print("⠇⠄⢰⡏⠄⠸⡇⡰⠖⠋⠉⠛⠶⡄⠄⠄⢀⡆⠄⠄⠄⢀⡴⠶⠶⠶⢦⡀⢸⡇⠄⠈⡇⠄⣿⠄⠄⠄⠄⠄")
        print("⠄⠄⢸⡇⢀⠄⡟⢧⣀⣀⣀⣀⣤⠇⠄⠄⡿⠄⠄⠄⠄⣇⡀⠄⠄⠄⢀⡿⢸⡇⠄⠄⡇⣄⣿⠄⠄⠄⠄⠄")    # because it shares the same name as you, you also probably had a rather big panic attack from seeing 
        print("⡇⠄⢸⡇⠘⣆⡇⠄⠉⠉⠉⠉⠄⠄⠄⣸⠁⠄⠄⠄⠄⠈⠑⠒⠒⠒⠋⠁⢈⡧⠄⠄⡇⢹⡿⠄⠄⠄⠄⠄")
        print("⡇⠄⠘⡇⠄⣿⠁⠄⠄⠄⠄⠄⠄⠄⠐⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡇⠄⢠⡇⢸⠃⠄⠄⠄⠄⠄")    # my bad ascii art, but it is the best I can do.
        print("⡇⠄⠄⢹⡆⡿⠄⠄⠄⠄⠄⠄⠄⠄⢀⣰⠶⣄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⣇⠄⡾⢀⢸⠄⠄⠄⠄⠄⠄")
        print("⢧⠄⠄⢰⣿⣇⠄⠄⠄⠄⠄⠄⠄⢴⡛⠁⠄⠈⢳⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⡾⡅⢸⠟⠄⠄⠄⠄⠄⠄")    # Karen Doesn't do much in her spare time, but since you chose karen as your adventurer, she is now
        print("⢸⢀⡇⢸⡟⠙⣆⠄⠄⠄⠄⠄⠄⠈⠑⢦⣠⡖⠋⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣾⣾⣧⡟⠄⠄⠄⠄⠄⠄⠄")   
        print("⢸⣿⢧⡼⠁⠄⠈⠱⣤⡀⠄⠄⠄⠄⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄⢀⣠⠾⠁⢸⣿⠉⠁⠄⠄⠄⠄⠄⠄⠄")    # thrown into battle, of course it doesn't matter that she hasn't ever battled before only you can
        print("⣼⡿⠄⠄⠄⠄⠄⠄⠄⠙⠳⠤⣄⣀⡀⠄⠄⠄⠄⠄⠄⣀⣀⡤⠞⠋⠁⠄⠄⣼⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄") 
        print("⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠉⠉⠛⠒⠒⠒⠛⠉⠉⠁⠄⠄⠄⠄⠄⠄⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")    # decide if she is bad at fighting or not.  
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")    # Overall karen is a pretty chill character.
        print("⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄")

    
#actual game code
#====================================================================================================
_gamelogo()

fasttype("\n\n================================= INTRO ========================================")
slowtype("\n\nwelcome, pick a character...\n\n Dave\n Karen\n\n")
while True:
    _charselect = input("> ").upper()   # input for selection of character 
    _charface(_charselect)
    
    if _charselect == "KAREN":
        slowtype("epic\n")
    elif _charselect == "HELP":
                print(" select a character by typing out their name, must be the full name.")
                
    elif _charselect =="DAVE":
        slowtype("dave hides a secret... find it\n\n")
