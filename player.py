import pygame # 解決 image_33e8c6.png 報錯

class PlayerPlugin:
    def __init__(self):
        self.rect = pygame.Rect(400, 500, 50, 50)
        self.color = (0, 255, 0)
        self.lives = 3 

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 800: self.rect.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        for i in range(self.lives): # 畫出血條
            pygame.draw.circle(screen, (0, 255, 0), (30 + i*30, 30), 10)