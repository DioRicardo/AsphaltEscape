#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import WIN_HEIGHT, ENTITY_SPEED
from code.Entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position, speed)

    # def __init__(self, name: str, position: tuple, speed):
    #     super().__init__(name, position, speed)
    #     self.speed = ENTITY_SPEED[self.name]

    def move(self):
        self.rect.centery += self.speed
        if self.rect.top >= WIN_HEIGHT:
            self.rect.bottom = 0
        pass
