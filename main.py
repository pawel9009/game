import pygame
from settings import *
from level import Level
from support import change_dimension
import time
pygame.init()
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Comic Sans MS", 24)

def draw_text(text, font, color, surface, x,y):
    oobj = font.render(text, 1 , color)
    text_rect = oobj.get_rect()
    text_rect.topleft = (x,y)
    surface.blit(oobj, text_rect)
click = False

def main_menu():
    while True:
        win.fill((0,0,0))
        draw_text('main menu', font, (255,255,255), win, win_width//2,20)

        mx, my = pygame.mouse.get_pos()

        button1 = pygame.Rect(win_width//2,244,200,50)
        button2 = pygame.Rect(win_width//2,322,200,50)

        if button1.collidepoint((mx,my)):
            if click:
                game()
        if button2.collidepoint((mx,my)):
            if click:
                print('options')
        pygame.draw.rect(win,(255,0,0), button1)
        pygame.draw.rect(win,(255,0,0), button2)

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



def game():

    heart = pygame.image.load('graphics/heart.png').convert_alpha()
    portal = pygame.image.load('graphics/nowyportal.png').convert_alpha()

    sound = pygame.mixer.music.load('sound/feel.mp3')

    size = 8
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.01)
    map = create_map(size)
    # main loop
    level_num = 0
    level_lenght = len(map)
    level = Level(map, win)
    level.end_portal = portal

    text = font.render("Front", False, [128, 64, 255])
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



if __name__ == "__main__":
    main_menu()
