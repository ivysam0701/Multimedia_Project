import pygame

class ScorePlugin:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont("arial", 24)

    def update(self):
        # 這裡不需要判斷 lives，因為 main.py 已經幫我們停掉 update 了
        self.score += 1 

    def draw(self, screen):
        score_surf = self.font.render(f"SCORE: {self.score}", True, (255, 255, 255))
        screen.blit(score_surf, (10, 60)) # 顯示在生命值下方