import pygame
import random

class EnemyPlugin:
    def __init__(self):
        self.enemies = []
        # 初始化兩顆球，拉開垂直距離避免重疊
        self.enemies.append({'pos': [random.randint(50, 750), -50], 'type': "NORMAL"})
        self.enemies.append({'pos': [random.randint(50, 750), -350], 'type': "NORMAL"})
        self.speed = 3 

    def spawn_enemy(self):
        # 調整機率：普通(80%), 黃金(5%), 炸彈(10%), 補血(5%)
        rand_type = random.choices(["NORMAL", "GOLD", "BOMB", "LIFE"], weights=[80, 5, 10, 5])[0]
        self.enemies.append({'pos': [random.randint(50, 750), -50], 'type': rand_type})

    def update(self):
        for e in self.enemies: e['pos'][1] += self.speed

    def draw(self, screen):
        for e in self.enemies:
            color = (231, 76, 60) # 普通紅球
            if e['type'] == "GOLD": color = (241, 196, 15) # 黃金球
            elif e['type'] == "BOMB": color = (44, 62, 80)  # 炸彈球
            elif e['type'] == "LIFE": color = (52, 152, 219) # 補血藍球
            
            # 繪製陰影與主體
            pygame.draw.circle(screen, color, (int(e['pos'][0]), int(e['pos'][1])), 15)
            pygame.draw.circle(screen, (255, 255, 255), (int(e['pos'][0]-5), int(e['pos'][1]-5)), 5) # 光澤