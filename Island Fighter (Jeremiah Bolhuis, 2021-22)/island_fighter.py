# Imports
import pygame
import random
import math

# Window settings
WIDTH = 1200
HEIGHT = 800
TITLE = "Space Warrior"
FPS = 60


# Make the game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()


# Define colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)

BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

   
# Fonts
FONT_SM = pygame.font.Font(None, 48)
FONT_MD = pygame.font.Font(None, 64)
FONT_LG = pygame.font.Font(None, 96)


# Load images
background = pygame.image.load('assets/images/background.jpg').convert_alpha()
start_img = pygame.image.load('assets/images/start_screen.jpg').convert_alpha()
end_img = pygame.image.load('assets/images/end_screen.jpg').convert_alpha()
win_img = pygame.image.load('assets/images/win_screen.jpg').convert_alpha()

ship_img = pygame.image.load('assets/images/player_ship.png').convert_alpha()
bullet_img = pygame.image.load('assets/images/bullet-1.png').convert_alpha()
enemy1_img = pygame.image.load('assets/images/enemy1_ship.png').convert_alpha()
enemy1_ship_damaged_1_img = pygame.image.load('assets/images/enemy1_ship_damaged_1.png').convert_alpha()
enemy1_ship_damaged_2_img = pygame.image.load('assets/images/enemy1_ship_damaged_2.png').convert_alpha()
enemy1_ship_damaged_3_img = pygame.image.load('assets/images/enemy1_ship_damaged_3.png').convert_alpha()
enemy1_ship_damaged_4_img = pygame.image.load('assets/images/enemy1_ship_damaged_4.png').convert_alpha()
enemy1_mini_1_img = pygame.image.load('assets/images/enemy1_mini_1.png').convert_alpha()
enemy1_mini_1_damaged1_img = pygame.image.load('assets/images/enemy1_mini_1_damaged_1.png').convert_alpha()
enemy1_mini_1_damaged2_img = pygame.image.load('assets/images/enemy1_mini_1_damaged_2.png').convert_alpha()
enemy1_mini_1_damaged3_img = pygame.image.load('assets/images/enemy1_mini_1_damaged_3.png').convert_alpha()
enemy1_mini_1_damaged4_img = pygame.image.load('assets/images/enemy1_mini_1_damaged_4.png').convert_alpha()
enemy1_mini_2_img = pygame.image.load('assets/images/enemy1_mini_2.png').convert_alpha()
enemy1_mini_2_damaged1_img = pygame.image.load('assets/images/enemy1_mini_2_damaged_1.png').convert_alpha()
enemy1_mini_2_damaged2_img = pygame.image.load('assets/images/enemy1_mini_2_damaged_2.png').convert_alpha()
enemy1_mini_2_damaged3_img = pygame.image.load('assets/images/enemy1_mini_2_damaged_3.png').convert_alpha()
enemy1_mini_2_damaged4_img = pygame.image.load('assets/images/enemy1_mini_2_damaged_4.png').convert_alpha()
enemy2_img = pygame.image.load('assets/images/enemy2_ship.png').convert_alpha()
enemy2_damaged1_img = pygame.image.load('assets/images/enemy2_ship_damaged_1.png').convert_alpha()
enemy2_damaged2_img = pygame.image.load('assets/images/enemy2_ship_damaged_2.png').convert_alpha()
enemy2_damaged3_img = pygame.image.load('assets/images/enemy2_ship_damaged_3.png').convert_alpha()
enemy2_damaged4_img = pygame.image.load('assets/images/enemy2_ship_damaged_4.png').convert_alpha()
enemy2_mini_1_img = pygame.image.load('assets/images/enemy2_mini_1.png').convert_alpha()
enemy2_mini1_damaged1_img = pygame.image.load('assets/images/enemy2_mini_1_damaged_1.png').convert_alpha()
enemy2_mini1_damaged2_img = pygame.image.load('assets/images/enemy2_mini_1_damaged_2.png').convert_alpha()
enemy2_mini1_damaged3_img = pygame.image.load('assets/images/enemy2_mini_1_damaged_3.png').convert_alpha()
enemy2_mini1_damaged4_img = pygame.image.load('assets/images/enemy2_mini_1_damaged_4.png').convert_alpha()
enemy2_mini_2_img = pygame.image.load('assets/images/enemy2_mini_2.png').convert_alpha()
enemy2_mini_2_damaged_1_img = pygame.image.load('assets/images/enemy2_mini_2_damaged_1.png').convert_alpha()
enemy2_mini_2_damaged_2_img = pygame.image.load('assets/images/enemy2_mini_2_damaged_2.png').convert_alpha()
enemy2_mini_2_damaged_3_img = pygame.image.load('assets/images/enemy2_mini_2_damaged_3.png').convert_alpha()
enemy2_mini_2_damaged_4_img = pygame.image.load('assets/images/enemy2_mini_2_damaged_4.png').convert_alpha()

enemy_boss_img = pygame.image.load('assets/images/enemy_boss.png').convert_alpha()
enemy_boss_damaged1_img = pygame.image.load('assets/images/enemy_boss_damaged_1.png').convert_alpha()
enemy_boss_damaged2_img = pygame.image.load('assets/images/enemy_boss_damaged_2.png').convert_alpha()
enemy_boss_damaged3_img = pygame.image.load('assets/images/enemy_boss_damaged_3.png').convert_alpha()
enemy_boss_damaged4_img = pygame.image.load('assets/images/enemy_boss_damaged_4.png').convert_alpha()
enemy_boss_mini_1_img = pygame.image.load('assets/images/enemy_boss_mini_1.png').convert_alpha()
enemy_boss_mini_1_damaged1_img = pygame.image.load('assets/images/enemy_boss_mini_1_damaged_1.png').convert_alpha()
enemy_boss_mini_1_damaged2_img = pygame.image.load('assets/images/enemy_boss_mini_1_damaged_2.png').convert_alpha()
enemy_boss_mini_1_damaged3_img = pygame.image.load('assets/images/enemy_boss_mini_1_damaged_3.png').convert_alpha()
enemy_boss_mini_1_damaged4_img = pygame.image.load('assets/images/enemy_boss_mini_1_damaged_4.png').convert_alpha()
enemy_boss_mini_2_img = pygame.image.load('assets/images/enemy_boss_mini_2.png').convert_alpha()
enemy_boss_mini_2_damaged1_img = pygame.image.load('assets/images/enemy_boss_mini_2_damaged_1.png').convert_alpha()
enemy_boss_mini_2_damaged2_img = pygame.image.load('assets/images/enemy_boss_mini_2_damaged_2.png').convert_alpha()
enemy_boss_mini_2_damaged3_img = pygame.image.load('assets/images/enemy_boss_mini_2_damaged_3.png').convert_alpha()
enemy_boss_mini_2_damaged4_img = pygame.image.load('assets/images/enemy_boss_mini_2_damaged_4.png').convert_alpha()

doubleshot_img = pygame.image.load('assets/images/powerup1.png').convert_alpha()
speedup_img = pygame.image.load('assets/images/powerup2.png').convert_alpha()
healup_img = pygame.image.load('assets/images/health_up.png').convert_alpha()
shotgun_img = pygame.image.load('assets/images/shotgun.png').convert_alpha()
powerDown_img = pygame.image.load('assets/images/powerup.png').convert_alpha()


# Load sounds
bullet_snd = pygame.mixer.Sound("assets/sounds/bullet.ogg")
explosion_snd = pygame.mixer.Sound('assets/sounds/explosion.ogg')

# Load music
back_music = pygame.mixer.music.load('assets/music/background_music.ogg')

# Other constants and settings
START = 0
PLAYING = 1
LOSE = 2
WIN = 3

# Game objects
class Ship(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = 10
        self.speed = 9
        self.can_shoot = True
        self.shoots_double = 0
        self.shoots_shotgun = 0
        self.score = 0
        
    def move_right(self):
        self.rect.x += self.speed
        if self.rect.right > WIDTH - 25:
            self.rect.right = WIDTH - 25
            
    def move_left(self):
        self.rect.x -= self.speed
        if self.rect.left <= 25:
            self.rect.left = 25
            
    def move_up(self):
        self.rect.y -= self.speed
        if self.rect.top <= 300:
            self.rect.top = 300
            
    def move_down(self):
        self.rect.y += self.speed
        if self.rect.top >= HEIGHT - 100:
            self.rect.top = HEIGHT - 100
            
    def shoot(self, bullets):
        if self.can_shoot:
            if self.shoots_double:
                x1 = self.rect.left
                x2 = self.rect.right
                y = self.rect.centery
                bullets.add( Bullet(bullet_img, x1, y) )
                bullets.add( Bullet(bullet_img, x2, y) )
            elif self.shoots_shotgun:
                x1 = self.rect.left
                x2 = self.rect.right
                x3 = self.rect.left + 45
                y = self.rect.centery
                bullets.add( Bullet(bullet_img, x1, y) )
                bullets.add( Bullet(bullet_img, x3, y) )
                bullets.add( Bullet(bullet_img, x2, y) )
                print(x3)
            else:
                x = self.rect.centerx
                y = self.rect.top
                bullets.add( Bullet(bullet_img, x, y) )
                
    def update(self, bombs, powerups):
        hits = pygame.sprite.spritecollide(self, bombs, True, pygame.sprite.collide_mask)
        for hit in hits:
            self.shield -=1
            self.shoots_double = 0
            self.shoots_shotgun = 0
            self.speed -= 1
        if self.shield <= 0:
            self.kill()
        if self.shoots_double > 0:
            self.shoots_double -= 1
        elif self.shoots_shotgun > 0:
            self.shoots_shotgun -= 1
        hits = pygame.sprite.spritecollide(self, powerups, True, pygame.sprite.collide_mask)
        for hit in hits:
            hit.apply(self)

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, image, from_x, from_y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = from_x
        self.rect.centery = from_y
        self.speed = 10
        to_x, to_y = pygame.mouse.get_pos()
        dx = from_x - to_x
        dy = from_y - to_y
        hyp = math.sqrt(dx**2 + dy**2)
        self.vx = (dx * self.speed) / hyp
        self.vy = (dy * self.speed) / hyp
        
    def update(self):
        self.rect.x  -= self.vx
        self.rect.y -= self.vy
        if self.rect.bottom < 0:
            self.kill()

class Enemy_1(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 10 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 50)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 2:
            if self.shield == 1:
                self.image = enemy1_ship_damaged_1_img
        elif self.max_health == 3:
            if self.shield == 2:
                self.image = enemy1_ship_damaged_1_img
            elif self.shield == 1:
                self.image = enemy1_ship_damaged_2_img
        elif self.max_health == 4:
            if self.shield == 3:
                self.image = enemy1_ship_damaged_1_img
            elif self.shield == 2:
                self.image = enemy1_ship_damaged_2_img
            elif self.shield == 1:
                self.image = enemy1_ship_damaged_3_img
        elif self.max_health == 5:
            if self.shield == 4:
                self.image = enemy1_ship_damaged_1_img
            elif self.shield == 3:
                self.image = enemy1_ship_damaged_2_img
            elif self.shield == 2:
                self.image = enemy1_ship_damaged_3_img
            elif self.shield == 1:
                self.image = enemy1_ship_damaged_4_img
        elif self.max_health == 6:
            if self.shield == 5:
                self.image = enemy1_ship_damaged_1_img
            elif self.shield == 4:
                self.image = enemy1_ship_damaged_2_img
            elif self.shield == 2:
                self.image = enemy1_ship_damaged_3_img
            elif self.shield == 1:
                self.image = enemy1_ship_damaged_4_img
        elif self.max_health == 7:
            if self.shield == 6:
                self.image = enemy1_ship_damaged_1_img
            elif self.shield == 4:
                self.image = enemy1_ship_damaged_2_img
            elif self.shield == 2:
                self.image = enemy1_ship_damaged_3_img
            elif self.shield == 1:
                self.image = enemy1_ship_damaged_4_img
        
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value
            print(ship.score)
            explosion_snd.play()

class Enemy_1_mini_1(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 10 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 250)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 2:
            if self.shield == 1:
                self.image = enemy1_mini_1_damaged1_img
        elif self.max_health == 3:
            if self.shield == 2:
                self.image = enemy1_mini_1_damaged1_img
            elif self.shield == 1:
                self.image = enemy1_mini_1_damaged2_img
        elif self.max_health == 4:
            if self.shield == 3:
                self.image = enemy1_mini_1_damaged1_img
            elif self.shield == 2:
                self.image = enemy1_mini_1_damaged2_img
            elif self.shield == 1:
                self.image = enemy1_mini_1_damaged3_img
        elif self.max_health == 5:
            if self.shield == 4:
                self.image = enemy1_mini_1_damaged1_img
            elif self.shield == 3:
                self.image = enemy1_mini_1_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_1_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_1_damaged4_img
        elif self.max_health == 6:
            if self.shield == 5:
                self.image = enemy1_mini_1_damaged1_img
            elif self.shield == 4:
                self.image = enemy1_mini_1_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_1_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_1_damaged4_img
        elif self.max_health == 7:
            if self.shield == 6:
                self.image = enemy1_mini_1_damaged1_img
            elif self.shield == 4:
                self.image = enemy1_mini_1_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_1_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_1_damaged4_img
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
           self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value
            print(ship.score)
            explosion_snd.play()

class Enemy_1_mini_2(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 10 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 250)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 2:
            if self.shield == 1:
                self.image = enemy1_mini_2_damaged1_img
        elif self.max_health == 3:
            if self.shield == 2:
                self.image = enemy1_mini_2_damaged1_img
            elif self.shield == 1:
                self.image = enemy1_mini_2_damaged2_img
        elif self.max_health == 4:
            if self.shield == 3:
                self.image = enemy1_mini_2_damaged1_img
            elif self.shield == 2:
                self.image = enemy1_mini_2_damaged2_img
            elif self.shield == 1:
                self.image = enemy1_mini_2_damaged3_img
        elif self.max_health == 5:
            if self.shield == 4:
                self.image = enemy1_mini_2_damaged1_img
            elif self.shield == 3:
                self.image = enemy1_mini_2_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_2_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_2_damaged4_img
        elif self.max_health == 6:
            if self.shield == 5:
                self.image = enemy1_mini_2_damaged1_img
            elif self.shield == 4:
                self.image = enemy1_mini_2_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_2_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_2_damaged4_img
        elif self.max_health == 7:
            if self.shield == 6:
                self.image = enemy1_mini_2_damaged1_img
            elif self.shield == 4:
                self.image = enemy1_mini_2_damaged2_img
            elif self.shield == 2:
                self.image = enemy1_mini_2_damaged3_img
            elif self.shield == 1:
                self.image = enemy1_mini_2_damaged4_img
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
           self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value
            print(ship.score)
            explosion_snd.play()
            
class Enemy_2(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 100)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 2:
            if self.shield == 1:
                self.image = enemy2_damaged1_img
        elif self.max_health == 3:
            if self.shield == 2:
                self.image = enemy2_damaged1_img
            elif self.shield == 1:
                self.image = enemy2_damaged2_img
        elif self.max_health == 4:
            if self.shield == 3:
                self.image = enemy2_damaged1_img
            elif self.shield == 2:
                self.image = enemy2_damaged2_img
            elif self.shield == 1:
                self.image = enemy2_damaged3_img
        elif self.max_health == 5:
            if self.shield == 4:
                self.image = enemy2_damaged1_img
            elif self.shield == 3:
                self.image = enemy2_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_damaged4_img
        elif self.max_health == 6:
            if self.shield == 5:
                self.image = enemy2_damaged1_img
            elif self.shield == 4:
                self.image = enemy2_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_damaged4_img
        elif self.max_health == 7:
            if self.shield == 6:
                self.image = enemy2_damaged1_img
            elif self.shield == 4:
                self.image = enemy2_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_damaged4_img
            
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()
            
class Enemy_2_mini_1(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 100)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 2:
            if self.shield == 1:
                self.image = enemy2_mini1_damaged1_img
        elif self.max_health == 3:
            if self.shield == 2:
                self.image = enemy2_mini1_damaged1_img
            elif self.shield == 1:
                self.image = enemy2_mini1_damaged2_img
        elif self.max_health == 4:
            if self.shield == 3:
                self.image = enemy2_mini1_damaged1_img
            elif self.shield == 2:
                self.image = enemy2_mini1_damaged2_img
            elif self.shield == 1:
                self.image = enemy2_mini1_damaged3_img
        elif self.max_health == 5:
            if self.shield == 4:
                self.image = enemy2_mini1_damaged1_img
            elif self.shield == 3:
                self.image = enemy2_mini1_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_mini1_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_mini1_damaged4_img
        elif self.max_health == 6:
            if self.shield == 5:
                self.image = enemy2_mini1_damaged1_img
            elif self.shield == 4:
                self.image = enemy2_mini1_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_mini1_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_mini1_damaged4_img
        elif self.max_health == 7:
            if self.shield == 6:
                self.image = enemy2_mini1_damaged1_img
            elif self.shield == 4:
                self.image = enemy2_mini1_damaged2_img
            elif self.shield == 2:
                self.image = enemy2_mini1_damaged3_img
            elif self.shield == 1:
                self.image = enemy2_mini1_damaged4_img
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()
            
class Enemy_2_mini_2(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 100)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()

class Enemy_boss(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 1)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 500:
            if self.shield == 400:
                self.image = enemy_boss_damaged1_img
            elif self.shield == 300:
                self.image = enemy_boss_damaged2_img
            elif self.shield == 200:
                self.image = enemy_boss_damaged3_img
            elif self.shield == 100:
                self.image = enemy_boss_damaged4_img
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()

class Enemy_boss_mini_1(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 50)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 9:
            if self.shield == 7:
                self.image = enemy_boss_mini_1_damaged1_img
            elif self.shield == 5:
                self.image = enemy_boss_mini_1_damaged2_img
            elif self.shield == 3:
                self.image = enemy_boss_mini_1_damaged3_img
            elif self.shield == 1:
                self.image = enemy_boss_mini_1_damaged4_img
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()

class Enemy_boss_mini_2(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y, max_health, shield=1):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        self.shield = shield
        self.value = 20 * shield
        self.max_health = max_health
        
    def drop_bomb(self, bombs):
        r = random.randint(0, 75)
        if r == 0:
            x = self.rect.centerx
            y = self.rect.bottom
            bombs.add( Bomb(bullet_img, x, y) )
            
    def set_image(self):
        if self.max_health == 7:
            if self.shield == 6:
                self.image = enemy_boss_mini_2_damaged1_img
            elif self.shield == 4:
                self.image = enemy_boss_mini_2_damaged2_img
            elif self.shield == 2:
                self.image = enemy_boss_mini_2_damaged3_img
            elif self.shield == 1:
                self.image = enemy_boss_mini_2_damaged4_img
                
                
    def update(self, bullets, ship, bombs):
        self.drop_bomb(bombs)
        self.set_image()
        hits = pygame.sprite.spritecollide(self, bullets, True, pygame.sprite.collide_mask)
        for hits in hits:
            self.shield -=1
        if self.shield <= 0:
            self.kill()
            ship.score += self.value 
            print(ship.score)
            explosion_snd.play()
            
class Bomb(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        
    def update(self):
        self.rect.y  += 6
        if self.rect.top > HEIGHT:
            self.kill()
            
class Fleet(pygame.sprite.Group):
    
    def __init__(self):
        super().__init__()
        self.speed = 3
        self.left_boundary = 0
        self.right_boundary = WIDTH
        
    def move(self):
        hits_edge = False
        for enemy in self.sprites():
            enemy.rect.x += self.speed
            if enemy.rect.left < self.left_boundary or enemy.rect.right > self.right_boundary:
                hits_edge = True
        if hits_edge:
            self.speed *= -1
            
    def update(self, bullets, ship, bombs):
        super().update(bullets, ship, bombs)
        self.move()

class DoubleShot(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        
    def apply(self, ship):
        ship.shoots_double = 500
        ship.speed = ship.speed
        ship.score += 300
        
    def update(self):
        self.rect.y  += 6
        if self.rect.top > HEIGHT:
            self.kill()
            
class Shotgun(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        
    def apply(self, ship):
        ship.shoots_shotgun = 250
        ship.speed = ship.speed
        ship.score += 450
        
    def update(self):
        self.rect.y  += 2
        if self.rect.top > HEIGHT:
            self.kill()
            
class SpeedUp(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y

    def apply(self, ship):
        ship.speed = 10
        ship.score += 250

    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.kill()

class HealUp(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        
    def apply(self, ship):
        ship.shield += 3
        ship.score += 100
        
    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.kill()

class HealDown(pygame.sprite.Sprite):
    
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.centerx = x
        self.rect.centery = y
        
    def apply(self, ship):
        ship.shield = 1
        ship.score -= 200
        
    def update(self):
        self.rect.y += 5
        if self.rect.top > HEIGHT:
            self.kill()

# Main game class
class Game:

    def __init__(self):
        self.running = True
        self.new_game()

    def new_game(self):
        self.player = pygame.sprite.Group()
        self.ship = Ship(ship_img, 400, 500)
        self.player.add(self.ship)
        self.enemies = Fleet()
        self.bullets = pygame.sprite.Group()
        self.bombs = pygame.sprite.Group()
        self.powerups = pygame.sprite.Group()
        self.stage = START
        self.level = 1
        self.start_level()

    def start_level(self):
        if self.level == 1:
            e1 = Enemy_1(enemy1_img, 150, 250, 2, 2)
            e2 = Enemy_1(enemy1_img, 350, 150, 2, 2)
            e3 = Enemy_2(enemy2_img, 650, 250, 2, 2)
            e4 = Enemy_2(enemy2_img, 850, 150, 2, 2)
            self.enemies.add(e1, e2, e3, e4)
        elif self.level == 2:
            e1 = Enemy_1(enemy1_img, 150, 250, 3, 3)
            e2 = Enemy_1(enemy1_img, 350, 150, 3, 3)
            e3 = Enemy_2(enemy2_img, 650, 250, 2, 2)
            e4 = Enemy_2(enemy2_img, 850, 150, 2, 2)
            e5 = Enemy_1_mini_1(enemy1_mini_1_img, 100, 175, 2, 2)
            e6 = Enemy_1_mini_1(enemy1_mini_1_img, 200, 175, 2, 2)
            e7 = Enemy_1_mini_1(enemy1_mini_1_img, 300, 75, 2, 2)
            e8 = Enemy_1_mini_1(enemy1_mini_1_img, 400, 75, 2, 2)
            e9 = Enemy_2_mini_1(enemy2_mini_1_img, 600, 175, 1, 1)
            e10 = Enemy_2_mini_1(enemy2_mini_1_img, 700, 175, 1, 1)
            e11 = Enemy_2_mini_1(enemy2_mini_1_img, 800, 75, 1, 1)
            e12 = Enemy_2_mini_1(enemy2_mini_1_img, 900, 75, 1, 1)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12)
        elif self.level == 3:
            e1 = Enemy_1(enemy1_img, 150, 250, 4, 4)
            e2 = Enemy_1(enemy1_img, 350, 150, 4, 4)
            e3 = Enemy_2(enemy2_img, 650, 250, 3, 3)
            e4 = Enemy_2(enemy2_img, 850, 150, 3, 3)
            e5 = Enemy_1_mini_1(enemy1_mini_1_img, 100, 175, 3, 3)
            e6 = Enemy_1_mini_1(enemy1_mini_1_img, 200, 175, 3, 3)
            e7 = Enemy_1_mini_1(enemy1_mini_1_img, 300, 75, 3, 3)
            e8 = Enemy_1_mini_1(enemy1_mini_1_img, 400, 75, 3, 3)
            e9 = Enemy_2_mini_1(enemy2_mini_1_img, 600, 175, 2, 2)
            e10 = Enemy_2_mini_1(enemy2_mini_1_img, 700, 175, 2, 2)
            e11 = Enemy_2_mini_1(enemy2_mini_1_img, 800, 75, 2, 2)
            e12 = Enemy_2_mini_1(enemy2_mini_1_img, 900, 75, 2, 2)
            e13 = Enemy_2_mini_2(enemy2_mini_2_img, 600, 325, 1, 1)
            e14 = Enemy_2_mini_2(enemy2_mini_2_img, 700, 325, 1, 1)
            e15 = Enemy_2_mini_2(enemy2_mini_2_img, 800, 225, 1, 1)
            e16 = Enemy_2_mini_2(enemy2_mini_2_img, 900, 225, 1, 1)
            e17 = Enemy_1_mini_2(enemy1_mini_2_img, 100, 325, 2, 2)
            e18 = Enemy_1_mini_2(enemy1_mini_2_img, 200, 325, 2, 2)
            e19 = Enemy_1_mini_2(enemy1_mini_2_img, 300, 225, 2, 2)
            e20 = Enemy_1_mini_2(enemy1_mini_2_img, 400, 225, 2, 2)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20)
        elif self.level == 4:
            p4 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
            self.powerups.add(p4)
            e1 = Enemy_1(enemy1_img, 150, 250, 5, 5)
            e2 = Enemy_1(enemy1_img, 350, 150, 5, 5)
            e3 = Enemy_2(enemy2_img, 650, 250, 4, 4)
            e4 = Enemy_2(enemy2_img, 850, 150, 4, 4)
            e5 = Enemy_1_mini_1(enemy1_mini_1_img, 100, 175, 4, 4)
            e6 = Enemy_1_mini_1(enemy1_mini_1_img, 200, 175, 4, 4)
            e7 = Enemy_1_mini_1(enemy1_mini_1_img, 300, 75, 4, 4)
            e8 = Enemy_1_mini_1(enemy1_mini_1_img, 400, 75, 4, 4)
            e9 = Enemy_2_mini_1(enemy2_mini_1_img, 600, 175, 3, 3)
            e10 = Enemy_2_mini_1(enemy2_mini_1_img, 700, 175, 3, 3)
            e11 = Enemy_2_mini_1(enemy2_mini_1_img, 800, 75, 3, 3)
            e12 = Enemy_2_mini_1(enemy2_mini_1_img, 900, 75, 3, 3)
            e13 = Enemy_2_mini_2(enemy2_mini_2_img, 600, 325, 2, 2)
            e14 = Enemy_2_mini_2(enemy2_mini_2_img, 700, 325, 2, 2)
            e15 = Enemy_2_mini_2(enemy2_mini_2_img, 800, 225, 2, 2)
            e16 = Enemy_2_mini_2(enemy2_mini_2_img, 900, 225, 2, 2)
            e17 = Enemy_1_mini_2(enemy1_mini_2_img, 100, 325, 3, 3)
            e18 = Enemy_1_mini_2(enemy1_mini_2_img, 200, 325, 3, 3)
            e19 = Enemy_1_mini_2(enemy1_mini_2_img, 300, 225, 3, 3)
            e20 = Enemy_1_mini_2(enemy1_mini_2_img, 400, 225, 3, 3)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20)
        elif self.level == 5:
            e1 = Enemy_1(enemy1_img, 150, 300, 6, 6)
            e2 = Enemy_1(enemy1_img, 250, 300, 6, 6)
            e3 = Enemy_1(enemy1_img, 350, 300, 6, 6)
            e4 = Enemy_1(enemy1_img, 450, 300, 6, 6)
            e5 = Enemy_1(enemy1_img, 300, 200, 6, 6)
            e6 = Enemy_2(enemy2_img, 1050, 300, 5, 5)
            e7 = Enemy_2(enemy2_img, 950, 300, 5, 5)
            e8 = Enemy_2(enemy2_img, 850, 300, 5, 5)
            e9 = Enemy_2(enemy2_img, 750, 300, 5, 5)
            e10 = Enemy_2(enemy2_img, 900, 200, 5, 5)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10)
        elif self.level == 6:
            p4 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
            self.powerups.add(p4)
            e1 = Enemy_1(enemy1_img, 150, 300, 6, 6)
            e2 = Enemy_1(enemy1_img, 250, 300, 6, 6)
            e3 = Enemy_1(enemy1_img, 350, 300, 6, 6)
            e4 = Enemy_1(enemy1_img, 450, 300, 6, 6)
            e5 = Enemy_1(enemy1_img, 300, 200, 6, 6)
            e6 = Enemy_1_mini_1(enemy1_mini_1_img, 200, 200, 4, 4)
            e7 = Enemy_1_mini_1(enemy1_mini_1_img, 400, 200, 4, 4)
            e8 = Enemy_1_mini_1(enemy1_mini_1_img, 100, 200, 4, 4)
            e9 = Enemy_1_mini_1(enemy1_mini_1_img, 500, 200, 4, 4)
            e10 = Enemy_1_mini_2(enemy1_mini_2_img, 150, 100, 2, 2)
            e11 = Enemy_1_mini_2(enemy1_mini_2_img, 250, 100, 2, 2)
            e12 = Enemy_1_mini_2(enemy1_mini_2_img, 350, 100, 2, 2)
            e13 = Enemy_1_mini_2(enemy1_mini_2_img, 450, 100, 2, 2)
            e14 = Enemy_2(enemy2_img, 1050, 300, 5, 5)
            e15 = Enemy_2(enemy2_img, 950, 300, 5, 5)
            e16 = Enemy_2(enemy2_img, 850, 300, 5, 5)
            e17 = Enemy_2(enemy2_img, 750, 300, 5, 5)
            e18 = Enemy_2(enemy2_img, 900, 200, 5, 5)
            e19 = Enemy_2_mini_1(enemy2_mini_1_img, 1000, 200, 3, 3)
            e20 = Enemy_2_mini_1(enemy2_mini_1_img, 1100, 200, 3, 3)
            e21 = Enemy_2_mini_1(enemy2_mini_1_img, 800, 200, 3, 3)
            e22 = Enemy_2_mini_1(enemy2_mini_1_img, 700, 200, 3, 3)
            e23 = Enemy_2_mini_2(enemy2_mini_2_img, 1050, 100, 1, 1)
            e23 = Enemy_2_mini_2(enemy2_mini_2_img, 950, 100, 1, 1)
            e23 = Enemy_2_mini_2(enemy2_mini_2_img, 850, 100, 1, 1)
            e23 = Enemy_2_mini_2(enemy2_mini_2_img, 750, 100, 1, 1)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21, e22, e23)
        elif self.level == 7:
            e1 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 200, 9, 9)
            e2 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 200, 9, 9)
            e3 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 200, 9, 9)
            e4 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 200, 9, 9)
            e5 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 200, 9, 9)
            e6 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 100, 9, 9)
            e7 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 100, 9, 9)
            e8 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 100, 9, 9)
            e9 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 100, 9, 9)
            e10 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 100, 9, 9)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10)
        elif self.level == 8:
            p4 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
            self.powerups.add(p4)
            e1 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 200, 9, 9)
            e2 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 200, 9, 9)
            e3 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 200, 9, 9)
            e4 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 200, 9, 9)
            e5 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 200, 9, 9)
            e6 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 100, 9, 9)
            e7 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 100, 9, 9)
            e8 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 100, 9, 9)
            e9 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 100, 9, 9)
            e10 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 100, 9, 9)
            e11 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 1050, 200, 7, 7)
            e12 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 950, 200, 7, 7)
            e13 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 850, 200, 7, 7)
            e14 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 750, 200, 7, 7)
            e15 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 650, 100, 7, 7)
            e16 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 1050, 100, 7, 7)
            e17 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 950, 100, 7, 7)
            e18 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 850, 100, 7, 7)
            e19 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 750, 100, 7, 7)
            e20 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 650, 200, 7, 7)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20)
        elif self.level == 9:
            p4 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-1500, -1000))
            p5 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-4000, -2000))
            p6 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-6000, -4500))
            p7 = Shotgun(shotgun_img, random.randrange(100, 1000), random.randrange(-8000, -6500))
            p8 = HealUp(healup_img, random.randrange(100, 1000), random.randrange(-1500, -1000))
            p9 = HealUp(healup_img, random.randrange(100, 1000), random.randrange(-4000, -2000))
            p10 = HealUp(healup_img, random.randrange(100, 1000), random.randrange(-6000, -4500))
            p11 = HealUp(healup_img, random.randrange(100, 1000), random.randrange(-8000, -6500))
            p12 = DoubleShot(doubleshot_img, random.randrange(100, 1000), random.randrange(-1500, -1000))
            p13 = DoubleShot(doubleshot_img, random.randrange(100, 1000), random.randrange(-4000, -2000))
            p14 = DoubleShot(doubleshot_img, random.randrange(100, 1000), random.randrange(-6000, -4500))
            p15 = DoubleShot(doubleshot_img, random.randrange(100, 1000), random.randrange(-8000, -6500))
            p16 = SpeedUp(speedup_img, random.randrange(100, 1000), random.randrange(-1500, -1000))
            p17 = SpeedUp(speedup_img, random.randrange(100, 1000), random.randrange(-4000, -2000))
            p18 = SpeedUp(speedup_img, random.randrange(100, 1000), random.randrange(-6000, -4500))
            p19 = SpeedUp(speedup_img, random.randrange(100, 1000), random.randrange(-8000, -6500))
            
            self.powerups.add(p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19)
            
            e1 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 200, 9, 9)
            e2 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 200, 9, 9)
            e3 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 200, 9, 9)
            e4 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 200, 9, 9)
            e5 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 200, 9, 9)
            e6 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 50, 100, 9, 9)
            e7 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 150, 100, 9, 9)
            e8 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 250, 100, 9, 9)
            e9 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 350, 100, 9, 9)
            e10 = Enemy_boss_mini_1(enemy_boss_mini_1_img, 450, 100, 9, 9)
            e11 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 1050, 200, 7, 7)
            e12 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 950, 200, 7, 7)
            e13 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 850, 200, 7, 7)
            e14 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 750, 200, 7, 7)
            e15 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 650, 100, 7, 7)
            e16 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 1050, 100, 7, 7)
            e17 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 950, 100, 7, 7)
            e18 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 850, 100, 7, 7)
            e19 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 750, 100, 7, 7)
            e20 = Enemy_boss_mini_2(enemy_boss_mini_2_img, 650, 200, 7, 7)
            e21 = Enemy_boss(enemy_boss_img, 550, 150, 500, 500)
            self.enemies.add(e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15, e16, e17, e18, e19, e20, e21)

        p1 = DoubleShot(doubleshot_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
        p2 = HealUp(healup_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
        p3 = SpeedUp(speedup_img, random.randrange(100, 1000), random.randrange(-2000, -1000))
        self.powerups.add(p1, p2, p3)


    def show_title_screen(self):
        screen.blit(start_img, (0, 0))
    def show_lose_screen(self):
        screen.blit(end_img, (0, 0))
    def show_win_screen(self):
        screen.blit(win_img, (0, 0))
    def show_hud(self):
        text = FONT_SM.render('Score: ' + str(self.ship.score), True, WHITE)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = 16
        screen.blit(text, rect)
        text = FONT_SM.render('Level: ' + str(self.level), True, WHITE)
        rect = text.get_rect()
        rect.right = WIDTH - 16
        rect.bottom = HEIGHT
        screen.blit(text, rect)

        text = FONT_SM.render('Health: ' + str(self.ship.shield), True, WHITE)
        rect = text.get_rect()
        rect.left = 16
        rect.bottom = HEIGHT - 16
        screen.blit(text, rect)
       

    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if self.stage == START:
                    self.stage = PLAYING
                    pygame.mixer.music.play(-1)
                elif self.stage == LOSE:
                    if event.key == pygame.K_r:
                        self.new_game()
                        pygame.mixer.music.stop()
                elif self.stage == WIN:
                    if event.key == pygame.K_r:
                        self.new_game()
                        pygame.mixer.music.stop()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.stage == PLAYING:
                    self.ship.shoot(self.bullets)
                    bullet_snd.play()

        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_RIGHT] and pressed[pygame.K_LEFT]:
            self.ship.move_right()
            self.ship.move_left()
        elif pressed[pygame.K_RIGHT] and pressed[pygame.K_UP]:
            self.ship.move_right()
            self.ship.move_up()
        elif pressed[pygame.K_LEFT] and pressed[pygame.K_UP]:
            self.ship.move_left()
            self.ship.move_up()
        elif pressed[pygame.K_LEFT] and pressed[pygame.K_DOWN]:
            self.ship.move_left()
            self.ship.move_down()
        elif pressed[pygame.K_RIGHT] and pressed[pygame.K_DOWN]:
            self.ship.move_right()
            self.ship.move_down()
        elif pressed[pygame.K_w] and pressed[pygame.K_d]:
            self.ship.move_up()
            self.ship.move_right()
        elif pressed[pygame.K_w] and pressed[pygame.K_a]:
            self.ship.move_up()
            self.ship.move_left()
        elif pressed[pygame.K_s] and pressed[pygame.K_a]:
            self.ship.move_down()
            self.ship.move_left()
        elif pressed[pygame.K_s] and pressed[pygame.K_d]:
            self.ship.move_down()
            self.ship.move_right()
        elif pressed[pygame.K_w]:
            self.ship.move_up()
        elif pressed[pygame.K_a]:
            self.ship.move_left()
        elif pressed[pygame.K_s]:
            self.ship.move_down()
        elif pressed[pygame.K_d]:
            self.ship.move_right()
        elif pressed[pygame.K_RIGHT]:
            self.ship.move_right()
        elif pressed[pygame.K_LEFT]:
            self.ship.move_left()
        elif pressed[pygame.K_UP]:
            self.ship.move_up()
        elif pressed[pygame.K_DOWN]:
            self.ship.move_down()


    def update(self):
        if self.stage != START:
            self.bullets.update()
            self.bombs.update()
            self.powerups.update()
            self.enemies.update(self.bullets, self.ship, self.bombs)
            self.player.update(self.bombs, self.powerups)

        if len(self.player) == 0:
            self.stage = LOSE
        elif len(self.enemies) == 0:
            if self.level < 9:
                self.level += 1
                self.start_level()
            else:
                self.stage = WIN

   
    def render(self):
        screen.blit(background, (0, 0))
        self.player.draw(screen)
        self.bullets.draw(screen)
        self.bombs.draw(screen)
        self.powerups.draw(screen)
        self.enemies.draw(screen)

        self.show_hud()
       
        if self.stage == START:
            self.show_title_screen()
        if self.stage == LOSE:
            self.show_lose_screen()
        if self.stage == WIN:
            self.show_win_screen()

       
    def play(self):
        while self.running:
            self.process_input()    
            self.update()    
            self.render()
           
            pygame.display.update()
            clock.tick(FPS)


# Let's do this!
if __name__ == "__main__":
   g = Game()
   g.play()
   pygame.quit() 
