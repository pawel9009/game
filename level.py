import pygame
from tiles import Tile
from settings import tile_size, win_width, win_height
from player import *
from particles import ParticleEffect


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface

        self.lv = 0
        self.current_level = level_data[0]
        self.player_x = 0
        self.player_y = 0
        self.player = pygame.sprite.GroupSingle(None)
        self.setup_level(self.current_level)
        self.world_shift_x = 0
        self.world_shift_y = 0

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def create_jump_praticles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)

        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()

        player_pos = (win_width // 2, win_height // 2)

        for index_row, row in enumerate(layout):
            for index_col, cell in enumerate(row):
                x = tile_size * index_col
                y = tile_size * index_row
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    tile.update(self.player_x + 512, self.player_y)
                    self.tiles.add(tile)
                player = Player((player_pos), self.display_surface, self.create_jump_praticles)
                self.player.add(player)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.dir.x

        if player_x < win_width / 2 and direction_x < 0:
            self.world_shift_x = 8
            self.player_x += 8
            player.speed = 0
        elif player_x > win_width - (win_width / 2) and direction_x > 0:
            self.world_shift_x = -8
            player.speed = 0
            self.player_x -= 8
        else:
            self.world_shift_x = 0
            player.speed = 8

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.dir.y

        if player_y < win_height / 2 and direction_y < 0:
            self.world_shift_y = 8
            player.rect.y += 8
            self.player_y += 8
        elif player_y > win_height - (win_height / 4) and direction_y >= 0:

            self.world_shift_y = player.jump_speed
            player.rect.y += player.jump_speed
            self.player_y += player.jump_speed
        else:
            self.world_shift_y = 0

    def save(self):
        if self.player_y < -700:
            self.player_y = -250
            self.player_x = -34
            self.setup_level(self.current_level)

    def input(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.dir.x = 1
            self.facing_right = True
        elif keys[pygame.K_LEFT]:
            self.dir.x = -1
            self.facing_right = False
        else:
            self.dir.x = 0

    def test_colision(self):
        hit_list = []
        player = self.player.sprite
        for tile in self.tiles.sprites():
            if tile.rect.colliderect(player.rect):
                hit_list.append(tile)
        return hit_list

    def move(self):
        player = self.player.sprite
        player.rect.x += player.dir.x * player.speed
        hit_list = self.test_colision()

        for tile in hit_list:
            if player.dir.x == 0:
                if not player.facing_right:
                    player.rect.left = tile.rect.right
                    self.current_x = player.rect.left
                    player.on_left = True

                if player.facing_right:
                    player.rect.right = tile.rect.left
                    self.current_x = player.rect.right
                    player.on_right = True

            elif player.dir.x < 0:
                player.rect.left = tile.rect.right
                player.on_left = True
                self.current_x = player.rect.left

            elif player.dir.x > 0:
                player.rect.right = tile.rect.left
                player.on_right = True
                self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.dir.x >= 0):
            player.on_left = False

        if player.on_right and (player.rect.right < self.current_x or player.dir.x <= 0):
            player.on_right = False
        self.get_player_on_ground()

        # -----------------------------------
        player = self.player.sprite

        player.apply_gravity()

        hit_list = self.test_colision()

        for tile in hit_list:
            if player.dir.y > 0:

                player.rect.bottom = tile.rect.top
                player.dir.y = 0
                player.on_ground = True
            elif player.dir.y < 0:
                player.rect.top = tile.rect.bottom
                player.on_ceiling = True

        if player.on_ground and player.dir.y < 0 or player.dir.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.dir.y > 0 or player.dir.y > 1:
            player.on_ceiling = False

    def run(self):
        # dust
        self.dust_sprite.update(self.world_shift_x)
        self.dust_sprite.draw(self.display_surface)
        # level
        self.tiles.update(self.world_shift_x, self.world_shift_y)
        self.tiles.draw(self.display_surface)

        # player
        self.player.update()
        self.move()
        self.scroll_x()
        self.create_landing_dust()
        self.scroll_y()
        self.save()
        self.player.draw(self.display_surface)
