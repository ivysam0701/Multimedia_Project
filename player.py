# player.py
class PlayerPlugin:
    def __init__(self):
        self.rect = pygame.Rect(400, 500, 50, 50)
        self.color = (0, 255, 0)
        self.lives = 3 # 投影片提到的額外功能：免死機會

    def take_damage(self):
        self.lives -= 1
        print(f"扣血！剩餘生命: {self.lives}")

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0: self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < 800: self.rect.x += 5

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
        # 簡單顯示生命值 (多媒體視覺反饋)
        for i in range(self.lives):
            pygame.draw.circle(screen, (0, 255, 0), (30 + i*30, 30), 10)