# AP Computer Science Principles Create Task

This project is for the AP CSP Create Task. The project is simply a collection of python files to gauge progress. I would continue to use repl.it as a repository, but I have migrated my program to the PyCharm IDE for easier development; however, this means that I would have to tediously copy over files and directories to maintain my code with repl.it. Also, the addition of GUI elements were incompatible with a browser-based environment. 

## May 7th In Class Create Task Progress

During the May 7th class period, I removed depracated files and functions from my program code and reduced the overall vision for the game. I also began planning to answer the prompts and gave credit to the pygame library.

  Note: the customDisplayText function may be duplicated and needs to be consolidated

## May 4th-6th Out of Class Create Task Progress

Outside of class from May 4th to May 6th, I finished planning for the overall program and decided to proritize working on responses over further game development since the current program illustrates the required elements and functions properly, although it does lack overall gameplay/plot. I spent the out of class time prioritizing the required elements, cleaning code segments, deciding on code segments to discuss in written responses, and beginning to write the written responses.

## May 4th In Class Create Task Progress

During the May 4th class period, I remapped inputs and fixed NPC-related bugs in my prorgam.

## Apirl 30th-May 3rd Out of Class Create Task Progress

Outside of class from April 30th to May 3rd, I created the final object in the game, the NPC object. Along with the object I created sprites and a basic interaction GUI. My goal for this development is to allow the user to interact with the NPC to progress in the game. The remaining game development tasks are: finish gui-game areas, finalize NPC dialogue, and create an end-game screen.

## April 30th In Class Create Task Progress

During the Apirl 30th class period, I remade the Room Class and finished creating all room-object attributes, connecting all the independent maps together. I also continued to combine the original text-based version of the game with the gui system and identified some more objectives to complete in the upcoming Out of Class Create Task Progress. I also spent some time to plan out further development of NPCs to allow for the player to buy and sell items, a crucial feature for the game.

## April 27th-30th Out of Class Create Task Progress

Outside of class from April 27th to April 30th, I fixed some incorrectly identified teleportation locations, created water tiles, solved several bugs related to the teleporters including null values and relative teleport location, fixed a player-animation loading bug, and fixed a bug that prohibited levels from being unloaded which caused the game to lag and eventually crash. 

## April 27th In Class Create Task Progress

During the April 27th class period, I primarily worked on map values which will become different sections which the player will be able to explore during the course of the game. These files can be found in gui-sys/maps. If you open a map file you will see several lines of characters. Each character corresponds to a specific tile-type in the game, and each line will be represented as row of tiles. The numbered characters 7,8,9, and 0 represent teleport points which will take the player to its destination tile, as specified in the current room's object variable. Together these maps form the entire game which the player will be able to treverse. Once completed, there should also be two buildings the user can go into and two NPCs the user will be able to interact with to further the game.

## Current Development - Pre-April 27th Progress

Currently, the repository is primarily split between the main program in the main directory and the gui system in the gui-sys/ directory. My intention is to merge these programs to allow for the data structures and classes of the main program to be displayed and interacted with through the gui system.
