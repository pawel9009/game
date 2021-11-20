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


def change_dimension(map, num):
    """Change dimension on map"""
    new_level = []
    index = num
    print(index)
    for dimension in range(len(map[0])):
        new_level.append('')
    for dimmendion in map:
        for i, row in enumerate(dimmendion):
            new_level[i] = new_level[i] + row[index]
    for a in new_level:
        print(a)
    return new_level
