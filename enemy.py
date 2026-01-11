import pygame
import random

class EnemyPlugin:
    def __init__(self):
        # 初始兩顆球
        self.enemies = [[random.randint(0, 750), 0], [random.randint(0, 750), -300]]
        self.color = (255, 0, 0)
        self.speed = 3 

    def update(self):
        for e in self.enemies:
            e[1] += self.speed

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)