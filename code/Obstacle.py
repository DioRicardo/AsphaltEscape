#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class Obstacle(Entity):

    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position, speed)

    # def __init__(self, name: str, position: tuple, speed):
    #     super().__init__(name, position, speed)
    #     self.speed = ENTITY_SPEED['Obstacle']

    def move(self):
        self.rect.centery += self.speed
        pass
