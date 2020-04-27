import pygame as pg
from settings import *
from map_handler import *
from os import path

vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img

        self.animationFrame = 0
        self.animationState = 0
        self.facing = "up"

        self.rect = self.image.get_rect()

        self.rect.width = 45 # Note - manual width adjustment for collision
        self.rect.height = 50

        self.vel = vec(0, 0)
        self.pos = vec(x, y) * TILESIZE
        self.openInv = False # determines whether or not the players inventory should be displayed
        self.canOpenInv = True
        self.customDisplayText = ""
        self.room = 2

    # handles player input and manages inventory display
    def player_input(self):
        self.vel = vec(0, 0)
        keys = pg.key.get_pressed()

        if not self.openInv:
            if keys[pg.K_LEFT] or keys[pg.K_a]:
                self.vel.x = -PLAYER_SPEED
                self.changePlayerImg('player/left/left.png')
                self.facing = "left"
            elif keys[pg.K_RIGHT] or keys[pg.K_d]:
                self.vel.x = PLAYER_SPEED
                self.changePlayerImg('player/right/right.png')
                self.facing = "right"
            elif keys[pg.K_UP] or keys[pg.K_w]:
                self.vel.y = -PLAYER_SPEED
                self.changePlayerImg('player/up/up.png')
                self.facing = "up"
            elif keys[pg.K_DOWN] or keys[pg.K_s]:
                self.vel.y = PLAYER_SPEED
                self.changePlayerImg('player/down/down.png')
                self.facing = "down"
            if keys[pg.K_e]:
                if self.canOpenInv:
                    self.openInv = not self.openInv
                    self.canOpenInv = False
            else:
                self.canOpenInv = True
        elif keys[pg.K_e]:
            if self.canOpenInv:
                self.openInv = False
                self.canOpenInv = False
        else:
            self.canOpenInv = True

        if keys[pg.K_e]:
            if self.customDisplayText != "":
                self.customDisplayText = ""

    # Note: this has not been tested

    # IDEA - when the player tps to a new room there location should be relative to the location to tp back, for istance if going north, then location should be south pad -1y

    def setPlayerLocation(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def changePlayerImg(self, img):
        self.game.updatePlayerImg(img)
        self.image = self.game.player_img

        # Since this function is run while the player is in motion, the animation frames are only counted through this function
        self.animationFrame += 1

    # prevents the player from walking through a wall
    def checkForWallCollision(self, dir):
        # wall collision testing
        if dir == 'x':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.x > 0:
                    self.pos.x = hits[0].rect.left - self.rect.width
                else:
                    self.pos.x = hits[0].rect.right
                self.vel.x = 0
                self.rect.x = self.pos.x

            teleHits = pg.sprite.spritecollide(self, self.game.teleports, False)
            if teleHits:
                print("I just hit a teleporter")

                game_folder = path.dirname(__file__)
                img_folder = path.join(game_folder, 'source')
                self.game.map = Map(path.join(game_folder, 'maps/map{}.txt'.format(teleHits[0].teleport)))



                # for some reason it does not want to update and display properly on the Main class
                # Current explanation - Two player objects have been created and are apparently "competeting" for methods which is causing consistency errors
                #self.customDisplayText = "test"

                print("teleporting to maps/map{}.txt".format(teleHits[0].teleport))

                # retreive current room's location for the new room



                # update player room data
                self.room = teleHits[0].teleport
                self.game.changePlayerRoom(teleHits[0].teleport)


                # load changes
                self.game.updateMapData(False)


        if dir == 'y':
            hits = pg.sprite.spritecollide(self, self.game.walls, False)
            if hits:
                if self.vel.y > 0:
                    self.pos.y = hits[0].rect.top - self.rect.height
                else:
                    self.pos.y = hits[0].rect.bottom
                self.vel.y = 0
                self.rect.y = self.pos.y


    def update(self): # handles player input and movement
        self.player_input()

        self.pos += self.vel * self.game.dt

        self.rect.x = self.pos.x
        self.checkForWallCollision('x')
        self.rect.y = self.pos.y
        self.checkForWallCollision('y')


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, img, collide, teleport):
        self.groups = game.all_sprites
        self.teleport = teleport


        #if collide:
        #    if not teleport == False:
        #        self.groups = game.all_sprites, game.walls, game.teleports
        #    else:
        #        self.groups = game.all_sprites, game.walls
        #else:
        #    if not teleport == False:
        #        self.groups = game.all_sprites, game.teleports

        if not self.teleport:
            if collide:
                self.groups = game.all_sprites, game.walls
        else:
            self.groups = game.all_sprites, game.teleports

        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game

        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, 'source')
        self.image = pg.image.load(path.join(img_folder, img)).convert_alpha()

        #self.image = pg.Surface((TILESIZE, TILESIZE))
        #self.image.fill(color)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

