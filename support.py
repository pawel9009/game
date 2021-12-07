from os import walk
import pygame


def import_folder(path):
    """Import images from folder"""
    surface_list = []

    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list


def create_dimension(map, num):
    """Create dimension current map"""

    new_level = []
    index = num
    for dimension in range(len(map[0])):
        new_level.append('')
    for dimension in map:
        for i, row in enumerate(dimension):
            new_level[i] = new_level[i] + row[index]
    return new_level

def change_dimension(level,map, font):
    liczba = (level.player_x * -1) // 100
    if level.front_dimension:

        copy = create_dimension(map, liczba)

        level.setup_level(copy)
        level.front_dimension = False
        t = font.render("Depth", False, [128, 64, 255])
    else:

        level.setup_level(map[liczba])
        level.front_dimension = True
        t = font.render("Front", False, [128, 64, 255])
    return level,t



