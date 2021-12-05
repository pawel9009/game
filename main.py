import pygame
from settings import *
from level import Level
from support import change_dimension
import time

pygame.init()
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
heart = pygame.image.load('graphics/heart.png').convert_alpha()
portal = pygame.image.load('graphics/nowyportal.png').convert_alpha()

sound = pygame.mixer.music.load('sound/feel.mp3')


# pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.01)
map = level_map
# main loop
level_num = 0
level_lenght = len(map)
level = Level(map, win)
level.end_portal = portal
font = pygame.font.SysFont("Comic Sans MS", 24)
text = font.render("Front", False, [128, 64, 255])
end = font.render("Koniec gry !!!", False, [128, 64, 222])
run = True

change_color = True
zmienna = 0

current_color = 0
counting_up = True
while run:

    clock.tick(60)
    lives = level.lives
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
            elif event.key == pygame.K_d:
                liczba = (level.player_x * -1) // tile_size
                if level.front_dimension:
                    s = time.time()
                    copy = change_dimension(map, liczba)

                    level.setup_level(copy)
                    print(time.time() - s, 'czas kopii')
                    level.front_dimension = False
                    text = font.render("Depth", False, [128, 64, 255])
                else:
                    print(liczba, level_lenght, "wymiary")

                    level.setup_level(map[liczba])
                    level.front_dimension = True
                    text = font.render("Front", False, [128, 64, 255])


    win.fill('white')
    # staty = time.time()

    level.run()
    # print(time.time() - staty)
    win.blit(text, [0, 0])
    if lives > 0:
        for x in range(lives):
            win.blit(heart, [x * 30, 50])
    else:
        win.blit(end, [win_width // 2, win_height // 2])
    pygame.display.update()
pygame.quit()
