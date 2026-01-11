import pygame
import random

class EnemyPlugin:
    def init(self):
        self.enemies = [[random.randint(0, 750), 0]]
        self.color = (255, 0, 0)
        self.speed = 3  # <--- 務必加上這行，解決 image_3dd228.png 的錯誤

    def update(self):
        # 這裡會用到 self.speed
        for e in self.enemies:
            e[1] += self.speed
            if e[1] > 600:
                e[0], e[1] = random.randint(0, 750), 0

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)