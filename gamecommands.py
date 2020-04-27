# gamecommands processes the input from the user then changes variables to continue the getattr

# Allow functions to be used in game commands
from functions import *

def gamecommands(command):
  if(player.interface == "default"):
    # test command
    if(command == "test"):
      print("test command being processed")
      goToRoom(2)
    # basic help command
    elif(command == "help"):
      print("Try moving around with the different cardinal directions: north, south, east, and west. You should also probably see what you have on you with the 'inventory' command.")
    # user stop command
    elif(command == "stop" or command == "quit" or command == "exit"):
      exit()
    # user movement command
    elif(command == "north" or command == "east" or command == "south" or command == "west"):
      moveDirection(command)
    # user check surroundings command
    elif(command == "look" or command == "look around"):
      goToRoom(player.room)
    # displays the user's inventory
    elif(command == "inventory" or command == "inv"):
      displayArray("Inventory - ${}".format(player.money), player.inv)
    # allows the user to access the shop interface
    elif((command == "what's for sale?'" or command == "what is for sale?" or command == "what's for sale" or command == "what is for sale")) and player.room == 14:
      # start shop interface and redirect all commands to shop reference
      player.interface = "shop" # switch player interface
      shopCommand("start") # start the shop system
    # allows the player to talk to the old man
    elif((command == "hello") and player.room == 16):
      player.interface = "man"
      talkToMan("start")
    # if no valid command is entered by the user
    else:
      print("Not a command")
  elif (player.interface == "shop"):
    shopCommand(command)
  elif (player.interface == "man"):
    talkToMan(command)
  else:
    print("Error: player interface has not been properly defined")
