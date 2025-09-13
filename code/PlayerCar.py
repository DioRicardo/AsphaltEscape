#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import FACTOR, WIN_WIDTH
from code.Entity import Entity


class PlayerCar(Entity):
    def __init__(self, name: str, position: tuple, speed: int):
        super().__init__(name, position, speed)

    # def __init__(self, name: str, position: tuple):
    #     super().__init__(name, position, speed)

    def move(self, speed=None):
        for event in pygame.event.get(eventtype=pygame.KEYDOWN):
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.rect.left >= 322:
                        self.rect.centerx -= FACTOR
                if event.key == pygame.K_RIGHT:
                    if self.rect.right <= WIN_WIDTH - 262:
                        self.rect.centerx += FACTOR
        pass
