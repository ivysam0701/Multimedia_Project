import pygame
import sys

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("多媒體期末專案：插件式遊戲引擎")
        self.clock = pygame.time.Clock()
        self.plugins = []  # 存放所有註冊的插件

    def register_plugin(self, plugin):
        """用於掛載功能的介面"""
        self.plugins.append(plugin)

    def run(self):
        while True:
            # 1. 基本事件處理
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # 2. 插件邏輯更新 (Base 不管內容，只管發號施令)
            for p in self.plugins:
                p.update()
            
            # 3. 畫面繪製
            self.screen.fill((30, 30, 30))  # 背景
            for p in self.plugins:
                p.draw(self.screen)
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    from player import PlayerPlugin
    from enemy import EnemyPlugin
    
    engine = GameEngine()
    # 稍微設定：註冊插件
    engine.register_plugin(PlayerPlugin())
    engine.register_plugin(EnemyPlugin())
    
    engine.run()