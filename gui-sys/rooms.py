# Tiles are the different rooms and areas
class Tile:
    # Initializer
    def __init__(self, name, id, north, east, south, west, requirement):
        self.name = name
        self.id = id
        self.north = north
        self.east = east
        self.south = south
        self.west = west

        self.requirement = requirement

class Item:
    def __init__(self, name, desc, price):
        self.name = name
        self.desc = desc
        self.price = price

# Init Items
flashlight = Item("flashlight", "A tool that helps you see in dark places, like a forrest", 20)
bear_repellent = Item("bear repellent", "A tool that prevents bears from eating you alive, which is quite useful", 30)
meat = Item("old meat", "It's rotten and smelly, perfect for a Yeti", 50)

# Init Rooms
R1 = Tile("Gravel Path", 1, 0, 2, 0, 0, 0)
R2 = Tile("Gravel Path", 2, 3, 7, 0, 1, 0)
R3 = Tile("Gravel Path", 3, 5, 0, 2, 0, 0)
R4 = Tile("Gravel Path", 4, 14, 5, 0, 0, 0)
R5 = Tile("Gravel Path", 5, 15, 6, 3, 4, 0)
R6 = Tile("Gravel Path", 6, 16, 0, 0, 5, 0)
R7 = Tile("Forest", 7, 0, 8, 0, 2, "flashlight")
R8 = Tile("Forest", 8, 9, 0, 0, 7, 0)
R9 = Tile("Forest", 9, 0, 10, 8, 0, 0)
R10 = Tile("Forest", 10, 0, 11, 0, 9, 0)
R11 = Tile("Forest", 11, 0, 0, 12, 10, 0)
R12 = Tile("Forest", 12, 11, 13, 0, 8, 0)
R13 = Tile("Forest", 13, 0, 0, 0, 12, 0)
# Idea - make location names bold
R14 = Tile("An Old Souvenir Shop", 14, 0, 0, 4, 0, 0)
R15 = Tile("Yeti Statue", 15, 17, 0, 5, 0, 0)
R16 = Tile("Inside the House", 16, 0, 0, 6, 0, 0)
R17 = Tile("Beginning of the Hiking Trail", 17, 18, 0, 15, 0, "old meat")
R18 = Tile("Hiking Trail", 18, 19, 0, 17, 0, "flashlight")
R19 = Tile("Hiking Trail", 19, 0, 20, 18, 0, 0)
R20 = Tile("Hiking Trail", 20, 21, 0, 0, 19, "bear repellent")
R21 = Tile("Hiking Trail", 21, 0, 0, 20, 22, 0)
R22 = Tile("Hiking Trail", 22, 23, 21, 0, 0, 0) # bear here
R23 = Tile("The Yeti's Den", 23, 0, 0, 0, 0, 0)

