# Import Usage of Player Game Commands
from gamecommands import gamecommands

# Retreive User Input then test for Commands

# Commands to run on start
gamecommands("look")
print("Use the 'help' command to get started if you are confused")

while 1==1:
  print("\n")
  userInput = input(">")
  gamecommands(userInput)

# currently working on areas/tiles