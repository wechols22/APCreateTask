# Tiles are the different rooms and areas
class Tile:
    # Initializer
    def __init__(self, name, id, north, east, south, west):
        self.name = name
        self.id = id
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# Init Rooms
R1 = Tile("Gravel Path", 1, 0, 2, 0, 0)
R2 = Tile("Gravel Path", 2, 3, 7, 0, 1)
R3 = Tile("Gravel Path", 3, 5, 0, 2, 0)
R4 = Tile("Gravel Path", 4, 14, 5, 0, 0)
R5 = Tile("Gravel Path", 5, 15, 6, 3, 4)
R6 = Tile("Gravel Path", 6, 16, 0, 0, 5)
R7 = Tile("Forest", 7, 0, 8, 0, 2)
R8 = Tile("Forest", 8, 9, 0, 0, 7)
R9 = Tile("Forest", 9, 0, 10, 8, 0)
R10 = Tile("Forest", 10, 0, 11, 0, 9)
R11 = Tile("An Old Souvenir Shop", 11, 0, 0, 12, 10)
