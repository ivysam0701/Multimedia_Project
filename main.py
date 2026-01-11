import pygame
import sys

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.plugins = []
        self.running = True # 解決 image_3dcdeb.png 報錯

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    def run(self):
        font = pygame.font.SysFont("arial", 72)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            # 更新邏輯
            for p in self.plugins:
                p.update()
            
            # 碰撞偵測
            player = self.plugins[0]
            enemy_plugin = self.plugins[1]
            for e_pos in enemy_plugin.enemies:
                e_rect = pygame.Rect(e_pos[0]-15, e_pos[1]-15, 30, 30)
                if player.rect.colliderect(e_rect):
                    player.lives -= 1
                    e_pos[1] = -50 # 撞到後敵人重生
            
            # 繪製畫面
            self.screen.fill((30, 30, 30))
            for p in self.plugins:
                p.draw(self.screen)
            
            if player.lives <= 0:
                text_surf = font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(text_surf, (200, 250))
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    from player import PlayerPlugin
    from enemy import EnemyPlugin
    engine = GameEngine()
    engine.register_plugin(PlayerPlugin())
    engine.register_plugin(EnemyPlugin())
    engine.run()