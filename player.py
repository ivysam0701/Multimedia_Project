import pygame

class PlayerPlugin:
    def __init__(self, max_lives=3, speed=7, magnet_range=0):
        self.width, self.height = 60, 60
        self.rect = pygame.Rect(370, 500, self.width, self.height)
        self.max_lives = max_lives
        self.lives = max_lives 
        self.move_speed = speed
        self.magnet_range = magnet_range
        self.image = None
        self.color = (46, 204, 113) # 鮮豔綠
        self.dash_cd = 0 

    def load_local_image(self, file_path):
        """更換角色造型"""
        try:
            original_image = pygame.image.load(file_path).convert_alpha()
            self.image = pygame.transform.smoothscale(original_image, (self.width, self.height))
        except: pass

    def update(self):
        keys = pygame.key.get_pressed()
        move_dir = 0
        if keys[pygame.K_LEFT] and self.rect.left > 0: 
            self.rect.x -= self.move_speed
            move_dir = -1
        if keys[pygame.K_RIGHT] and self.rect.right < 800: 
            self.rect.x += self.move_speed
            move_dir = 1
        
        # 閃現：左 Shift 鍵
        if keys[pygame.K_LSHIFT] and self.dash_cd <= 0 and move_dir != 0:
            self.rect.x += move_dir * 160 
            self.dash_cd = 60 
        if self.dash_cd > 0: self.dash_cd -= 1

    def draw(self, screen):
        # 繪製角色
        if self.image: 
            screen.blit(self.image, self.rect)
        else: 
            pygame.draw.rect(screen, self.color, self.rect, border_radius=8)
            
        # 繪製生命值圖示 (愛心樣式)
        for i in range(self.lives):
            pygame.draw.circle(screen, (231, 76, 60), (35 + i*35, 35), 12)