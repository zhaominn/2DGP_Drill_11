import random

from pico2d import *
import game_framework

import game_world
from game_world import add_collision_pair
from grass import Grass
from boy import Boy
from ball import Ball
from zombie import Zombie

# boy = None

def handle_events():
    global balls
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)

def init():
    global boy

    grass = Grass()
    game_world.add_object(grass, 0)

    boy = Boy()
    game_world.add_object(boy, 1)

    add_collision_pair('zombie:boy', None, boy)

    balls=[Ball(random.randint(100,1500),60,0)for _ in range(30)]
    game_world.add_objects(balls,1) # 게임 월드에 추가,

    # 충돌 대상들을 등록해주기
    add_collision_pair('boy:ball', boy, None)
    for ball in balls:
        add_collision_pair('boy:ball', None, ball)
    # {'boy:ball' : [[boy],[ball1, ball2, ball3, ..., ball30]]}

    #좀비 생성
    zombies = [Zombie() for _ in range(5)]
    game_world.add_objects(zombies,1)
    for zombie in zombies:
        add_collision_pair('zombie:ball', zombie, None)
        add_collision_pair('zombie:boy', zombie, None)

def finish():
    game_world.clear()
    pass


def update():
    game_world.update()
    game_world.handle_collisions()

def draw():
    clear_canvas()
    game_world.render()
    update_canvas()

def pause():
    pass

def resume():
    pass

