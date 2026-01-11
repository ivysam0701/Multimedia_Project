import pygame

class ScorePlugin:
    def __init__(self):
        self.score = 0
        # 修正 image_3e5cb0 的錯誤
        self.font = pygame.font.SysFont("arial", 30) 

    def update(self):
        pass # 分數由 main.py 接到球時增加

    def draw(self, screen):
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_surf, (650, 20))