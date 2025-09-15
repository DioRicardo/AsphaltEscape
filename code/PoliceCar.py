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
        self.siren_volume = float(0.5)

    def move(self):
        pass

    def dropping_back(self):
        volume = float(1.0)
        if self.rect.top <= WIN_HEIGHT + 10:
            self.rect.centery += 1
            self.siren_volume -= 0.004
        pygame.mixer.Sound.set_volume(self.sound, self.siren_volume)

    def closing_in(self, player_car):
        if self.rect.top > player_car.rect.bottom + 30:
            self.rect.centery -= 0.6
            self.siren_volume += 0.004
        pygame.mixer.Sound.set_volume(self.sound, self.siren_volume)
