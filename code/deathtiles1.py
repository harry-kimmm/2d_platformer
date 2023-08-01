import pygame

class DeathTile1(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        razor = pygame.image.load('../assets/blocks/razor.png')
        self.image = pygame.Surface((size, size))
        self.image.blit(razor, (0, 0))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift