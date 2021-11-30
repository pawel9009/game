import pygame

class T(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)
        self.colide = True

class Tile(T):
    def __init__(self, pos, size, color):
        super().__init__(pos,size)
        self.image = pygame.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y, color):
        self.rect.x += x
        self.rect.y += y
        self.image.fill(color)

class Portal(T):
    def __init__(self, pos, size, img):
        super().__init__(pos, size)
        self.colide = False
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x, y, color):
        self.rect.x += x
        self.rect.y += y