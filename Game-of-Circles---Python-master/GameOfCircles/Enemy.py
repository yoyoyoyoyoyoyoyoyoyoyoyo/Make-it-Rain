from Sprite import Sprite

class Enemy(sprite):
    
    speed = 8
    diameter = 50
    c = color(255,200,200)
    
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
            
