class Player:
    def __init__(self, room, money, inv, interface):
        # room is the id of the user's current room
        self.room = room
        self.money = money
        # array of Strings of items in inventory
        self.inv = inv
        # examples: default or shop
        self.interface = interface

# Tiles are the different rooms and areas
class Tile:
    # General Class Attributes
    type = "room"

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