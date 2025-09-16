from datetime import datetime

import pygame
from pygame import Surface, Rect, KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font

from code.Const import C_BLACK, WIN_WIDTH, C_YELLOW, WIN_HEIGHT, SCORE_POS, C_WHITE
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, player_score):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.set_volume(1)
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''

        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # Game Title
            self.score_text(80, "ASPHALT ESCAPE", C_BLACK, (WIN_WIDTH / 2, 80))
            self.score_text(80, "ASPHALT ESCAPE", C_YELLOW, ((WIN_WIDTH / 2) + 5, 80))

            # Score
            self.score_text(25, "Congratulations!!", C_YELLOW, SCORE_POS['Title'])
            text = f'{player_score}pts - Insert your name: (4 characters)'
            self.score_text(25, text, C_WHITE, SCORE_POS['EnterName'])

            # Copyright
            self.score_text(20, "© Copyright 2025 - Aluno: Dio Ricardo Ferreira Vieira - RU: 4751823", C_BLACK,
                            ((WIN_WIDTH / 2), WIN_HEIGHT - 80))

            for event in pygame.event.get(eventtype=[pygame.QUIT, pygame.KEYDOWN]):
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': player_score, 'date': get_formatted_date()})
                        self.show()
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    elif event.key == K_ESCAPE:
                        return
                    else:
                        if len(name) < 4:
                            name += event.unicode

            self.score_text(25, name, C_WHITE, SCORE_POS['Name'])

            pygame.display.flip()
            pass

    def show(self):
        pygame.mixer_music.load('./asset/Score.wav')
        pygame.mixer_music.set_volume(0.4)
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(80, "ASPHALT ESCAPE", C_BLACK, (WIN_WIDTH / 2, 80))
        self.score_text(80, "ASPHALT ESCAPE", C_YELLOW, ((WIN_WIDTH / 2) + 5, 80))
        self.score_text(20, "© Copyright 2025 - Aluno: Dio Ricardo Ferreira Vieira - RU: 4751823", C_BLACK,
                        ((WIN_WIDTH / 2), WIN_HEIGHT - 80))

        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title'])
        self.score_text(20,
                        'NAME                                     SCORE                                 DATE          ',
                        C_YELLOW, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(20,
                            f'{name}                                     {score:08d}                     {date}',
                            C_YELLOW,
                            SCORE_POS[list_score.index(player_score)])

        while True:
            pygame.display.flip()

            for event in pygame.event.get(eventtype=[pygame.QUIT, KEYDOWN]):
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return

            pass

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Stencil", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
