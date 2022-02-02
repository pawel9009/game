import random

tile_size = 100
win_width = 1400
win_height = 850

choice = ['X', ' ', ' ', ' ']

def create(size, random_number_portal):
    array = list(range(size))

    """ if must to create portal in this dimension"""
    if random_number_portal:
        for number in range(size):
            row = ''
            for a in range(size):
                ran = random.randint(0, 3)
                row += choice[ran]
            array[number] = row
        portal_x, portal_y = (random.randint(2, size) % (size // 3) * 2, random.randint(2, size) - 2)
        while array[portal_x][portal_y] == 'X':
            portal_x, portal_y = (
                random.randint(0, size) % (size // 3) * 2, random.randint(0, size) - 2)
        tmp = array[portal_x]
        tmp = tmp[0:portal_y - 1] + 'P' + tmp[portal_y::]
        array[portal_x] = tmp
    else:
        for number in range(size):
            row = ''
            for a in range(size):
                ran = random.randint(0, 3)
                row += choice[ran]
            array[number] = row

    array[-1] = 'X'*size
    return array


def create_map_size(size):
    new_map = []
    random_number = random.randint(0, size)
    for number in range(size):
        if number == random_number:
            new_map.append(create(size, 1))
        else:
            new_map.append(create(size, 0))
    return new_map


level_map = [
    ['                          ',
     'XX                        ',
     '  X  X      X             ',
     '        XX   XXXXXX       ',
     '       XXX                ',
     ' X  XX    P  X         XXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX', ],

    ['XXXX                      ',
     'XXXX                      ',
     '     X      X             ',
     '         X   XXXXXX       ',
     '     X XXX                ',
     '    XX       X         XXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     '                          ',
     '                          ',
     'X                         ',
     'X            X         XXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

    ['XXXX                      ',
     '            X             ',
     ' X                        ',
     '                          ',
     'X                         ',
     'X XX X  XX XX  X X X  XXX ',
     'XXXXXXXXXXXXXXXXXXXXXXXXXX',
     'XXXXXXXXXXXXXXXXXXXXxXXXXX', ],

]
