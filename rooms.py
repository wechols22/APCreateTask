# Tiles are the different rooms and areas
class Tile:
    # Initializer
    def __init__(self, id, north, east, south, west):
        self.north = north
        self.east = east
        self.south = south
        self.west = west

# Init Rooms
R1 = Tile(1, 0, 2, 0, 0)
R2 = Tile(2, 3, 7, 0, 1)
R3 = Tile(3, 5, 0, 2, 0)
R4 = Tile(4, 14, 5, 0, 0)
R5 = Tile(5, 15, 6, 3, 4)
R6 = Tile(6, 16, 0, 0, 5)
R7 = Tile(7, 0, 8, 0, 2)
R8 = Tile(8, 9, 0, 0, 7)
R9 = Tile(9, 0, 10, 8, 0)
R10 = Tile(10, 0, 11, 0, 9)
R11 = Tile(11, 0, 0, 12, 10)
