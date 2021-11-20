import random

tile_size = 100
win_width = 16 * 64
win_height = 600
wymiary = [20,10,30]
choice = ['X', ' ',' ', ' ']

def create(pos_x,pos_y):
    tab = list(range(pos_x))
    for x in range(pos_x):
        line = ''
        for a in range(pos_y):
            ran = random.randint(0,3)
            line += choice[ran]
        tab[x] = line
    return tab

def create_map():
    new = []
    for x in range(wymiary[0]):
        new.append(create(wymiary[1], wymiary[2]))
    return new


level_map1 = create_map()
print(level_map1)


level_map = [
    ['                          ',
     'XX                        ',
     '  X  X      X             ',
     '        XX   XXXXXX       ',
     '       XXX                ',
     ' X  XX       X         XXX',
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
