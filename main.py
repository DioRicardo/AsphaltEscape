import pygame

pygame.init()

window = pygame.display.set_mode(size=(840, 980))

while True:
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
