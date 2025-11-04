from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 20.0 # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Bird:
    image = None
    def __init__(self, x, y, dir):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.dir = x, y, dir
    def draw(self):
        self.image.clip_composite_draw(self.x, self.y)
        pass

    def update(self):
        pass