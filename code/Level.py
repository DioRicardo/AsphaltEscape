#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.display

from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))

    def run(self):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.set_volume(0.0)
        pygame.mixer_music.play(-1)
        print(len(self.entity_list))
        while True:

            for ent in self.entity_list:

                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        

        pass
