import pygame
from tiles import Tile,Portal
from settings import tile_size, win_width, win_height
from player import *
from particles import ParticleEffect


class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.front_dimension = True
        self.lives = 3
        self.reset_test = False
        self.checkpoint = (0, -200)
        self.lv = 0
        self.current_level = level_data[0]
        self.player_x = 0
        self.player_y = 0
        self.tile_color = (255, 0, 0)
        self.player = pygame.sprite.GroupSingle(None)
        self.setup_level(self.current_level, self.tile_color)
        self.world_shift_x = 0
        self.world_shift_y = 0
        self.world_speed = 8

        self.end_portal = None
        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

    def tile_color_update(self, color):
        self.tile_color = color

    def create_jump_praticles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)

        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def get_player_on_ground(self):
        """Check if player touch the ground"""
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

    def setup_level(self, layout, tile_color):
        """Create lvl"""
        portal = pygame.image.load('graphics/nowyportal.png').convert_alpha()
        self.tiles = pygame.sprite.Group()
        player_pos = (win_width // 2, win_height // 2)

        for index_row, row in enumerate(layout):
            for index_col, cell in enumerate(row):
                x = tile_size * index_col
                y = tile_size * index_row
                if cell == 'X':
                    tile = Tile((x, y), tile_size, tile_color)
                    tile.update(self.player_x + 512, self.player_y, self.tile_color)
                    self.tiles.add(tile)
                elif cell == 'P':
                    portal = Portal((x,y), tile_size,portal)
                    portal.update(self.player_x + 512, self.player_y, 'gray')
                    self.tiles.add(portal)

                player = Player((player_pos), self.display_surface, self.create_jump_praticles)
                self.player.add(player)

    def scroll_x(self):
        """Camera move x"""
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.dir.x

        if player_x < win_width / 2 and direction_x < 0:
            self.world_shift_x = self.world_speed
            self.player_x += self.world_speed
            player.speed = 0
        elif player_x > win_width - (win_width / 2) and direction_x > 0:
            self.world_shift_x = -self.world_speed
            self.player_x -= self.world_speed
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = self.world_speed

    def scroll_y(self):
        """Camera move y"""
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.dir.y

        if player_y < win_height / 2 and direction_y < 0:
            self.world_shift_y = self.world_speed
            player.rect.y += self.world_speed
            self.player_y += self.world_speed
        elif player_y > win_height - (win_height / 5) and direction_y >= 0:

            self.world_shift_y = player.jump_speed
            player.rect.y += player.jump_speed
            self.player_y += player.jump_speed
        elif player_y > win_height - (win_height / 2) and player.look_down:
            self.world_shift_y = player.jump_speed
            player.rect.y += player.jump_speed
            self.player_y += player.jump_speed
        else:
            self.world_shift_y = 0

    def save(self):
        """ 'Checkpoint' """
        if self.player_y < -1400:
            self.lives -= 1
            self.player_y, self.player_x = self.checkpoint
            self.setup_level(self.current_level, self.tile_color)

    def test_colision(self):
        """Check how many colisions"""
        hit_list = []
        player = self.player.sprite
        for tile in self.tiles.sprites():
            if tile.colide:
                if tile.rect.colliderect(player.rect):
                    hit_list.append(tile)
        return hit_list

    def move(self):
        """Move and text colision with tiles"""
        colision = True
        player = self.player.sprite
        player.rect.x += player.dir.x * player.speed
        hit_list = self.test_colision()
        if max(self.tile_color) < 6 and self.reset_test:
            colision = False
            if hit_list:
                self.player_y, self.player_x = self.checkpoint
                self.setup_level(self.current_level, self.tile_color)

        if colision:
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

        player.apply_gravity()

        hit_list = self.test_colision()
        if colision:
            for tile in hit_list:
                if player.dir.y > 0:
                    player.rect.bottom = tile.rect.top
                    player.dir.y = 0
                    player.on_ground = True
                elif player.dir.y < 0:
                    player.dir.y = 0
                    player.rect.top = tile.rect.bottom
                    player.on_ceiling = True

            if player.on_ground and player.dir.y < 0 or player.dir.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.dir.y > 0 or player.dir.y > 1:
                player.on_ceiling = False

    def run(self):
        """Run all functions"""

        # print(self.player_x,self.player_y)
        # dust
        self.dust_sprite.update(self.world_shift_x)
        self.dust_sprite.draw(self.display_surface)
        # level
        self.tiles.update(self.world_shift_x, self.world_shift_y, self.tile_color)
        self.tiles.draw(self.display_surface)
        # player
        self.player.update()
        self.move()
        self.scroll_x()
        self.create_landing_dust()
        self.scroll_y()
        self.save()
        self.player.draw(self.display_surface)
