import random

tile_size = 100
win_width = 16 * 64
win_height = 600

choice = ['X', ' ', ' ', ' ',' ']


def create(size, add_portal):
    tab = list(range(size))
    """ if must to create portal in this dimension"""
    if add_portal == 1:
        for x in range(size):
            line = ''
            for a in range(size):
                ran = random.randint(0, 3)
                line += choice[ran]
            tab[x] = line
        portal_x, portal_y = (random.randint(2, size) % (size // 3) * 2, random.randint(2, size) - 2)
        while tab[portal_x][portal_y] == 'X':
            portal_x, portal_y = (
                random.randint(0, size) % (size // 3) * 2, random.randint(0, size) - 2)
        tmp = tab[portal_x]
        tmp = tmp[0:portal_y - 1] + 'P' + tmp[portal_y::]
        tab[portal_x] = tmp
    else:
        for x in range(size):
            line = ''
            for a in range(size):
                ran = random.randint(0, 3)
                line += choice[ran]
            tab[x] = line
    return tab


def create_map(size):
    new = []
    add = random.randint(0, size)
    for x in range(size):
        if x == add:
            new.append(create(size, 1))
        else:
            new.append(create(size, 0))
    return new


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
