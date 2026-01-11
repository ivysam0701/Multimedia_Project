import pygame
import sys
import random

class GameEngine:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # 初始化多媒體音效系統
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.plugins = []
        self.running = True # 解決 image_3dcdeb 報錯

        # --- 多媒體音效設定 ---
        try:
            # 請確保資料夾內有這兩個檔案，或將其換成你自己的檔名
            pygame.mixer.music.load('bgm.mp3') 
            pygame.mixer.music.play(-1) # 背景音樂無限循環
            self.catch_sound = pygame.mixer.Sound('catch.wav') 
        except:
            print("音效檔案載入失敗，將以無聲模式執行")
            self.catch_sound = None

    def register_plugin(self, plugin):
        self.plugins.append(plugin)

    def run(self):
        font = pygame.font.SysFont("arial", 72)
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            player = self.plugins[0]
            enemy_plugin = self.plugins[1]
            score_plugin = self.plugins[2]
            
            if player.lives > 0:
                for p in self.plugins:
                    p.update()
                
                # 動態難度：分數越高球速越快
                enemy_plugin.speed = 3 + (score_plugin.score // 1000)
                
                for e_pos in enemy_plugin.enemies:
                    e_rect = pygame.Rect(e_pos[0]-15, e_pos[1]-15, 30, 30)
                    
                    # 成功接球
                    if player.rect.colliderect(e_rect):
                        score_plugin.score += 100 
                        if self.catch_sound: self.catch_sound.play() # 播放音效
                        e_pos[1] = -50 
                        # 修正：限制重生在玩家 X 軸左右 250 像素內，避免太遠接不到
                        min_x = max(0, player.rect.x - 250)
                        max_x = min(750, player.rect.x + 250)
                        e_pos[0] = random.randint(min_x, max_x)
                    
                    # 漏接球
                    if e_pos[1] > 600:
                        player.lives -= 1
                        e_pos[1] = -50
                        e_pos[0] = random.randint(0, 750)

            self.screen.fill((30, 30, 30))
            for p in self.plugins:
                p.draw(self.screen)
            
            if player.lives <= 0:
                text_surf = font.render("GAME OVER", True, (255, 0, 0))
                self.screen.blit(text_surf, (200, 250))
                pygame.mixer.music.stop() # 遊戲結束停止音樂
            
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    from player import PlayerPlugin
    from enemy import EnemyPlugin
    from score import ScorePlugin
    engine = GameEngine()
    engine.register_plugin(PlayerPlugin())
    engine.register_plugin(EnemyPlugin())
    engine.register_plugin(ScorePlugin())
    engine.run()