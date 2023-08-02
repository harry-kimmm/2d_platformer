import pygame
from tiles import Tile
from deathtiles1 import DeathTile1
from deathtiles2 import DeathTile2
from wintile import WinTile
from settings import tile_size, screen_width, screen_height
from player import Player

class Level:
    def __init__(self, level_data, surface):
        # Level Setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.deathtiles = pygame.sprite.Group()
        self.wintiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for r, row in enumerate(layout):
            for c, cell in enumerate(row):
                x = c * tile_size 
                y = r * tile_size
                if cell == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if cell == 'D':
                    dTile = DeathTile1((x, y), tile_size)
                    self.deathtiles.add(dTile)
                if cell == 'Y':
                    dTile = DeathTile2((x, y), tile_size)
                    self.deathtiles.add(dTile)
                if cell == 'W':
                    wTile = WinTile((x, y), tile_size)
                    self.wintiles.add(wTile)
 
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def death_collision(self):

        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.deathtiles.sprites():
            if sprite.rect.colliderect(player.rect):
                pygame.time.wait(1000)
                pygame.quit()

    def win_collision(self):
        font = pygame.font.Font('freesansbold.ttf', 50)
        text = font.render('You win!', True, (255,255,0), (255 ,255, 255))
        textRect = text.get_rect()
        textRect.center = (screen_width // 2, screen_height // 2)

        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.wintiles.sprites():
            if sprite.rect.colliderect(player.rect):
                self.display_surface.blit(text, textRect)
                

    def horizontal_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

    def vertical_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


    def run(self):
        # Tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.deathtiles.update(self.world_shift)
        self.deathtiles.draw(self.display_surface)
        self.wintiles.update(self.world_shift)
        self.wintiles.draw(self.display_surface)
        self.scroll_x()

        # Player
        self.player.update()
        self.horizontal_collision()
        self.vertical_collision()
        self.death_collision()
        self.win_collision()
        self.player.draw(self.display_surface)
        