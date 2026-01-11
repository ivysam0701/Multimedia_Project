import pygame
import random

class EnemyPlugin:
    def init(self):
        self.enemies = [[random.randint(0, 750), 0]]
        self.color = (255, 0, 0)
        self.speed = 3 # 初始速度

    def update(self):
        # 難度演進：每 500 幀稍微增加速度
        self.speed += 0.001 
        for e in self.enemies:
            e[1] += self.speed
            if e[1] > 600:
                e[0], e[1] = random.randint(0, 750), 0

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)