import pygame

class ScorePlugin:
    def init(self):
        self.score = 0
        self.font = pygame.font.SysFont("arial", 30)

    def update(self):
        # 分數隨時間微幅增加，或由 main.py 判斷碰撞後呼叫增加
        pass

    def draw(self, screen):
        score_surf = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        screen.blit(score_surf, (650, 20))