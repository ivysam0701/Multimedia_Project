import pygame
import sys
import random

class GameEngine:
    def __init__(self):
        pygame.init()
        pygame.mixer.init() # 初始化音效系統
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.plugins = []
        self.running = True
        
        # --- 加入背景音樂 ---
        try:
            pygame.mixer.music.load('bgm.mp3') # 確保檔案名稱正確
            pygame.mixer.music.play(-1) # -1 代表無限循環
            pygame.mixer.music.set_volume(0.5) # 音量 50%
            self.catch_sound = pygame.mixer.Sound('catch.wav') # 接球音效
        except:
            print("警告：找不到音樂檔，將在無聲模式下運行")
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
                
                enemy_plugin.speed = 3 + (score_plugin.score // 1000) # 稍微放慢難度提升速度
                
                for e_pos in enemy_plugin.enemies:
                    e_rect = pygame.Rect(e_pos[0]-15, e_pos[1]-15, 30, 30)
                    
                    if player.rect.colliderect(e_rect):
                        score_plugin.score += 100 
                        if self.catch_sound: self.catch_sound.play() # 播放接球音
                        e_pos[1] = -50 
                        # --- 修正 2：讓球重生在玩家附近，不要太遠 ---
                        safe_x = random.randint(max(0, player.rect.x - 200), min(750, player.rect.x + 200))
                        e_pos[0] = safe_x
                    
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
                pygame.mixer.music.stop() # 結束時停止音樂
            
            pygame.display.flip()
            self.clock.tick(60)