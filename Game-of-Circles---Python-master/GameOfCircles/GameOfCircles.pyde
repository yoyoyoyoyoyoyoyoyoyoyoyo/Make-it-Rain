import platform
from Bullet import Bullet
from Enemy import Enemy
from Enemy2 import Enemy2
from JiggleBot import Enemy3
from ScreensaverBot import Enemy4
from Player import Player

import SpriteManager 

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 10
    player = Player(height, width, playerTeam)    
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(Enemy(50, 50, enemyTeam))
    SpriteManager.spawn(Enemy(60, 60, enemyTeam))
    SpriteManager.spawn(Enemy(70, 70, enemyTeam))
    SpriteManager.spawn(Enemy(80, 80, enemyTeam))
    SpriteManager.spawn(Enemy(90, 90, enemyTeam))
    SpriteManager.spawn(Enemy(100, 100, enemyTeam))
    SpriteManager.spawn(Enemy(110, 110, enemyTeam))
    SpriteManager.spawn(Enemy(120, 120, enemyTeam))
    SpriteManager.spawn(Enemy(130, 130, enemyTeam))
    SpriteManager.spawn(Enemy(140, 140, enemyTeam))
    SpriteManager.spawn(Enemy(150, 150, enemyTeam))
    
    SpriteManager.spawn(player)
    SpriteManager.spawn(Enemy2(50, 50, enemyTeam))
    SpriteManager.spawn(Enemy2(60, 60, enemyTeam))
    SpriteManager.spawn(Enemy2(70, 70, enemyTeam))
    SpriteManager.spawn(Enemy2(80, 80, enemyTeam))
    SpriteManager.spawn(Enemy2(90, 90, enemyTeam))
    SpriteManager.spawn(Enemy2(100, 100, enemyTeam))
    SpriteManager.spawn(Enemy2(110, 110, enemyTeam))
    SpriteManager.spawn(Enemy2(120, 120, enemyTeam))
    SpriteManager.spawn(Enemy2(130, 130, enemyTeam))
    SpriteManager.spawn(Enemy2(140, 140, enemyTeam))
    SpriteManager.spawn(Enemy2(150, 150, enemyTeam))
    
    SpriteManager.spawn(player)
    SpriteManager.spawn(Enemy3(50, 50, enemyTeam))
    SpriteManager.spawn(Enemy3(60, 60, enemyTeam))
    SpriteManager.spawn(Enemy3(70, 70, enemyTeam))
    SpriteManager.spawn(Enemy3(80, 80, enemyTeam))
    SpriteManager.spawn(Enemy3(90, 90, enemyTeam))
    SpriteManager.spawn(Enemy3(100, 100, enemyTeam))
    SpriteManager.spawn(Enemy3(110, 110, enemyTeam))
    SpriteManager.spawn(Enemy3(120, 120, enemyTeam))
    SpriteManager.spawn(Enemy3(130, 130, enemyTeam))
    SpriteManager.spawn(Enemy3(140, 140, enemyTeam))
    SpriteManager.spawn(Enemy3(150, 150, enemyTeam))
    
    SpriteManager.spawn(player)
    SpriteManager.spawn(Enemy4(50, 60, enemyTeam))
    SpriteManager.spawn(Enemy4(60, 70, enemyTeam))
    SpriteManager.spawn(Enemy4(70, 80, enemyTeam))
    SpriteManager.spawn(Enemy4(80, 90, enemyTeam))
    SpriteManager.spawn(Enemy4(90, 100, enemyTeam))
    SpriteManager.spawn(Enemy4(100, 110, enemyTeam))
    SpriteManager.spawn(Enemy4(110, 120, enemyTeam))
    SpriteManager.spawn(Enemy4(120, 130, enemyTeam))
    SpriteManager.spawn(Enemy4(130, 140, enemyTeam))
    SpriteManager.spawn(Enemy4(140, 150, enemyTeam))
    SpriteManager.spawn(Enemy4(150, 160, enemyTeam))
                           
def draw():
    background(255)    
    SpriteManager.animate()
    
def keyPressed():
    SpriteManager.player.keyDown()
        
def keyReleased():
    SpriteManager.player.keyUp()
