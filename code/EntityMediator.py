#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Const import WIN_HEIGHT, SPEED_REDUCTION, FACTOR, WIN_WIDTH, ENT_INI_POS
from code.Entity import Entity
from code.Obstacle import Obstacle
from code.PlayerCar import PlayerCar
from code.PoliceCar import PoliceCar


class EntityMediator:

    @staticmethod
    def __verify_collision_window(ent: Entity):
        if isinstance(ent, Obstacle):
            if ent.rect.top > WIN_HEIGHT:
                ent.health = 0
        pass

    @staticmethod
    def __verify_collision_entity(ent1: Entity, ent2: Entity):
        valid_interaction = False
        if isinstance(ent1, Obstacle) and isinstance(ent2, PlayerCar):
            valid_interaction = True
        elif isinstance(ent1, PlayerCar) and isinstance(ent2, Obstacle):
            valid_interaction = True

        if valid_interaction:
            if (ent1.rect.right >= ent2.rect.left and
                    ent1.rect.left <= ent2.rect.right and
                    ent1.rect.bottom >= ent2.rect.top and
                    ent1.rect.top <= ent2.rect.bottom):
                return SPEED_REDUCTION
            return 0

    @staticmethod
    def verify_collision(entity_list: list[Entity]):
        for i in range(len(entity_list)):
            entity1 = entity_list[i]
            EntityMediator.__verify_collision_window(entity1)
            for j in range(i + 1, len(entity_list)):
                entity2 = entity_list[j]
                result = EntityMediator.__verify_collision_entity(entity1, entity2)
                if result:
                    return result
        return 0

    @staticmethod
    def verify_health(entity_list: list[Entity]):
        for ent in entity_list:
            if ent.health <= 0:
                entity_list.remove(ent)

    @staticmethod
    def change_lanes(entity_list: list[Entity]):
        for ent in entity_list:
            if isinstance(ent, PlayerCar):
                lane = random.choice(['left', 'right'])
                if lane == 'left':
                    if ent.rect.left >= 322:
                        ent.rect.centerx -= FACTOR
                elif lane == 'right':
                    if ent.rect.right <= WIN_WIDTH - 262:
                        ent.rect.centerx += FACTOR

    @staticmethod
    def move_police(entity_list: list[Entity], game_speed):
        player_car = None
        police_car = None
        for ent in entity_list:
            if isinstance(ent, PlayerCar):
                player_car = ent
            if isinstance(ent, PoliceCar):
                police_car = ent
        police_car.rect.centerx = player_car.rect.centerx

        if game_speed > 5:
            police_car.closing_in()
        elif game_speed <= 5:
            police_car.dropping_back(player_car)

