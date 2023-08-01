import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        brick = pygame.image.load('../assets/blocks/brick.png')
        self.image = pygame.Surface((size, size))
        self.image.blit(brick, (0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift