import pygame

class Ship():
    def __init__(self, screen):
        """Init ship and it's position"""
        self.screen = screen

        """Downloading img ship and takeing square"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """New ship creats in center"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        """Moving flag"""
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Updating position of ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += 2
        if self.moving_left and self.rect.left > 0:
            self.rect.centerx -= 2
        if self.moving_up and self.rect.centery > 0:
            self.rect.centery -= 2
        if self.moving_down and self.rect.centery < 800:
            self.rect.centery += 2

    def blitme(self):
        """Blitting ship"""
        self.screen.blit(self.image,self.rect)
