#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, WIN_HEIGHT
from code.Entity import Entity


class Obstacle(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self):
        self.rect.centery += ENTITY_SPEED['Obstacle']
        pass
