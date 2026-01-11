import pygame
import random

class EnemyPlugin:
    def init(self):
        self.enemies = [[random.randint(0, 750), 0]] # 解決 image_3dd92d.png 報錯
        self.color = (255, 0, 0)
        self.speed = 3 # 解決 image_3dd228.png 報錯

    def update(self):
        self.speed += 0.001
        for e in self.enemies:
            e[1] += self.speed
            if e[1] > 600:
                e[0], e[1] = random.randint(0, 750), 0

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)