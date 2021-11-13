from os import walk
import pygame


def import_folder(path):
    surface_list = []

    for _, __, img_file in walk(path):
        for image in img_file:
            full_path = path + '/' + image
            img_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(img_surf)
    return surface_list


def change_dimension(map, num):
    new = []
    index = num // 100
    print(index)
    for x in range(len(map[0])):
        new.append('')
    for dim in map:
        for i, row in enumerate(dim):
            new[i] = new[i] + row[index]
    for a in new:
        print(a)
    return new
