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

    # main.py 核心循環部分
    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # 更新所有插件
            for p in self.plugins:
                p.update()
            
            # --- 碰撞偵測（新增）---
            player = self.plugins[0] # 假設第一個是玩家
            enemy_plugin = self.plugins[1] # 假設第二個是敵人
            
            for e_pos in enemy_plugin.enemies:
                # 建立矩形判定區 (座標, 寬高)
                enemy_rect = pygame.Rect(e_pos[0]-15, e_pos[1]-15, 30, 30)
                if player.rect.colliderect(enemy_rect):
                    # 呼叫玩家插件的「受傷」功能
                    player.take_damage() 
                    # 敵人重置位置避免連續碰撞
                    e_pos[1] = -50 
                    if player.lives <= 0:
                        print("遊戲結束")
                        self.running = False
            # ----------------------

            self.screen.fill((30, 30, 30))
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