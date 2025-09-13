#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame.display
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import C_BLACK, WIN_HEIGHT, WIN_WIDTH, EVENT_OBSTACLE, ENTITY_SPEED
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator


class Level:
    def __init__(self, window, name):
        pygame.event.clear()
        self.window = window
        self.name = name
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('LevelBg'))
        self.entity_list.append(EntityFactory.get_entity('PlayerCar'))
        pygame.time.set_timer(EVENT_OBSTACLE, 600)

        self.baseline_speed = float(ENTITY_SPEED)
        self.game_speed = float(self.baseline_speed)
        self.game_speed_max = float(self.baseline_speed * 2.0)
        self.speed_accel = 0.5
        self.collision_cooldown_ms = 0
        pygame.time.set_timer(EVENT_OBSTACLE, 600)

    def run(self):
        pygame.mixer_music.load('./asset/Level.wav')
        pygame.mixer_music.set_volume(0.03)
        pygame.mixer_music.play(-1)
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()

        while True:

            dt = clock.tick(120)

            if self.collision_cooldown_ms > 0:
                self.collision_cooldown_ms -= dt
                if self.collision_cooldown_ms <= 0:
                    self.game_speed = max(self.baseline_speed * 0.5, self.game_speed)
            else:
                self.game_speed = min(self.game_speed + self.speed_accel * (dt / 1000.0), self.game_speed_max)

            for ent in self.entity_list:
                if hasattr(ent, 'base_speed') and ent.base_speed > 0:
                    ent.speed = self.game_speed
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            elapsed_time = pygame.time.get_ticks() - start_time

            self.level_text(20, f'{self.name} - TIME ELAPSED: {elapsed_time / 1000:.1f}s', C_BLACK, (160, 35))
            self.level_text(20, f'Cooldown Collision: {self.collision_cooldown_ms}', C_BLACK, (WIN_WIDTH - 160, 35))
            self.level_text(20, f'Game Speed: {self.game_speed:.2f}', C_BLACK, (WIN_WIDTH - 160, 75))
            self.level_text(20, f'Entidades: {len(self.entity_list)}', C_BLACK, (100, WIN_HEIGHT - 35))

            pygame.display.flip()

            for event in pygame.event.get(eventtype=[pygame.QUIT, EVENT_OBSTACLE]):
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == EVENT_OBSTACLE:
                    obs = EntityFactory.get_entity('Obstacle')
                    if hasattr(obs, 'speed'):
                        obs.speed = self.game_speed
                    self.entity_list.append(obs)

            # Collisions
            collision_result = EntityMediator.verify_collision(entity_list=self.entity_list)
            if collision_result:
                self.collision_cooldown_ms = 600
                self.game_speed = 0
                # self.game_speed = -0.5
                # self.game_speed = 5
                EntityMediator.change_lanes(entity_list=self.entity_list)

            EntityMediator.verify_health(entity_list=self.entity_list)
            pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Stencil", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
