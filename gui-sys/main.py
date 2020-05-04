import pygame as pg
import sys
from os import path
from settings import *
from sprites import *
from map_handler import *
from rooms import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.load_data()

        self.player = ""


    # loads map2.txt level data using os path
    def load_data(self):
        # game_folder is the root location for the game directory
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'source')
        self.map = Map(path.join(game_folder, 'maps/map2.txt'))

        self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()

    def updatePlayerImg(self, img):
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'source')
        if self.player_img != pg.image.load(path.join(img_folder, img)).convert_alpha():
            self.player_img = pg.image.load(path.join(img_folder, img)).convert_alpha()
            #print("Player is now {}".format(img))

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.teleports = pg.sprite.Group()
        self.npcs = pg.sprite.Group()

        self.player = Player(self, 8, 8)

        self.updateMapData(True)

    def updateMapData(self, isNew):
        if not isNew:
            self.all_sprites = pg.sprite.Group()
            self.all_sprites.add(self.player)

            self.npcs = pg.sprite.Group()

            self.walls = pg.sprite.Group()
            self.teleports = pg.sprite.Group()

        for row, tiles in enumerate(self.map.data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    Wall(self, col, row, "bush.png", True, False, None, False)
                if tile == '2':
                    Wall(self, col, row, "gravel_path.png", False, False, None, False)
                if tile == '3':
                    Wall(self, col, row, "water.png", True, False, None, False)

                # available ids

                # Shop Seller
                if tile == 'y':
                    Wall(self, col, row, "shop_npc.png", True, False, None, "shop")
                # Man
                elif tile == 'z':
                    Wall(self, col, row, "man_npc.png", True, False, None, "man")
                elif tile.isalpha():
                    Wall(self, col, row, "house/{}.png".format(tile), True, False, None, False)

                # teleportation tiles

                if tile == '7':
                    Wall(self, col, row, "north.png", False, eval("R" + str(self.player.room)).north, "north", False) # North
                    if self.player.roomMovementDir == "south":
                        self.player.pos.x = col * 64
                        self.player.pos.y = (row + 2) * 64
                if tile == '8':
                    Wall(self, col, row, "south.png", False, eval("R" + str(self.player.room)).south, "south", False) # South
                    if self.player.roomMovementDir == "north":
                        self.player.pos.x = col * 64
                        self.player.pos.y = (row - 1) * 64
                if tile == '9':
                    Wall(self, col, row, "east.png", False, eval("R" + str(self.player.room)).east, "east", False) # East
                    if self.player.roomMovementDir == "west":
                        self.player.pos.x = (col - 1) * 64
                        self.player.pos.y = row * 64
                if tile == '0':
                    Wall(self, col, row, "west.png", False, eval("R" + str(self.player.room)).west, "west", False) # West
                    if self.player.roomMovementDir == "east":
                        self.player.pos.x = (col + 1) * 32
                        self.player.pos.y = row * 64


                # empty tile
                if tile == '.':
                    Wall(self, col, row, "grass.png", False, False, None, False)

        # camera/player tracking system
        self.camera = Camera(self.map.width, self.map.height)


    def run(self):
        # game loop - set self.playing = False to end the game
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()

    def quit(self):
        pg.quit()
        sys.exit()

    def update(self):
        # update portion of the game loop
        self.all_sprites.update()

        # update camera
        self.camera.update(self.player)

        # update animation frame, cycle through 8 animation states
        self.player.animationState = int(self.player.animationFrame/7)
        if self.player.animationState > 6:
            self.player.animationFrame = 0

    def draw(self):
        self.screen.fill(BGCOLOR)

        # dynamic camera/based drawing of sprites including player
        for sprite in self.all_sprites:
            # player
            if sprite.image == self.player.image or sprite in self.npcs:
                pass
            else:
                sprite.image = pg.transform.scale(sprite.image, (64, 64))
                self.screen.blit(sprite.image, self.camera.apply(sprite))

            # NPCs
            if sprite in self.npcs:
                sprite.image = pg.transform.scale(sprite.image, (32, 46))
                self.screen.blit(sprite.image, self.camera.apply(sprite))

        # scale up the player image
        self.player.image = pg.transform.scale(self.player.image, (400, 70))

        if self.player.facing == "down":
            self.screen.blit(self.player.image, self.camera.apply(self.player), (1 + (self.player.animationState * 44), 12, 44, 54))
        else:
            self.screen.blit(self.player.image, self.camera.apply(self.player), (1 + (self.player.animationState * 46), 12, 44, 54))

        self.displayGui()

        self.displayCustomText()

        # update the entire screen
        pg.display.flip()

    def displayGui(self):
        # draw the inventory if open
        if self.player.openInv or not self.player.customDisplayText == "":
            if self.player.openInv:
                text = 'Inventory'
            else:
                text = self.player.customDisplayText
            pg.draw.rect(self.screen, BLACK, (10, 490, WIDTH - 20, 270))
            pg.draw.rect(self.screen, BROWN, (20, 500, WIDTH - 40, 250))

            largeText = pg.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects(text, largeText)
            TextRect.center = ((WIDTH / 2), (HEIGHT / 2) + 140)
            self.screen.blit(TextSurf, TextRect)

    def displayCustomText(self):
        customText = str(self.player.customDisplayText)
        if customText != "":
            pg.draw.rect(self.screen, BLACK, (10, 490, WIDTH - 20, 270))
            pg.draw.rect(self.screen, BROWN, (20, 500, WIDTH - 40, 250))
            pg.draw.rect(self.screen, BROWN, (20, 500, WIDTH - 40, 250))

            largeText = pg.font.Font('freesansbold.ttf', 40)
            TextSurf, TextRect = self.text_objects(customText, largeText)
            TextRect.center = ((WIDTH / 2), (HEIGHT / 2) + 140)
            self.screen.blit(TextSurf, TextRect)

    # handles fonts and texts for pg
    def text_objects(self, text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def changePlayerRoom(self, roomId):
        print("setting player room to {}".format(roomId))
        self.player.room = roomId
        print("South is {}".format(eval("R" + str(self.player.room)).south))

    def events(self):
        # catch all events here
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

# create the game object
g = Game()

# Commands called on start
while True:
    g.new()
    g.run()
