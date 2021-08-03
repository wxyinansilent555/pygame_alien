class GameStats():
    """跟踪游戏的统计数据."""
    
    def __init__(self, ai_settings):
        """初始化统计数据."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score should never be reset.
        self.high_score = 0
        
    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计数据."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
