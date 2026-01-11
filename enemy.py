import pygame
import random

class EnemyPlugin:
    def __init__(self):
        self.enemies = [[random.randint(0, 750), 0]]
        self.color = (255, 0, 0)

    def update(self):
        for e in self.enemies:
            e[1] += 3  # 往下掉
            if e[1] > 600:
                e[0], e[1] = random.randint(0, 750), 0

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)