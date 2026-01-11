import pygame

class ScorePlugin:
    def init(self):
        self.score = 0
        self.font = pygame.font.SysFont("arial", 30) 

    def update(self):
        pass 

    def draw(self, screen):
        # --- 修正 1：靠右對齊，預留空間給數字長度 ---
        score_text = f"Score: {self.score}"
        score_surf = self.font.render(score_text, True, (255, 255, 255))
        # 確保 X 座標會根據文字寬度自動調整，不超出 800
        text_width = score_surf.get_width()
        screen.blit(score_surf, (780 - text_width, 20))