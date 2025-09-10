# C
import pygame

CAR_OPTION = ('RED CAR',
              'YELLOW CAR')

C_WHITE = (255, 255, 255)
C_YELLOW = (255, 212, 71)
C_GRAY = (176, 176, 176)
C_RED = (230, 57, 70)
C_BLACK = (0, 0, 0)

# E

ENTITY_SPEED = {
    'LevelBg': 5,
    'Obstacle': 5,
}

EVENT_OBSTACLE = pygame.USEREVENT + 1

# M

MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# O

OBSTACLE_LIST = ['Obstacle1', 'Obstacle2', 'Obstacle3', 'Obstacle4', 'Obstacle5']

# W

WIN_WIDTH = 840
WIN_HEIGHT = 980

# E (AFTER W TO USE THE CONSTS)

ENT_INI_POS = {
    'PlayerCarX': (WIN_WIDTH / 2) + 30,
    'PlayerCarY': WIN_HEIGHT - 350
}

# FATOR DE MUDANÇA DE FAIXA DO PLAYER CAR

FACTOR = 128
