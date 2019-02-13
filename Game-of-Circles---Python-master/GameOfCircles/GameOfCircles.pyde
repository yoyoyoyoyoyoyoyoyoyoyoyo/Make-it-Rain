import platform
from Bullet import Bullet
from Enemy import Enemy
from Enemy2 import Enemy2
from JiggleBot import Enemy3
from ScreensaverBot import Enemy4
from Player import Player
from SpriteManager import sprites

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 10
    player = Player(height, width, playerTeam)
    
    sprites.append(player)
    sprites.append(Enemy(50, 50, enemyTeam))
    sprites.append(Enemy(60, 60, enemyTeam))
    sprites.append(Enemy(70, 70, enemyTeam))
    sprites.append(Enemy(80, 80, enemyTeam))
    sprites.append(Enemy(90, 90, enemyTeam))
    sprites.append(Enemy(100, 100, enemyTeam))
    sprites.append(Enemy(110, 110, enemyTeam))
    sprites.append(Enemy(120, 120, enemyTeam))
    sprites.append(Enemy(130, 130, enemyTeam))
    sprites.append(Enemy(140, 140, enemyTeam))
    sprites.append(Enemy(150, 150, enemyTeam))
    
    sprites.append(player)
    sprites.append(Enemy2(50, 50, enemyTeam))
    sprites.append(Enemy2(60, 60, enemyTeam))
    sprites.append(Enemy2(70, 70, enemyTeam))
    sprites.append(Enemy2(80, 80, enemyTeam))
    sprites.append(Enemy2(90, 90, enemyTeam))
    sprites.append(Enemy2(100, 100, enemyTeam))
    sprites.append(Enemy2(110, 110, enemyTeam))
    sprites.append(Enemy2(120, 120, enemyTeam))
    sprites.append(Enemy2(130, 130, enemyTeam))
    sprites.append(Enemy2(140, 140, enemyTeam))
    sprites.append(Enemy2(150, 150, enemyTeam))
    
    sprites.append(player)
    sprites.append(Enemy3(50, 50, enemyTeam))
    sprites.append(Enemy3(60, 60, enemyTeam))
    sprites.append(Enemy3(70, 70, enemyTeam))
    sprites.append(Enemy3(80, 80, enemyTeam))
    sprites.append(Enemy3(90, 90, enemyTeam))
    sprites.append(Enemy3(100, 100, enemyTeam))
    sprites.append(Enemy3(110, 110, enemyTeam))
    sprites.append(Enemy3(120, 120, enemyTeam))
    sprites.append(Enemy3(130, 130, enemyTeam))
    sprites.append(Enemy3(140, 140, enemyTeam))
    sprites.append(Enemy3(150, 150, enemyTeam))
    
    sprites.append(player)
    sprites.append(Enemy4(50, 60, enemyTeam))
    sprites.append(Enemy4(60, 70, enemyTeam))
    sprites.append(Enemy4(70, 80, enemyTeam))
    sprites.append(Enemy4(80, 90, enemyTeam))
    sprites.append(Enemy4(90, 100, enemyTeam))
    sprites.append(Enemy4(100, 110, enemyTeam))
    sprites.append(Enemy4(110, 120, enemyTeam))
    sprites.append(Enemy4(120, 130, enemyTeam))
    sprites.append(Enemy4(130, 140, enemyTeam))
    sprites.append(Enemy4(140, 150, enemyTeam))
    sprites.append(Enemy4(150, 160, enemyTeam))
                           
def draw():
    global player, sprites
    background(255)    

    for sprite in sprites:
        sprite.animate()
        
    checkCollisions()
    
def checkCollisions():
    global sprites
    for a in sprites:
        for b in sprites:
            if a.team != b.team:
                d = (pow(a.x - b.x, 2) + pow(a.y - b.y, 2))**(0.5)
                r1 = a.diameter / 2
                r2 = b.diameter / 2
                if(r1 + r2 > d):
                    sprites.remove(a)
                    sprites.remove(b)
    
def keyPressed():
    global player
    player.keyDown()    
        
def keyReleased():
    global player
    player.keyUp()
