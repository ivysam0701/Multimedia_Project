import pygame
import sys
import random
import math

class GameEngine:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("接球大作戰 Pro") # 漢化標題
        self.clock = pygame.time.Clock()
        self.plugins = []
        self.state = "MENU"
        self.volume = 0.5
        self.last_dropped_file = None
        self.shake_amount = 0 
        
        # 升級系統變數
        self.total_points = 0      
        self.speed_level = 0       
        self.life_level = 0        
        self.magnet_level = 0      
        self.best_catch = 0 
        
        # 使用系統字體支援中文 (Windows 常用字體)
        self.font_path = "microsoftjhenghei" 
        
        try:
            pygame.mixer.music.load('bgm.mp3')
            self.catch_sound = pygame.mixer.Sound('catch.wav')
            self.gameover_sound = pygame.mixer.Sound('gameover.wav')
            self.bomb_sound = pygame.mixer.Sound('gameover.wav') 
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(self.volume)
        except: self.catch_sound = self.gameover_sound = self.bomb_sound = None

    def reset_game(self):
        from player import PlayerPlugin
        from enemy import EnemyPlugin
        from score import ScorePlugin
        
        self.plugins = [] # 重置插件
        nl = 3 + self.life_level
        ns = 7 + (self.speed_level * 2)
        nm = self.magnet_level * 25 
        
        self.plugins = [PlayerPlugin(nl, ns, nm), EnemyPlugin(), ScorePlugin()]
        self.current_catch = 0
        if self.last_dropped_file: self.plugins[0].load_local_image(self.last_dropped_file)
        self.state = "PLAYING"
        pygame.mixer.music.play(-1)

    def draw_button(self, text, x, y, w, h, color, hover_color, m_pos):
        is_hover = x < m_pos[0] < x+w and y < m_pos[1] < y+h
        curr_color = hover_color if is_hover else color
        # 繪製圓角按鈕與陰影
        pygame.draw.rect(self.screen, (100, 100, 100), (x+2, y+2, w, h), border_radius=15) # 陰影
        pygame.draw.rect(self.screen, curr_color, (x, y, w, h), border_radius=15)
        
        font = pygame.font.SysFont(self.font_path, 22, bold=True)
        txt = font.render(text, True, (255, 255, 255))
        self.screen.blit(txt, txt.get_rect(center=(x+w/2, y+h/2)))
        return is_hover

    def run(self):
        font_big = pygame.font.SysFont(self.font_path, 72, bold=True)
        font_mid = pygame.font.SysFont(self.font_path, 28, bold=True)
        font_small = pygame.font.SysFont(self.font_path, 20)

        while True:
            m_pos = pygame.mouse.get_pos()
            # 倍增成本計算
            s_cost = 1000 * (2 ** self.speed_level)
            l_cost = 1600 * (2 ** self.life_level)
            m_cost = 2400 * (2 ** self.magnet_level)

            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit()
                if event.type == pygame.DROPFILE:
                    self.last_dropped_file = event.file
                    if self.state == "PLAYING": self.plugins[0].load_local_image(event.file)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.state == "MENU":
                        if 300 < m_pos[0] < 500 and 220 < m_pos[1] < 280: self.reset_game()
                        # 商店邏輯
                        if 150 < m_pos[0] < 350 and 340 < m_pos[1] < 400: # 速度
                            if self.total_points >= s_cost: self.total_points -= s_cost; self.speed_level += 1
                        if 450 < m_pos[0] < 650 and 340 < m_pos[1] < 400: # 生命
                            if self.total_points >= l_cost: self.total_points -= l_cost; self.life_level += 1
                        if 300 < m_pos[0] < 500 and 420 < m_pos[1] < 480: # 磁鐵
                            if self.total_points >= m_cost: self.total_points -= m_cost; self.magnet_level += 1
                        # 音量鍵
                        if 320 < m_pos[0] < 360 and 500 < m_pos[1] < 540: self.volume = max(0.0, self.volume-0.1); pygame.mixer.music.set_volume(self.volume)
                        if 440 < m_pos[0] < 480 and 500 < m_pos[1] < 540: self.volume = min(1.0, self.volume+0.1); pygame.mixer.music.set_volume(self.volume)
                    elif self.state == "GAMEOVER":
                        if 300 < m_pos[0] < 500 and 450 < m_pos[1] < 510: 
                            self.plugins = [] # 修復返回基地問題
                            self.state = "MENU"

            # 震動效果處理
            render_offset = [0, 0]
            if self.shake_amount > 0:
                render_offset = [random.randint(-self.shake_amount, self.shake_amount), random.randint(-self.shake_amount, self.shake_amount)]
                self.shake_amount -= 1

            # 介面渲染 (亮灰色系)
            self.screen.fill((240, 240, 240))
            temp_surface = pygame.Surface((800, 600))
            temp_surface.fill((240, 240, 240))

            if self.state == "MENU":
                title = font_big.render("接球大作戰 Pro", True, (44, 62, 80))
                self.screen.blit(title, title.get_rect(center=(400, 80)))
                
                # 分數與漢化提示
                p_txt = font_mid.render(f"累積分數: ${self.total_points} | 最佳紀錄: {self.best_catch}", True, (39, 174, 96))
                self.screen.blit(p_txt, p_txt.get_rect(center=(400, 155)))
                
                guide = font_small.render("[方向鍵] 移動  |  [左 Shift] 衝刺  |  [拖曳圖片] 更換造型", True, (127, 140, 141))
                self.screen.blit(guide, guide.get_rect(center=(400, 195)))
                
                # 商店按鈕漢化
                self.draw_button("開始任務", 300, 220, 200, 60, (52, 152, 219), (41, 128, 185), m_pos)
                self.draw_button(f"速度等級.{self.speed_level} (${s_cost})", 150, 340, 200, 60, (46, 204, 113), (39, 174, 96), m_pos)
                self.draw_button(f"生命等級.{self.life_level} (${l_cost})", 450, 340, 200, 60, (231, 76, 60), (192, 57, 43), m_pos)
                self.draw_button(f"磁鐵等級.{self.magnet_level} (${m_cost})", 300, 420, 200, 60, (155, 89, 182), (142, 68, 173), m_pos)
                
                vol_txt = font_small.render(f"音量: {int(self.volume*100)}%", True, (44, 62, 80))
                self.screen.blit(vol_txt, vol_txt.get_rect(center=(400, 520)))
                self.draw_button("-", 320, 500, 40, 40, (149, 165, 166), (127, 140, 141), m_pos)
                self.draw_button("+", 440, 500, 40, 40, (149, 165, 166), (127, 140, 141), m_pos)

            elif self.state == "PLAYING":
                player, enemy_plugin, score_plugin = self.plugins[0], self.plugins[1], self.plugins[2]
                for p in self.plugins: p.update()
                enemy_plugin.speed = 3 + (score_plugin.score // 1500)
                
                for e in enemy_plugin.enemies[:]:
                    if player.magnet_range > 0:
                        dist = math.hypot(e['pos'][0] - player.rect.centerx, e['pos'][1] - player.rect.centery)
                        if dist < player.magnet_range: e['pos'][0] += (3.5 if e['pos'][0] < player.rect.centerx else -3.5)
                    
                    e_rect = pygame.Rect(e['pos'][0]-15, e['pos'][1]-15, 30, 30)
                    if player.rect.colliderect(e_rect):
                        if e['type'] == "NORMAL": score_plugin.score += 100; self.current_catch += 1
                        elif e['type'] == "GOLD": score_plugin.score += 500; self.current_catch += 1
                        elif e['type'] == "BOMB": 
                            player.lives -= 2; self.shake_amount = 25
                            if self.bomb_sound: self.bomb_sound.play()
                        elif e['type'] == "LIFE": 
                            if player.lives < player.max_lives: player.lives += 1
                        
                        if self.catch_sound and e['type'] not in ["BOMB", "LIFE"]: self.catch_sound.play()
                        enemy_plugin.enemies.remove(e); enemy_plugin.spawn_enemy()
                    elif e['pos'][1] > 600:
                        if e['type'] in ["NORMAL", "GOLD"]:
                            player.lives -= 1
                            self.shake_amount = 12
                        enemy_plugin.enemies.remove(e); enemy_plugin.spawn_enemy()
                
                for p in self.plugins: p.draw(temp_surface)
                self.screen.blit(temp_surface, render_offset)

                if player.lives <= 0:
                    self.total_points += score_plugin.score
                    self.best_catch = max(self.best_catch, self.current_catch)
                    self.state = "GAMEOVER"; pygame.mixer.music.stop()
                    if self.gameover_sound: self.gameover_sound.play()

            elif self.state == "GAMEOVER":
                over = font_big.render("遊戲結束", True, (231, 76, 60))
                self.screen.blit(over, over.get_rect(center=(400, 250)))
                self.draw_button("返回基地", 300, 450, 200, 60, (52, 73, 94), (44, 62, 80), m_pos)

            pygame.display.flip()
            self.clock.tick(60)

if __name__ == "__main__":
    engine = GameEngine()
    engine.run()