import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """代表单个外星人的类."""

    def __init__(self, ai_settings, screen):
        """初始化外星人，设置初始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载图片和他的矩形
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # 每个外星人初始位置在屏幕左上方
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #存储每个外星人的确切位置
        self.x = float(self.rect.x)
        
    def check_edges(self):
        """外星人超过边缘返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
        
    def update(self):
        """从右到左移动外星人"""
        self.x += (self.ai_settings.alien_speed_factor *
                        self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """画出外星人"""
        self.screen.blit(self.image, self.rect)
