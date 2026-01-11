import pygame

class ScorePlugin:
    def __init__(self):
        self.score = 0
        # 務必確保定義了 self.font，解決之前的報錯
        self.font = pygame.font.SysFont("arial", 30) 

    def update(self):
        pass # 分數由 main.py 判定接球時增加

    def draw(self, screen):
        score_text = f"Score: {self.score}"
        score_surf = self.font.render(score_text, True, (255, 255, 255))
        
        # 修正 image_3eba32：動態計算文字寬度，確保永遠靠右顯示
        text_width = score_surf.get_width()
        screen.blit(score_surf, (780 - text_width, 20))