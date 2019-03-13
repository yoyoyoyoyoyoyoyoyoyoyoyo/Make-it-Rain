sprites = []
destroyed = []

playerTeam = 1
enemyTeam = 2

def setPlayer(PlayerInstance):
    global player
    player = PlayerInstance
    spawn(player)
    
def getPlayer():
    global player
    return player

def destroy(target):
    destroyed.append(target)
    
def spawn(obj):
    sprites.append(obj)
    
def animate():
    for sprite in sprites:
        sprite.animate()
    checkCollisions()
    bringOutTheDead()

def checkCollisions():
    for i in range(0, len(sprites)):
        for j in range(i + 1, len(sprites)):
            a = sprites[i]
            b = sprites[j]
            if a.team != b.team and a.isColliding(b):
                sprites[i].handleCollision()
                sprites[j].handleCollision()
                
def bringOutTheDead():
    for sprite in destroyed:
        if sprite in sprites:
            sprites.remove(sprite)
        destroyed.remove(sprite)
