import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self, ai_settings, screen):
        """初始化飞船及相关设置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图片，并得到他的矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #飞船的初始位置在屏幕底部
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 存储船的中心位置
        self.center = float(self.rect.centerx)
        
        # 移动
        self.moving_right = False
        self.moving_left = False
        
    def center_ship(self):
        """在屏幕上使船居中"""
        self.center = self.screen_rect.centerx
        
    def update(self):
        """基于移动更新船的数值."""
        #更新船的中心值
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 更新船的矩形
        self.rect.centerx = self.center

    def blitme(self):
        """画出船的图片."""
        self.screen.blit(self.image, self.rect)
