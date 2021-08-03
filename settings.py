class Settings():
    """一个包含所有设置的类"""

    def __init__(self):
        """游戏的基础信息"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # 飞船设置
        self.ship_limit = 3
            
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        
        # 外星人设置
        self.fleet_drop_speed = 10
            
        # 游戏速度
        self.speedup_scale = 1.1
        # 增加的速度
        self.score_scale = 1.5
    
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """游戏改变的数值"""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        
        # 得分
        self.alien_points = 50
    
        self.fleet_direction = 1
        
    def increase_speed(self):
        """提高速度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        
        self.alien_points = int(self.alien_points * self.score_scale)
