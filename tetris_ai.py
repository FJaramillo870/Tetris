import pygame
import random
import time

class Event():
    type = None
    key = None

    def __init__(self, type, key):
        self.type = type
        self.key = key

counter = 0

def run_ai():
    global counter
    counter += 1
    if counter < 3:
        return []
    counter = 0
    movement = movement1()
    if movement == 0:
        e = Event(pygame.KEYDOWN, pygame.K_w)
    elif movement == 1:
        e = Event(pygame.KEYDOWN, pygame.K_d)
    elif movement == 2:
        e = Event(pygame.KEYDOWN, pygame.K_a)
    else:
        e = Event(pygame.KEYDOWN, pygame.K_s)
    return [e]

def movement1():
    randmovement = random.randint(0,2)
    time.sleep(0.5)
    return randmovement