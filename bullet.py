import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """一个描述冲飞船上发射子弹的类"""

    def __init__(self, ai_settings, screen, ship):
        """创建子弹，根据飞船的位置"""
        super(Bullet, self).__init__()
        self.screen = screen

        #先在（0，0）创建子弹，再移动到正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
            ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #存储子弹的数量
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """在屏幕上移动子弹"""
        # 更新子弹的位置
        self.y -= self.speed_factor
        #更新到正确的位置
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上更新正确位置"""
        pygame.draw.rect(self.screen, self.color, self.rect)
