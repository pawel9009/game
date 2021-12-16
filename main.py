import pygame
from settings import *
from level import Level
from support import change_dimension
import time
pygame.init()
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("FFF Forward", 44)

play_button = pygame.image.load('graphics/play.png')
play_rect = play_button.get_rect(topleft = (100,200))

options_button = pygame.image.load('graphics/options.png')
options_rect = options_button.get_rect(topleft=(100, 400))

left_button = pygame.image.load('graphics/left.png')
left_rect = left_button.get_rect(topleft=(win_width//2-70, 200))

right_button = pygame.image.load('graphics/right.png')
right_rect = right_button.get_rect(topleft=(win_width//2+70, 200))

heart = pygame.image.load('graphics/heart.png').convert_alpha()
portal = pygame.image.load('graphics/nowyportal.png').convert_alpha()
size = 8
sound = pygame.mixer.music.load('sound/feel.mp3')

def draw_text(text, font, color, surface, x,y):
    oobj = font.render(text, 1 , color)
    text_rect = oobj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(oobj, text_rect)
click = False

def main_menu(size):
    while True:
        win.fill((0,0,0))
        draw_text('main menu', font, (255,255,255), win, win_width//2,20)

        mx, my = pygame.mouse.get_pos()
        if play_rect.collidepoint((mx,my)):
            if click:
                game(size)
        if options_rect.collidepoint((mx,my)):
            if click:
                print('posszlo')
                size,liczba = options(5)
        print(size)
        win.blit(play_button, [100, 200])
        win.blit(options_button, [100, 400])


        click=False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()
        clock.tick(60)




def game(size):
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.01)
    map = create_map(size)
    # main loop
    level_num = 0
    level_lenght = len(map)
    level = Level(map, win)
    level.end_portal = portal

    text = font.render("OPTIONS", False, [128, 64, 255])
    end = font.render("Koniec gry !!!", False, [128, 64, 222])
    run = True

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
                    level, text = change_dimension(level, map, font)

        if level.next_lvl:
            size += 1
            map = create_map(size)
            level = Level(map, win)
            time.sleep(1)

        win.fill('black')
        level.run()
        win.blit(text, [0, 0])
        if lives > 0:
            for x in range(lives):
                win.blit(heart, [x * 30, 50])
        else:
            win.blit(end, [win_width // 2, win_height // 2])
        pygame.display.update()
    pygame.mixer.music.stop()

def options(size,click=None):
    run = True
    while run:

        win.fill((0, 0, 0))
        draw_text('options', font, (255, 255, 255), win, win_width // 2, 20)
        draw_text('World size', font, (255, 255, 255), win, win_width//2-50, 170)
        draw_text(f'{size}', font, (255, 255, 255), win, win_width//2+10, 210)

        mx, my = pygame.mouse.get_pos()

        if left_rect.collidepoint((mx, my)):
            if click and size>5:
                size-=1
        if right_rect.collidepoint((mx, my)):
            if click and size <20:
                size+=1


        win.blit(left_button, [win_width//2-70, 200])
        win.blit(right_button, [win_width//2+70, 200])

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            pygame.display.update()
            clock.tick(60)
    return [size,11]

if __name__ == "__main__":
    main_menu(size)
