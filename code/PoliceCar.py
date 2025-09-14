#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_HEIGHT
from code.Entity import Entity


class PoliceCar(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.sound = pygame.mixer.Sound('./asset/PoliceSound.wav')
        pygame.mixer.Sound.play(self.sound, loops=-1)

    def move(self):
        pass

    def closing_in(self):
        if self.rect.top <= WIN_HEIGHT + 10:
            self.rect.centery += 1

    def dropping_back(self, player_car):
        if self.rect.top > player_car.rect.bottom + 30:
            self.rect.centery -= 0.6
