import random

tile_size = 100
win_width = 16 * 64
win_height = 600
wymiary = [5, 5, 5]
choice = ['X', ' ', ' ', ' ']


def create(pos_x, pos_y, add_portal):
    tab = list(range(pos_x))
    """ if must to create portal in this dimension"""
    if add_portal == 1:
        for x in range(pos_x):
            line = ''
            for a in range(pos_y):
                ran = random.randint(0, 3)
                line += choice[ran]
            tab[x] = line
        portal_x, portal_y = (random.randint(2, wymiary[1]) % (wymiary[1] // 3) * 2, random.randint(2, wymiary[2]) - 2)
        while tab[portal_x][portal_y] == 'X':
            portal_x, portal_y = (
            random.randint(0, wymiary[1]) % (wymiary[1] // 3) * 2, random.randint(0, wymiary[2]) - 2)
        tmp = tab[portal_x]
        tmp = tmp[0:portal_y - 1] + 'P' + tmp[portal_y::]
        tab[portal_x] = tmp
    else:
        for x in range(pos_x):
            line = ''
            for a in range(pos_y):
                ran = random.randint(0, 3)
                line += choice[ran]
            tab[x] = line
    return tab


def create_map():
    new = []
    add = random.randint(0, wymiary[0])
    for x in range(wymiary[0]):
        if x == add:
            new.append(create(wymiary[1], wymiary[2], 1))
        else:
            new.append(create(wymiary[1], wymiary[2], 0))
    return new


level_map1 = create_map()

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
#
# for index_row, row in enumerate(layout):
#     for index_col, cell in enumerate(row):
#         x, y = tile_size * index_col, tile_size * index_row
#         cos += 1
#         if cell == '':
#             continue
#         elif cell == 'X':
#             tile = Tile((x, y), tile_size, self.img)
#             tile.update(self.player_x + 512, self.player_y)
#             self.tiles.add(tile)
#         elif cell == 'P':
#             portal = Portal((x, y), portal)
#             portal.update(self.player_x + 512, self.player_y, )
#             self.tiles.add(portal)
#
#         player = Player((player_pos), self.display_surface, self.create_jump_praticles)
#         self.player.add(player)