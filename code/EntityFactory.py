#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from code.Background import Background
from code.Const import WIN_HEIGHT, ENT_INI_POS, OBSTACLE_LIST
from code.Obstacle import Obstacle
from code.PlayerCar import PlayerCar
from code.PoliceCar import PoliceCar


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
            case 'PoliceCar':
                return PoliceCar('PoliceCar', (ENT_INI_POS['PoliceCarX'], ENT_INI_POS['PoliceCarY']))
            case 'Obstacle':
                name = random.randint(0, len(OBSTACLE_LIST) - 1)
                return Obstacle(OBSTACLE_LIST[name], (random.choice((180, 308, 436, 564)), 0 - 300))
