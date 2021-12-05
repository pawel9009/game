import pygame

class T(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((100, 100))
        self.rect = self.image.get_rect(topleft=pos)
        self.colide = True

class Tile(T):
    def __init__(self, pos, size, img):
        super().__init__(pos)
        self.image = pygame.Surface((size, size))
        self.image=img
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x, y, ):
        self.rect.x += x
        self.rect.y += y


class Portal(T):
    def __init__(self, pos, img):
        super().__init__(pos)
        self.colide = False
        self.image = img
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x, y):
        self.rect.x += x
        self.rect.y += y