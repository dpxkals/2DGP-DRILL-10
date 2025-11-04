from pico2d import *
import game_world
import game_framework

PIXEL_PER_METER = (10.0 / 0.1)  # 10 pixel 10 cm
RUN_SPEED_KMPH = 40.0 # Km / Hour 새의 평균 비행 속도 40 km/h
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.2 # 비둘기를 기준으로 약 0.2초라 함
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14
FRAMES_PER_SECOND = FRAMES_PER_ACTION * ACTION_PER_TIME

class Bird:
    image = None
    def __init__(self, x, y, dir):
        if Bird.image == None:
            Bird.image = load_image('bird_animation.png')
        self.x, self.y, self.dir = x, y, dir
        self.frame = 0
    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(int(self.frame)* 184, 338, 184, 169, self.x, self.y)
        else :
            self.image.clip_composite_draw(int(self.frame)* 184, 338, 184, 169, 0, 'v', self.x, self.y)
        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_SECOND * game_framework.frame_time) % 14