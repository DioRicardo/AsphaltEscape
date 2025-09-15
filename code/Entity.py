#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

import pygame.image

from code.Const import ENTITY_HEALTH, ENTITY_SPEED


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load(f'./asset/' + name + '.png').convert_alpha()
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.base_speed = ENTITY_SPEED
        self.speed = self.base_speed
        self.health = ENTITY_HEALTH[self.name]
        self.score = 0

    @abstractmethod
    def move(self):
        pass
