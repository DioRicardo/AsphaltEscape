#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, WIN_HEIGHT, WIN_WIDTH, EVENT_OBSTACLE
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name):
        pygame.event.clear()
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('PlayerCar'))
        pygame.time.set_timer(EVENT_OBSTACLE, 600)

    def run(self):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.set_volume(0.03)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        while True:

            clock.tick(120)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                # if isinstance(ent, Background):  Implementar aumento da velocidade do background com o tempo sem bater
                #   ent.move(Speed)
                ent.move()

            elapsed_time = pygame.time.get_ticks() - start_time

            self.level_text(20, f'{self.name} - TIME ELAPSED: {elapsed_time / 1000:.1f}s', C_BLACK, (160, 35))
            self.level_text(20, f'fps: {clock.get_fps():.0f}', C_BLACK, (WIN_WIDTH - 60, 35))
            self.level_text(20, f'Entidades: {len(self.entity_list)}', C_BLACK, (100, WIN_HEIGHT - 35))

            pygame.display.flip()

            for event in pygame.event.get(eventtype=[pygame.QUIT, EVENT_OBSTACLE]):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_OBSTACLE:
                    self.entity_list.append(EntityFactory.get_entity('Obstacle'))

            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Stencil", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
