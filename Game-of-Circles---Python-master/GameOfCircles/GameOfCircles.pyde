import platform
import SpriteManager
from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Drops import Drop
from JiggleBot import Jiggle
from ScreensaverBot import Saver
from Shooter import Shooter

def setup():
    print "Built with Processing Python version " + platform.python_version()
    size(500, 500)

    SpriteManager.setPlayer(Player(width/2, height - 100, 1))
    SpriteManager.spawn(Enemy(200, 70, 2))
    SpriteManager.spawn(Enemy(200, 50, 2))
    SpriteManager.spawn(Enemy(200, 30, 2))

                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
