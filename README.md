# AP Computer Science Principles Create Task

This project is for the AP CSP Create Task. The project is simply a collection of python files to gauge progress. I would continue to use repl.it as a repository, but I have migrated my program to the PyCharm IDE for easier development; however, this means that I would have to tediously copy over files and directories to maintain my code with repl.it. Also, the addition of GUI elements were incompatible with a browser-based environment. 

## April 27th In Class Create Task Progress

During the April 27th class period, I primarily worked on map values which will become different section which the player will be able to explore during the course of the game. These files can be found in gui-sys/maps. If you open a map file you will see several lines of characters. Each character corresponds to a specific tile-type in the game, and each line will be represented as row of tiles. The numbered characters 7,8,9, and 0 represent teleport points which will take the player to its destination tile, as specified in the current room's object variable. Together these maps form the entire game which the player will be able to reverse. Once completed, there should also be two buildings the user can go into and two NPCs the user will be able to interact with to further the game.

## Current Development

Currently, the repository is primarily split between the main program in the main directory and the gui system in the gui-sys/ directory. My intention is to merge these programs to allow for the data structures and classes of the main program to be displayed and interacted with through the gui system.
