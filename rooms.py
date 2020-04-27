# Tiles are the different rooms and areas
class Tile:
    # Initializer
    def __init__(self, name, id, desc, north, east, south, west, requirement):
        self.name = name
        self.id = id
        self.desc = desc
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
R1 = Tile("The beginning of the trail", 1, "Here is where you started your treacherous journey: The Hunt for the Yeti",
          0, 2, 0, 0, 0)
R2 = Tile("You are excited to begin your journey and track down the elusive Yeti.", 2,
          "You see a small trail to the north and what looks like a gap in the forest to your east", 3, 7, 0, 1, 0)
R3 = Tile("As you continue down the trail you see a giant footprint to the east, what could that belong to?, you wonder", 3,
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