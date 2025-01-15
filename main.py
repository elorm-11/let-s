import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500,400
MOVEMENT_SPPEED = 5
FONT_SIZE = 72

pygame.init()

background_image = pygame.transfrom.scalepygame.image.laod("bg.jpg")
(SCREEN_WIDTH, SCREEN_HEIGHT)

font = pygame.font.sysFront("Times New Roman", FONT_SIZE)

class Sprite(pygame.sprite.Sprite):

    def __init__(self,colour,height, width):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(pygame.Color('dodgerblue'))
        pygame.draw.rect( self.image,color,pygame.rect(0, 0, width, height))
        self.rect = self.image.get_rect()
        
    def move(self, x_change, y_change):
      self.rect.x = max[
         min(self.rect.x + x_change, ,SRCEEN_WIDTH - self.rect.width), 0]
      self.rect.y = max[
         min(self.rect.x + x_change, SCREEN_WIDTH - SELF.RECT.WIDTH), 0]
      
      screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
      pygame.display.set_caption("Sprite Collision")
      all_sprites = pygame.sprite.Group()

      sprite1 = Sprite(pygame.color('black'), 20,30)
      sprite1.rect.x, sprite.rect.y = random.randint(
         0, SCREEN_WIDTH - SPRITE.RECT.WIDTH), random.randint(
            0, screen_height - sprite.rect.height)
all_sprite.add(sprite1)

while running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN
                                       and event.key == pygame.K_x):
        running = False

    if not win:
      keys = pygame.key.get_pressed()
      x_change = (key[pygame.K_RIGHT] -keys[pygame])
         


                                          