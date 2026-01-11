import pygame
import random

class EnemyPlugin:
    def init(self):
        # 解決 image_3e41ed 報錯
        self.enemies = [[random.randint(0, 750), 0]] 
        self.color = (255, 0, 0)
        # 解決 image_3de48e 報錯
        self.speed = 3 

    def update(self):
        # 這裡會用到 self.speed
        self.speed += 0.001
        for e in self.enemies:
            e[1] += self.speed
            if e[1] > 600:
                e[0], e[1] = random.randint(0, 750), 0

    def draw(self, screen):
        for e in self.enemies:
            pygame.draw.circle(screen, self.color, (e[0], e[1]), 20)