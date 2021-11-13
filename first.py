import pygame
from settings import *
from level import Level
from support import change_dimension

pygame.init()

win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# main loop
level_num = 0
level = Level(level_map, win)

run = True

while run:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1 and level_num < 4:
                level_num += 1
                level.setup_level(level_map[level_num])

            elif event.key == pygame.K_F2 and level_num > 0:
                level_num -= 1
                level.setup_level(level_map[level_num])

            elif event.key == pygame.K_e:
                liczba = level.player_x * -1
                map = change_dimension(level_map, liczba)

                level.setup_level(map)

    win.fill('black')
    level.run()
    pygame.display.update()

pygame.quit()
