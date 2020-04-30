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
