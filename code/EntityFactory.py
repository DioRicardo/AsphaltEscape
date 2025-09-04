#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_HEIGHT, ENT_INI_POS, OBSTACLE_LIST, WIN_WIDTH
from code.Obstacle import Obstacle
from code.PlayerCar import PlayerCar


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'LevelBg':
                level_bg = [Background(f'LevelBg', (0, 0)),
                            Background(f'LevelBg', (0, (0 - WIN_HEIGHT)))]
                return level_bg
            case 'PlayerCar':
                return PlayerCar('PlayerCar', (ENT_INI_POS['PlayerCarX'], ENT_INI_POS['PlayerCarY']))
            case 'Obstacle':
                return Obstacle('Obstacle1', (WIN_HEIGHT / 2, WIN_WIDTH / 2))
                # name = random.randint(0, len(OBSTACLE_LIST))
                # return Obstacle(OBSTACLE_LIST[name], (random.choice((194, 322, 450, 578)), 0))
