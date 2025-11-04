from pico2d import *
import random

from boy import Boy
from grass import Grass
from bird import Bird

import game_world

import game_framework


boy = None

def handle_events():
    global running

    event_list = get_events()
    for event in event_list:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy
    global running

    running = True
    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    for bird in range(10):
        rand_x = random.randint(25,1575)
        rand_y = random.randint(450, 550)
        rand_dir = random.randint(0, 1)
        if rand_dir == 0:
            rand_dir = -1
        bird = Bird(rand_x, rand_y, rand_dir)
        game_world.add_object(bird, 1)

def update():
    game_world.update()
    # 후진 pc 흉내
    #delay(0.2)

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def finish():
    game_world.clear()

def pause(): pass
def resume(): pass

