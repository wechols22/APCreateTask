# Allow Functions to Access Class Data
from classes import *

# Init Player
player = Player(2, 20, ["rock", "rock", "deer", "deer"], "default")

# Init Items
flashlight = Item("flashlight", "A tool that helps you see in dark places, like a forrest", 20)
bear_repellent = Item("bear repellent", "A tool that prevents bears from eating you alive, which is quite useful", 30)
meat = Item("old meat", "It's rotten and smelly, perfect for a Yeti", 50)

# Init Rooms
R1 = Tile("The beginning of the trail", 1, "Here is where you started your treacherous journey: The Hunt for the Yeti",
          0, 2, 0, 0, 0)
R2 = Tile("You are excited to begin your journey and track down the elusive Yeti.", 2,
          "You see a small trail to the north and what looks like a gap in the forest to your east", 3, 7, 0, 1, 0)
R3 = Tile(
    "As you continue down the trail you see a giant footprint to the east, what could that belong to?, you wonder", 3,
    "The small trail continues to the north and the south", 5, 0, 2, 0, 0)
R4 = Tile("You at the west end of a gravel road", 4,
          "The gravel road continues the east, to the north is a old shop that looks open", 14, 5, 0, 0, 0)
R5 = Tile("You are on a gravel road", 5,
          "The gravel road goes to the west and the east, to the north is a yeti statue that you can walk around, and the south will take you back to the small trail",
          15, 6, 3, 4, 0)
R6 = Tile("You are in front of log cabin, a light in on inside of the cabin", 6, "The gravel road continues the west",
          16, 0, 0, 5, 0)
R7 = Tile("You enter a forest through a narrow gap in the trees", 7,
          "The little light makes it this dark in the woods. The forest path continues to the east, or you can head back to the trail by going west",
          0, 8, 0, 2, "flashlight")
R8 = Tile("You are in the middle of a forrest", 8,
          "There is a little creek right next to you. A hill is to your east and there is a small passageway to the north",
          9, 0, 0, 7, 0)
R9 = Tile("You are in the middle of a forrest", 9,
          "You are on the west end of an east-west passageway. There is an opening to the south.", 0, 10, 8, 0, 0)
R10 = Tile("You are in the middle of a forrest", 10, "You are in the middle of an east-west passageway.", 0, 11, 0, 9,
           0)
R11 = Tile("You are in the middle of a forrest", 11,
           "You are on the east of an east-west passageway. There is an opening to the south.", 0, 0, 12, 10, 0)
R12 = Tile("You are in the middle of a forrest", 12,
           "You are standing on top of a hill in a small opening and see a ray of sunlight from the east. You can go to a small passageway to the north or roll down the hill to the west.",
           11, 13, 0, 8, 0)
R13 = Tile("You are in a hidden creek. A sign warns of wildlife that may visit", 13,
           "You can go back to the hill to the west.", 0, 0, 0, 12, 0)
# Idea - make location names bold
R14 = Tile("An Old Souvenir Shop", 14, "There is a shop teller. Perhaps you should ask 'what's for sale?'", 0, 0, 4, 0,
           0)
R15 = Tile("You are at the base of a large statue of a Yeti", 15,
           "You can walk around the statue to the north or to the south.", 17, 0, 5, 0, 0)
R16 = Tile("There is an older man. Perhaps you should say 'hello'?", 16, "You can leave the house to the south.", 0, 0,
           6, 0, 0)


# Development Testing Commands

# Access the instance attributes from array
def displayClassTable(name, attribute, obj):
    value = getattr(obj, attribute)
    print("{}  | {} \n---------- \n{}| {} \n".format(
        name, attribute, obj.name, value))


def moveDirection(direction):
    moveToRoomExists = True
    # retreive attributes of current player room
    toRoom = eval("R" + str(player.room))
    # find the relative room id based on player room object
    toRoom = getattr(toRoom, direction)

    # if room exists (id is not 0), send player to room
    if toRoom != 0:
        # if there is no room requirement or the player has the required item, move the player to the room

        # determine the object to the new room
        toRoomObj = eval("R" + str(toRoom))

        if toRoomObj.requirement == 0 or toRoomObj.requirement in player.inv:
            goToRoom(toRoom)
        else:
            # if the user does not have the required item
            print("You will need a {} to go farther that way".format(toRoomObj.requirement))
    else:
        moveToRoomExists = False

    # if the room does not exist display an error
    if moveToRoomExists == False:
        print("There is no area to go to in that direction")


# sends the player to a room and displays the room name as well as room description
def goToRoom(roomId):
    player.room = roomId
    room = eval("R" + str(roomId))
    cls()
    print("{}".format(room.name))
    print(room.desc)


# displays an array (use case: user inv)
def displayArray(array_name, array):
    print("{}\n---------\n".format(array_name))
    print(*array, sep='\n')
    # if array is inventory, display empty
    if array == []:
        print("empty")


# allows the user to buy different items through specific commands
def shopCommand(command):
    if (command == "start"):
        # determine if player has already bought something before stating options
        if ("flashlight" in player.inv and "bear repellent" in player.inv and "old meat" in player.inv):
            print(
                "Hey there, you already bought all I have to offer, but thanks for stopping buy. I guess you have to 'stop' shopping now.")
        else:
            print(
                "Hey there, you can buy a flashlight for $20, bear repellent for $30, or some old meat for $50. Once your done shopping, feel free to tell me to 'stop'")
    elif ("buy" in command):
        buyFromShop(command)
    elif (command == "inv" or command == "inventory"):
        displayArray("Inventory - ${}".format(player.money), player.inv)
    elif (command == "stop"):
        print("Okay, make sure to stop by again soon")
        player.interface = "default"
    else:
        print("Come again? I couldn't understand you")


# allows the user to buy something from the shop if they have not already bought it and they have enough money
ItemsForSale = [flashlight, bear_repellent, meat]


def buyFromShop(command):
    for item in ItemsForSale:
        if (item.name in command):
            if (item.name not in player.inv):
                if (player.money >= item.price):
                    player.money -= item.price
                    player.inv.append(item.name)
                    print("Thanks for the business.")
                else:
                    print("Sorry pal, {} is ${} and you only have ${}".format(item.name, item.price, player.money))
            else:
                print("Silly fellow, you already have {}".format(item.name))


# allows the user to talk to the man in his house
def talkToMan(command):
    if (command == "start"):
        print(
            "Hello there! I am Bob. Are you here to see the Yeti? He's quite a site, but I supposed you probably need some money to buy equipment. If you come buy with some square rocks or deer, I'd buy them off of you. Just say 'I've got something'. Oh, and if I'm rumbling on for too long just tell me to 'stop'")
    elif (command == "I've got something"):
        # Check for rocks and deer
        numRocks = 0
        numDeer = 0
        for i in player.inv:
            if (i == "rock"):
                numRocks += 1
            elif (i == "deer"):
                numDeer += 1

        moneyForPlayer = (10 * numDeer) + (2 * numRocks)

        # npc interaction
        if (numRocks != 0):
            if (numDeer != 0):
                # both
                print("Wow! You have {} rocks and {} deer! I'll take them from you and give you ${}".format(numRocks,
                                                                                                            numDeer,
                                                                                                            moneyForPlayer))
            else:
                # just rocks
                print("You have {} rocks.".format(numRocks))
        elif (numDeer != 0):
            # just deer
            print("You have {} deer.".format(numDeer))
        else:
            print(
                "Well, it doesn't look like you have anything that I would buy from you. You should try looking for rocks or deer")
            # nothing to sell

        # take items from player and give money
        for num in player.inv:
            player.inv.remove("rock")
            player.inv.remove("deer")
        player.money += moneyForPlayer


    elif (command == "stop"):
        print("Okay then, see you later")
        player.interface = "default"


# prints a lot of next lines to clear screen
def cls(): print("\n" * 100)