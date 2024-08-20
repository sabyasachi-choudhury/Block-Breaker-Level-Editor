import pygame

b_width, b_height = 96, 26


# Block white
class BlueBlock(pygame.sprite.Sprite):
    def __init__(self):
        super(BlueBlock, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("BlueBlock.jpg").convert(), (b_width, b_height))
        self.rect = self.surf.get_rect(center=(800, 80))
        self.id = 'BB'


# Red Block
class RedBlock(pygame.sprite.Sprite):
    def __init__(self):
        super(RedBlock, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("RedBlock.jpg").convert(), (b_width, b_height))
        self.rect = self.surf.get_rect(center=(800, 180))
        self.id = 'RB'


# Yellow Block
class YellowBlock(pygame.sprite.Sprite):
    def __init__(self):
        super(YellowBlock, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("YellowBlock.jpg").convert(), (b_width, b_height))
        self.rect = self.surf.get_rect(center=(800, 280))
        self.id = 'YB'


# Grey Block
class GreenBlock(pygame.sprite.Sprite):
    def __init__(self):
        super(GreenBlock, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("GreenBlock.jpg").convert(), (b_width, b_height))
        self.rect = self.surf.get_rect(center=(800, 380))
        self.id = 'GB'


# Immovable blocks
class Immovable(pygame.sprite.Sprite):
    def __init__(self):
        super(Immovable, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("block_tiles_blue.png").convert(),
                                                 (b_width, b_height * 2 + 4))
        self.rect = self.surf.get_rect(center=(800, 480))
        self.id = 'IM'


# Moving block
class Moving(pygame.sprite.Sprite):
    def __init__(self):
        super(Moving, self).__init__()
        self.surf = pygame.transform.smoothscale(pygame.image.load("MovingBlock.png").convert(), (b_width, b_height))
        self.rect = self.surf.get_rect(center=(800, 580))
        self.id = 'MB'
        self.vel = 1

    def motion(self):
        self.rect.move_ip(self.vel, 0)
        if self.rect.right > 700 or self.rect.left < 0:
            self.vel = -self.vel