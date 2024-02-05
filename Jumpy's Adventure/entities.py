from re import I
import pygame, random, math
from settings import *


# Game objects
class Entity(pygame.sprite.Sprite):

    def __init__(self, game, image, loc=[0, 0]):
        super().__init__()
        self.image = image
        self.game = game
        self.rect = self.image.get_rect()
        self.move_to(loc)
        self.on_platform = False
        
    def move_to(self, loc):
        self.rect.centerx = loc[0] * GRID_SIZE + GRID_SIZE // 2
        self.rect.centery = loc[1] * GRID_SIZE + GRID_SIZE // 2
        
    def apply_gravity(self):
        self.vy += self.game.gravity

    def reverse(self):
        self.vx *= -1

    def move(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

    def move_and_check_platforms(self):
        self.rect.y += self.vy
        self.on_platform = False

        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for platform in hits:
            if self.vy < 0:
                self.rect.top = platform.rect.bottom
            elif self.vy > 0:
                self.rect.bottom = platform.rect.top
                self.on_platform = True
        if len(hits) > 0:
            self.vy = 0
        self.rect.x += self.vx
        
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        for platform in hits:
            if self.vx < 0:
                self.rect.left = platform.rect.right
            elif self.vx > 0:
                self.rect.right = platform.rect.left
        if len(hits) > 0:
            self.reverse()

    def check_platform_edges(self):
        self.rect.y += 2
        hits = pygame.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        at_edge = True
        for platform in hits:
            if self.vx < 0:
                if self.rect.left >= platform.rect.left:
                    at_edge = False
            elif self.vx > 0:
                if self.rect.right <= platform.rect.right:
                    at_edge = False
        if at_edge:
            self.reverse()

    def check_world_edges(self):
        if self.rect.left <= 0:
            if self.name == "bullet":
                self.kill()
            else:
                if self.game.background_img == background_cave_img:
                    self.rect.left = 0
                    self.reverse()
                elif self.name == "player" and self.game.level > 2:
                    if 1428 < self.rect.centery < 2128 and self.game.level == 3:
                        self.at_end = True
                    else:
                        self.at_beginning = True
                    self.game.advance()
                else:
                    self.rect.left = 0
                    self.reverse()
        elif self.rect.right > self.game.world_width:
            if self.name == "bullet":
                self.kill()
            elif self.game.background_img == background_cave_img:
                self.rect.right = self.game.world_width
                self.reverse()
            elif self.name == "player":
                self.at_end = True
                self.game.advance()
            else:
                self.rect.right = self.game.world_width
                self.reverse()
        else:
            if self.name == "player":
                self.at_end = False
                self.at_beginning = False
        if self.rect.top > self.game.world_height:
            self.health = 0
        
        

class AnimatedEntity(Entity):
    def __init__(self, game, images, loc=[0, 0]):
        super().__init__(game, images[0], loc)
        self.images = images
        self.image_index = 0
        self.ticks = 0
        self.animation_speed = 7
        
    def set_image_list(self):
        self.images = self.images
        
    def animate(self):
        self.set_image_list()
        self.ticks += 1
        if self.ticks % self.animation_speed == 0:
            if self.image_index >= len(self.images):
                self.image_index = 0
            self.image = self.images[self.image_index]
            self.image_index += 1

# ---------- PLAYER ---------- #

class Player(AnimatedEntity):
    def __init__(self, game, images):
        super().__init__(game, images)
        self.vx = 0
        self.vy = 0
        self.speed = 4
        self.power = 1
        self.jump_power = 19
        self.score = 0
        self.health = 4
        self.numofcoins = 0
        self.jumps_remaining = 2
        self.name = "player"
        self.loc = [0, 0]
        
        self.image_index = 0
        self.bullet_count = 10
        self.escape_time = 0
        self.keys = []
        
        self.on_platform = False
        self.facing_right = True
        self.jumping = False
        self.flying = False
        self.has_gun = False
        self.has_gun_equipped = False
        self.on_ladder = False
        self.has_torch = False
        self.has_torch_equipped = False
        self.has_wings = False
        self.at_end = False
        self.at_beginning = False
        self.restarting = False
        
    def move_left(self):
        self.vx = -self.speed
        self.facing_right = False
        if self.on_platform:
            self.jumps_remaining = 2
        
    def move_right(self):
        self.vx = self.speed
        self.facing_right = True
        if self.on_platform:
            self.jumps_remaining = 2
        
    def jump(self):
        self.jumping = True
        if self.on_platform:
            self.game.create_checkpoint()
            self.vy = 0
            self.vy -= 1 * self.jump_power
        elif self.has_wings and not self.on_platform and self.jumps_remaining > 0:
            self.jumps_remaining -= 1
            self.vy = 0
            self.vy -= 1 * self.jump_power
    
    def shoot(self):
        if self.has_gun and self.has_gun_equipped and self.bullet_count >= 1:
            image = player_bullet_img
            if self.facing_right:
                x = self.rect.right
                y = self.rect.centery + 12
                direction = 1
            else:
                x = self.rect.left
                y = self.rect.centery + 12
                direction = -1
            loc = [x / 64, y / 64]
            b = Bullet(self.game, image, loc, direction, x, y)
            self.game.player_bullets.add(b)
            self.game.all_sprites.add(b)
            gun_snd.play()
            self.bullet_count -= 1
        
    def stop(self):
        self.vx = 0
        if not self.restarting:
            self.image_index = 0
        self.jumping = False
        if self.on_platform:
            self.jumps_remaining = 2

    def is_alive(self):
        return self.health > 0
    
    def figure_loc(self):
        x = self.rect.right
        y = self.rect.top
        self.loc = [x / 64, y / 64]

        if self.game.has_mouse:
            mx, my = pygame.mouse.get_pos()
            offset_x, offset_y = self.game.get_offsets()
            if mx > self.rect.centerx - offset_x:
                self.facing_right = True
            else:
                self.facing_right = False

    def reached_goal(self):
        hits = pygame.sprite.spritecollide(self, self.game.goals, False)
        return len(hits) > 0
    
    def check_stuff(self):
        """"
        hits = pygame.sprite.spritecollide(self, self.game.moveables, False)
        for moveable in hits:
            if self.rect.right == moveable.rect.left:
                moveable.rectx += 2
            elif self.rect.left == moveable.rect.right:
                moveable.rectx -= 1
        """
        
        hits = pygame.sprite.spritecollide(self, self.game.items, False)
        for item in hits:
            item.interact()
        
        hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
        for block in hits:
            block.interact()

        hits = pygame.sprite.spritecollide(self, self.game.messages, False)
        for message in hits:
            message.interact()
        
        hits = pygame.sprite.spritecollide(self, self.game.bridges, False)
        for bridge in hits:
            self.rect.x = bridge.vx
        
        if self.game.level == 2 or self.game.level == 3:
            hits = pygame.sprite.spritecollide(self, self.game.interactables, False)
            if hits:
                self.game.showing_spacebar = True
            else:
                self.game.showing_spacebar = False
        
        hits = pygame.sprite.spritecollide(self, self.game.death_blocks, False)
        for block in hits:
            block.apply()
        
        hits = pygame.sprite.spritecollide(self, self.game.ladders, False)
        if hits:
            self.on_ladder = True
        else:
            self.on_ladder = False
        
        hits = pygame.sprite.spritecollide(self, self.game.floating_bridge, False)
        for floating_bridge in hits:
            self.rect.x += floating_bridge.vx
            if self.vy < 0:
                self.rect.top = floating_bridge.rect.bottom
            elif self.vy > 0:
                self.rect.bottom = floating_bridge.rect.top
                self.on_platform = True
        if len(hits) > 0:
            self.vy = 0
                
        hits = pygame.sprite.spritecollide(self, self.game.floating_bridge, False)
        for floating_bridge in hits:
            if self.vx < 0:
                self.rect.left = floating_bridge.rect.right
            elif self.vx > 0:
                self.rect.right = floating_bridge.rect.left
        
    def check_enemies(self):
        if self.escape_time == 0:
            hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
            for enemy in hits:
                if enemy.is_alive:
                    if self.vy > 1:
                        if enemy.name == "boss" or enemy.name == "gear":
                            pass
                        else:
                            enemy.is_alive = False
                    else:
                        if self.facing_right and enemy.facing_right and self.rect.x > enemy.rect.x:
                            self.vx += 80
                            self.rect.y -= 32
                        elif self.facing_right and enemy.facing_right and self.rect.x < enemy.rect.x:
                            self.vx -= 80
                            self.rect.y -= 32
                        elif not self.facing_right and enemy.facing_left and self.rect.x > enemy.rect.x:
                            self.vx += 80
                            self.rect.y -= 32
                        elif not self.facing_right and enemy.facing_left and self.rect.x < enemy.rect.x:
                            self.vx -= 80
                            self.rect.y -= 32
                        elif self.facing_right and enemy.facing_left:
                            self.vx -= 80
                            self.rect.y -= 32
                        elif not self.facing_right and enemy.facing_right:
                            self.vx += 80
                            self.rect.y -= 32
                        self.health -= 1
                        self.escape_time = 30
        if self.escape_time > 0:
            self.escape_time -= 1

    def hitting_message(self):
        hits = pygame.sprite.spritecollide(self, self.game.messages, False)
        return len(hits) > 0

    def set_image_list(self):
#        if self.restarting:
#            self.animation_speed = 5
#            self.images = player_restarting_imgs
#            self.vx = 0
#            if self.image_index >= len(self.images):
#                self.restarting = False
#                self.facing_right = True
        if self.facing_right and not self.has_gun_equipped and not self.has_torch_equipped and not self.has_wings:
            if not self.on_platform:
                self.images = player_jump_rt_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_imgs
            else:
                self.images = player_idle_rt_img
        elif not self.facing_right and not self.has_gun_equipped and not self.has_torch_equipped and not self.has_wings:
            if not self.on_platform:
                self.images = player_jump_lt_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_imgs
            else:
                self.images = player_idle_lt_img
        elif self.facing_right and self.has_torch_equipped and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_rt_torch_and_wings_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_torch_and_wings_imgs
            else:
                self.images = player_idle_rt_torch_and_wings_imgs
        elif not self.facing_right and self.has_torch_equipped and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_lt_torch_and_wings_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_torch_and_wings_imgs
            else:
                self.images = player_idle_lt_torch_and_wings_img
        elif self.facing_right and self.has_gun_equipped and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_rt_gun_and_wings_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_gun_and_wings_imgs
            else:
                self.images = player_idle_rt_gun_and_wings_imgs
        elif not self.facing_right and self.has_gun_equipped and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_lt_gun_and_wings_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_gun_and_wings_imgs
            else:
                self.images = player_idle_lt_gun_and_wings_img
        elif self.facing_right and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_rt_wings_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_wings_imgs
            else:
                self.images = player_idle_rt_wings_img
        elif not self.facing_right and self.has_wings:
            if not self.on_platform:
                self.images = player_jump_lt_wings_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_wings_imgs
            else:
                self.images = player_idle_lt_wings_img
        elif self.facing_right and self.has_gun_equipped:
            if not self.on_platform:
                self.images = player_jump_rt_gun_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_gun_imgs
            else:
                self.images = player_idle_rt_gun_img
        elif not self.facing_right and self.has_gun_equipped:
            if not self.on_platform:
                self.images = player_jump_lt_gun_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_gun_imgs
            else:
                self.images = player_idle_lt_gun_img
        elif self.facing_right and self.has_torch_equipped:
            if not self.on_platform:
                self.images = player_jump_rt_torch_imgs
            elif self.vx > 0:
                self.images = player_walk_rt_torch_imgs
            else:
                self.images = player_idle_rt_torch_img
        elif not self.facing_right and self.has_torch_equipped:
            if not self.on_platform:
                self.images = player_jump_lt_torch_imgs
            elif self.vx < 0:
                self.images = player_walk_lt_torch_imgs
            else:
                self.images = player_idle_lt_torch_img
        if not self.restarting:
            self.animation_speed = 7
        
    def update(self):
        if not self.on_ladder:
            self.apply_gravity()
        self.check_enemies()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.check_stuff()
        self.animate()
        self.figure_loc()
        if self.game.has_mouse and False:
            print("Working.. Kind of.")
            from_x = self.rect.centerx 
            from_y = self.rect.centery 
            to_x, to_y = pygame.mouse.get_pos()
            offset_x, offset_y = self.game.get_offsets()
            dx = from_x - to_x - offset_x
            dy = from_y - to_y - offset_y
            hyp = math.sqrt(dx**2 + dy**2)
            self.vx = (dx * self.speed) / hyp
            self.vy = (dy * self.speed) / hyp
            angle = math.degrees(math.atan2(dy, dx))
            self.image = pygame.transform.rotate(self.image, -angle + 180)

# ---------- ENEMIES ---------- #

class Enemy(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.facing_left = False
        self.facing_right = False
        self.should_show_popup = False
        self.death_counter = 15
        self.is_alive = True
        self.category = "enemy"
        self.shot = False
        self.counter = 25
        self.should_stall = False
    
    def live(self):
        if self.health <= 0:
            self.is_alive = False
    
    def move(self):
        if self.vx < 0:
            self.facing_left = True
            self.facing_right = False
        elif self.vx > 0:
            self.facing_left = False
            self.facing_right = True
        if self.name == "bat" or self.name == "bee":
            if self.rect.left < self.min_x or self.rect.right > self.max_x:
                self.reverse()
    
    def stall(self):
        hits = pygame.sprite.spritecollide(self, self.game.player, False)
        if len(hits) > 0 and self.game.hero.vy == 0:
            self.should_stall = True
        if self.should_stall:
            self.counter -= 1
            if self.counter > 0:
                self.vx = 0
            else:
                if self.game.hero.rect.centerx > self.rect.centerx:
                    if self.name == "spider":
                        pass
                    else:
                        self.vx = 2
                elif self.game.hero.rect.centerx < self.rect.centerx:
                    if self.name == "spider":
                        pass
                    else:
                        self.vx = -2
                self.counter = 50
                self.should_stall = False

    def update(self):
        if not self.is_alive:
            if self.death_counter > 0:
                self.death_counter -= 1
                self.vx = 0
            else:
                self.kill()
        self.live()
        self.move_and_check_platforms()
        self.check_world_edges()
        self.animate()
        self.move()
        self.stall()

class Bat(Enemy):
    def __init__(self, game, image, loc, min_x, max_x):
        super().__init__(game, image, loc)
        self.vx = -1 * 2
        self.vy = 0
        self.health = 1
        self.score = 1
        self.flying = True
        self.min_x = min_x
        self.max_x = max_x
        self.name = "bat"
    
    def set_image_list(self):
        if self.is_alive:
            if self.vx < 0:
                self.images = bat_imgs_lt
            else:
                self.images = bat_imgs_rt
        else:
            if self.shot:
                self.images = shot_imgs
            else:
                self.images = bat_imgs_dead

class Bee(Enemy):
    def __init__(self, game, image, loc, min_x, max_x):
        super().__init__(game, image, loc)
        self.vx = -1 * 2
        self.vy = 0
        self.health = 1
        self.score = 1
        self.flying = True
        self.min_x = min_x
        self.max_x = max_x
        self.name = "bee"
    
    def set_image_list(self):
        if self.is_alive:
            if self.vx < 0:
                self.images = bee_imgs_lt
            else:
                self.images = bee_imgs_rt
        else:
            if self.shot:
                self.images = shot_imgs
            else:
                self.images = bee_imgs_dead

class Slime(Enemy):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = -1 * 2
        self.vy = 0
        self.health = 1
        self.score = 1
        self.flying = False
        self.name = "slime"

    def set_image_list(self):
        if self.is_alive:
            if self.vx < 0:
                self.images = slime1_imgs_lt
            else:
                self.images = slime1_imgs_rt
        else:
            if self.shot:
                self.images = shot_imgs
            else:
                self.images = slime_imgs_dead

    def update(self):
        super().update()
        self.apply_gravity()
        self.check_platform_edges()

class Spider(Enemy):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = -1 * 1
        self.vy = 0
        self.health = 4
        self.score = 2
        self.flying = False
        self.name = "boss_spider"

    def set_image_list(self):
        if self.is_alive:
            if self.vx < 0:
                self.images = spider_imgs_lt
            else:
                self.images = spider_imgs_rt
        else:
            if self.shot:
                self.images = shot_big_imgs
            else:
                self.images = spider_imgs_dead
    
    def find_player(self):
        distancex = self.game.hero.rect.centerx - self.rect.centerx
        distancey = self.game.hero.rect.centery - self.rect.centery
        if -300 < distancex < 300 and -32 < distancey < 32:
            if distancex < 0:
                self.vx = -1
            elif distancex > 0:
                self.vx = 1

    def update(self):
        super().update()
        self.find_player()
        self.apply_gravity()
        self.check_platform_edges()

class Gear(Enemy):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = -1 * 2
        self.vy = 0
        self.health = 2
        self.score = 2
        self.flying = False
        self.name = "gear"

    def set_image_list(self):
        if self.vx < 0:
            self.images = gear_imgs_lt
        else:
            if self.shot:
                self.images = shot_imgs
            else:
                self.images = gear_imgs_rt

    def update(self):
        super().update()
        self.apply_gravity()
        self.check_platform_edges()

class Ghost(Enemy):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 0
        self.vy = 0
        self.health = 3
        self.score = 3
        self.flying = False
        self.moving_left = False
        self.moving_right = False
        self.distancex = self.game.hero.rect.centerx - self.rect.centerx
        self.distancey = self.game.hero.rect.centery - self.rect.centery
        self.name = "ghost"
    
    def set_image_list(self):
        if self.is_alive:
            if self.vx < 0:
                self.images = ghost_close_imgs_lt
            elif self.vx > 0:
                self.images = ghost_close_imgs_rt
            else:
                self.images = ghost_imgs_lt
        else:
            if self.shot:
                self.images = shot_imgs
            else:
                self.images = ghost_imgs_dead
    
    def check_player(self):
        self.distancex = self.game.hero.rect.centerx - self.rect.centerx
        self.distancey = self.game.hero.rect.centery - self.rect.centery
        if -256 < self.distancex < 256 and -64 < self.distancey < 64:
            if self.distancex > 0:
                self.vx = 2
            elif self.distancex < 0:
                self.vx = -2
        else:
            self.vx = 0
    
    def update(self):
        super().update()
        self.check_player()
        self.apply_gravity()
        self.check_platform_edges()

# ---------- ITEMS ---------- #

class Ladder(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Platform(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.name = "platform"
        self.category = "platform"

class Goal(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.animation_speed = 5

    def update(self):
        self.animate()

class WalkThru(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class AnimatedWalkThru(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
    
    def update(self):
        self.animate()

class Message(WalkThru):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Interactable(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)

class Sign(WalkThru):
    def __init__(self, game, image, loc, num):
        super().__init__(game, image, loc)
        self.num = num
        self.display_img = None

    def interact(self):
        if self.game.has_mouse and self.num == "3":
            self.num = 4
        self.display_img = load_image("assets/images/other/message_" + str(self.num) + ".png")
        self.game.display_img = self.display_img

class FloatingBridge(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 3
        self.vy = 0
        self.name = "floating_bridge"
        self.category = "floating_bridge"
    
    def update(self):
        self.move_and_check_platforms()
        self.check_world_edges()

class Coin(Entity):
    def __init__(self, game, image, loc, num):
        super().__init__(game, image, loc)
        self.num = num
        self.score = 0
        self.counter = 30
        self.name = "coin"
        self.should_show_popup = False
        self.num_4 = 1
        if self.num == 1:
            self.image = coin_gold_img
            self.score = 150
        elif self.num == 2:
            self.image = coin_silver_img
            self.score = 100
        elif self.num == 3:
            self.image = coin_bronze_img
            self.score = 50
    
    def interact(self):
        if self.num_4 == 1:
            self.num_4 -= 1
            self.game.hero.numofcoins += 1
            self.game.hero.score += self.score
            self.game.coin_score = self.score
            pickup_snd.play()
            self.game.should_show_popup = True
    
    def show_counters(self):
        if self.game.should_show_popup:
            hits = pygame.sprite.spritecollide(self, self.game.player, False)
            if len(hits) > 0:
                self.image = blank_img
                if self.counter > 0:
                    self.counter -= 1
                    self.game.showing_popups = True
                else:
                    self.game.should_show_popups = False
                    self.game.showing_popups = False
                    self.game.counter = 30
                    self.game.num_2 = 0
                    self.game.num_3 = 12
                    self.game.ticks = 0
                    self.game.speed = 4
                    self.game.speed_2 = 1
                    self.kill()

    def update(self):
        if self.game.should_show_popup:
            self.show_counters()
    
class Health(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.restore = random.randint(1, 5)
        self.value = 10 * self.game.level
        self.name = "health"
    
    def interact(self):
        health_lost = 4 - self.game.hero.health
        amount = random.randint(0, health_lost)
        self.game.hero.health += amount
        self.game.hero.score += self.value
        self.kill()
        pickup_snd.play()

class Torch(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 10 * self.game.level
        self.name = "torch"
            
    def interact(self):
        self.game.hero.has_torch = True
        self.game.hero.has_torch_equipped = True
        self.game.hero.has_gun_equipped = False
        self.kill()

class Wings(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.value = 10 * self.game.level
        self.name = "wings"
        
    def interact(self):
        self.game.hero.has_wings = True
        self.kill()

class Bridge(Entity):
    def __init__(self, game, image, loc, code, way):
        super().__init__(game, image, loc)
        self.code = code
        self.original_pos = self.rect.x
        self.interacting = False
        self.way = way
        self.name = "bridge"
        self.category = "bridge"
        self.vx = 0
        self.vy = 0
    
    def interact(self):
        self.interacting = True
        self.original_pos = self.rect.x
    
    def update(self):
        self.move()
        if self.interacting:
            if self.way == 2:
                self.vx = 1
                if self.rect.x == self.original_pos + 174:
                    self.vx = 0
                    self.interacting = False
            elif self.way == 1:
                self.vx = -1
                if self.rect.x == self.original_pos - 174:
                    self.vx = 0
                    self.interact = False

class Bullet(Entity):
    def __init__(self, game, image, loc, direction, from_x, from_y):
        super().__init__(game, image, loc)
        self.speed_1 = 10 * direction
        self.name = "bullet"
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.centerx = from_x
        self.rect.centery = from_y
        self.speed = 15
        if self.game.has_mouse:
            to_x, to_y = pygame.mouse.get_pos()
            offset_x, offset_y = self.game.get_offsets()
            dx = from_x - to_x - offset_x
            dy = from_y - to_y - offset_y
            hyp = math.sqrt(dx**2 + dy**2)
            self.vx = (dx * self.speed) / hyp
            self.vy = (dy * self.speed) / hyp
            angle = math.degrees(math.atan2(dy, dx))
            self.image = pygame.transform.rotate(self.image, -angle + 180)
        
    def update(self):
        self.check_world_edges()
        if self.game.has_mouse:
            self.rect.x -= self.vx
            self.rect.y -= self.vy
        else:
            self.rect.centerx += self.speed_1
        objects = pygame.sprite.spritecollide(self, self.game.all_sprites_except_player, False)
        if len(objects) > 0:
            for thing in objects:
                if thing.category == "enemy":
                    if thing.is_alive:
                        if thing.health == 1:
                            thing.shot = True
                            thing.is_alive = False
                        thing.health -= 1
                        self.kill()
                    else:
                        pass
                else:
                    self.kill()

class Door(Entity):
    def __init__(self, game, image, loc, color, destination, function, code=None):
        super().__init__(game, image, loc)
        self.destination = destination
        self.function = function
        self.code = code
        self.color = color
        self.locked = False
        self.name = "door"
        if self.code == "None":
            pass
        else:
            self.image = load_image('assets/images/tiles/door_locked_' + self.color + '.png')
            self.locked = True
    
    def interact(self):
        if self.locked and self.code in self.game.hero.keys:
            self.image = door_open_img
            self.locked = False
            opendoor_snd.play()
        elif not self.locked and self.code in self.game.hero.keys:
            if self.function == "teleport_to_dungeon":
                self.game.level = 1
                play_music(cave_music)
                self.game.start_level()
        elif self.code == "None":
            if self.function == "exit_dungeon":
                self.game.level = 3
                play_music(theme_music)
                self.game.start_level()
                self.game.hero.move_to([51.5, 20])

class Key(Entity):
    def __init__(self, game, image, loc, code, color):
        super().__init__(game, image, loc)
        self.code = code
        self.color = None
        self.name = "key"
        if color == 1:
            self.image = key_blue_img
        elif color == 2:
            self.image = key_yellow_img
        elif color == 3:
            self.image = key_orange_img
        elif color == 4:
            self.image = key_green_img
    
    def interact(self):
        self.game.hero.keys.append(self.code)
        pickup_snd.play()
        self.kill()

class Friend(Entity):
    def __init__(self, game, image, loc, num):
        super().__init__(game, image, loc)
        self.num = num
        self.name = "friend"
        self.image = load_image('assets/images/characters/friends/friend_' + str(num) + '.png')
    
    def interact(self):
        self.game.drawing_message = True
        self.game.friend_num = self.num

class LockBox(Entity):
    def __init__(self, game, image, loc, color, function, code):
        super().__init__(game, image, loc)
        self.function = function
        self.code = code
        self.color = color
        self.name = "lockbox"
        self.image = load_image('assets/images/tiles/lockbox_' + self.color + ".png")
        self.times = 0
    
    def interact(self):
        if self.times == 0:
            self.times += 1
            if self.code in self.game.hero.keys:
                opendoor_snd.play()
                if self.function == "reload_and_extra_points":
                    self.game.hero.score += 350
                    self.game.hero.has_gun = True
                    self.game.hero.has_gun_equipped = True
                    self.game.hero.bullet_count = 10
                self.image = load_image('assets/images/tiles/lockbox_' + self.color + "_unlocked.png")


class Lever(Entity):
    def __init__(self, game, image, loc, pos, code):
        super().__init__(game, image, loc)
        self.position = pos
        self.times = 0
        self.code = code
        self.name = "lever"
    
    def interact(self):
        if self.times == 0:
            for bridge in self.game.bridges:
                if bridge.code == self.code:
                    bridge.interact()
            self.times += 1
            if self.position == 1:
                self.position += 1
                self.image = lever_right_img
            elif self.position == 2:
                self.position -= 1
                self.image = lever_left_img
    
class DeathBlock(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
    
    def apply(self):
        self.game.hero.health = 0

class Gun(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.animation_speed = 5
        self.name = "gun"
    
    def interact(self):
        self.game.hero.bullet_count = 10
        self.game.hero.has_gun = True
        self.game.hero.has_gun_equipped = True
        opendoor_snd.play()
        self.kill()
    
    def update(self):
        self.animate()

class Spike(Entity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 0
        self.vy = 0
        self.health = 2
        self.flying = False

        self.name = "spike"
    
    def interact(self):
        self.game.hero.health -= 1
        self.game.hero.vy = 0
        self.game.hero.vy -= 15
    
class Lava(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 0
        self.vy = 0
        self.health = 2
        self.flying = False
        self.animation_speed = 10

        self.name = "spike"
    
    def interact(self):
        self.game.hero.health -= 1
        self.game.hero.vy = 0
        self.game.hero.vy -= 15
    
    def update(self):
        self.animate()

class Water(AnimatedEntity):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        self.vx = 0
        self.vy = 0
        self.health = 2
        self.flying = False
        self.animation_speed = 10

        self.name = "water"
    
    def interact(self):
        self.game.hero.health -= 1
        self.game.hero.vy = 0
        self.game.hero.vy -= 15
    
    def update(self):
        self.animate()

class Bouncy(Interactable):
    def __init__(self, game, image, loc):
        super().__init__(game, image, loc)
        
    def interact(self):
        if self.game.hero.vy > 0:
            self.game.hero.vy -= 40