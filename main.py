import pygame
from settings import *
from level import Level
from support import change_dimension

pygame.init()
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

font = pygame.font.SysFont("FFF Forward", 44)

play_button = pygame.image.load('graphics/others/play.png')
play_rect = play_button.get_rect(topleft=(100, 200))

options_button = pygame.image.load('graphics/others/options.png')
options_rect = options_button.get_rect(topleft=(100, 400))

left_button_size = pygame.image.load('graphics/others/left.png')
left_rect_size = left_button_size.get_rect(topleft=(win_width // 2 - 70, 200))

right_button_size = pygame.image.load('graphics/others/right.png')
right_rect_size = right_button_size.get_rect(topleft=(win_width // 2 + 70, 200))

left_button_time = left_button_size
left_rect_time = left_button_size.get_rect(topleft=(win_width // 2 - 70, 300))

right_button_time = right_button_size
right_rect_time = right_button_size.get_rect(topleft=(win_width // 2 + 70, 300))

heart = pygame.image.load('graphics/others/heart.png').convert_alpha()
portal = pygame.image.load('graphics/others/nowyportal.png').convert_alpha()

sound = pygame.mixer.music.load('sound/feel.mp3')


def draw_text(text, font, color, surface, x, y):
    oobj = font.render(text, 1, color)
    text_rect = oobj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(oobj, text_rect)





def main_menu():
    size = 8
    time = 40
    click = False

    while True:
        win.fill((0, 0, 0))
        draw_text('main menu', font, (255, 255, 255), win, win_width // 2, 20)

        mx, my = pygame.mouse.get_pos()
        if play_rect.collidepoint((mx, my)):
            if click:
                game(size, time)
        if options_rect.collidepoint((mx, my)):
            if click:
                size, time = options(size, time)

        win.blit(play_button, [100, 200])
        win.blit(options_button, [100, 400])

        click = False
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


def game(size, time):
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.01)
    map = create_map_size(size)
    tmp = time
    level = Level(map, win, 3)
    level.world_shift_x = -500

    level.end_portal = portal
    tick_timer = 0
    text = font.render("OPTIONS", False, [128, 64, 255])
    end = font.render("Koniec gry !!!", False, [128, 64, 222])
    run = True
    lvl = 1
    while run:

        clock.tick(60)
        lives = level.lives

        if tick_timer == 59:
            tick_timer = 0
            tmp -= 1
            if tmp == 0:
                level.lives -= 1
                tmp = time
        tick_timer += 1

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
            lvl +=1
            map = create_map_size(size)
            level = Level(map, win, lives)
            tmp = time


        win.fill('black')
        level.run()
        draw_text(f'{tmp}', font, (44, 255, 255), win, win_width - 70, 20)
        draw_text(f'Lvl. {lvl}', font, (44, 255, 255), win, win_width//2-20, 20)
        win.blit(text, [0, 0])
        if lives > 0:
            for x in range(lives):
                win.blit(heart, [x * 30, 50])
        else:
            run = False
        pygame.display.update()
    pygame.mixer.music.stop()


def options(size, time, click=None):
    run = True
    while run:

        win.fill((0, 0, 0))
        draw_text('options', font, (255, 255, 255), win, win_width // 2, 20)

        draw_text('World size', font, (255, 255, 255), win, win_width // 2 - 50, 170)
        draw_text(f'{size}', font, (255, 255, 255), win, win_width // 2 + 10, 210)

        draw_text('Time', font, (255, 255, 255), win, win_width // 2 - 10, 270)
        draw_text(f'{time}', font, (255, 255, 255), win, win_width // 2 + 10, 310)

        mx, my = pygame.mouse.get_pos()

        if left_rect_size.collidepoint((mx, my)):
            if click and size > 6:
                size -= 1
        if right_rect_size.collidepoint((mx, my)):
            if click and size < 20:
                size += 1

        if left_rect_time.collidepoint((mx, my)):
            if click and time > 20:
                time -= 1
        if right_rect_time.collidepoint((mx, my)):
            if click and time < 200:
                time += 1

        win.blit(left_button_size, [win_width // 2 - 70, 200])
        win.blit(right_button_size, [win_width // 2 + 70, 200])

        win.blit(left_button_time, [win_width // 2 - 70, 300])
        win.blit(right_button_time, [win_width // 2 + 70, 300])

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
    return [size, time]


if __name__ == "__main__":
    main_menu()
