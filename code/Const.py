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

ENTITY_SPEED = 5

ENTITY_HEALTH = {
    'LevelBg': 999,
    'Obstacle1': 300,
    'Obstacle2': 300,
    'Obstacle3': 300,
    'Obstacle4': 300,
    'Obstacle5': 300,
    'PlayerCar': 999,
    'PoliceCar': 999,
}

EVENT_OBSTACLE = pygame.USEREVENT + 1

# F

FACTOR = 128  # FATOR DE MUDANÇA DE FAIXA DO PLAYER CAR

# M

MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# O

OBSTACLE_LIST = ['Obstacle1', 'Obstacle2', 'Obstacle3', 'Obstacle4', 'Obstacle5']

# s

SPEED_REDUCTION = 5

# W

WIN_WIDTH = 840
WIN_HEIGHT = 980

# E (AFTER W TO USE THE CONSTS)

ENT_INI_POS = {
    'PlayerCarX': (WIN_WIDTH / 2) + 30,
    'PlayerCarY': WIN_HEIGHT - 350,
    'PoliceCarX': (WIN_WIDTH / 2) + 30,
    'PoliceCarY': WIN_HEIGHT - 150
}

# S (AFTER W TO USE THE CONSTS)

SCORE_POS = {
    'Title': (WIN_WIDTH / 2, 250),
    'EnterName': (WIN_WIDTH / 2, 280),
    'Label': (WIN_WIDTH / 2, 290),
    'Name': (WIN_WIDTH / 2, 310),
    0: (WIN_WIDTH / 2, 330),
    1: (WIN_WIDTH / 2, 350),
    2: (WIN_WIDTH / 2, 370),
    3: (WIN_WIDTH / 2, 390),
    4: (WIN_WIDTH / 2, 410),
    5: (WIN_WIDTH / 2, 430),
    6: (WIN_WIDTH / 2, 450),
    7: (WIN_WIDTH / 2, 470),
    8: (WIN_WIDTH / 2, 490),
    9: (WIN_WIDTH / 2, 510),
}
