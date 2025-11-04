from pico2d import *
import game_world
import game_framework

class Bird:
    image = None
    def __init__(self, x, y, dir):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.dir = x, y, dir
    def draw(self):
        self.image.draw(self.x, self.y)
        pass

    def update(self):
        pass