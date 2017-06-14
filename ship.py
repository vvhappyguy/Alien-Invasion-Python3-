import pygame

class Ship():
    def __init__(self,ai_settings, screen):
        """Init ship and it's position"""
        self.screen = screen
        self.ai_settings = ai_settings

        """Downloading img ship and takeing square"""
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        """New ship creats on bottom"""
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        """Saving float coordinate of ship's center"""
        self.center = float(self.rect.centerx)

        """Moving flag"""
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updating position of ship"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):
        """Blitting ship"""
        self.screen.blit(self.image,self.rect)
