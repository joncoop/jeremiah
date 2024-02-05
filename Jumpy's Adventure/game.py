#    "door": [
#        {"loc": [50.5, 19.5], "color": "yellow", "destination": "none", "function": "teleport_to_dungeon", "code": "111"}
#    ],

#    "door": [
#        {"loc": [1, 3.5], "color": "yellow", "destination": "none", "function": "exit_dungeon", "code": "None"}
#    ],


# Imports
import json, pygame, random, math, os, sys, time, numpy as np
from settings import *
from utilities import *
from entities import *

# Main game class 
class Game:

    def __init__(self):
        self.running = True
        self.grid_on = False
        self.new_game()
        self.random1 = 0
        self.drawing_sign = False
        self.drawing_message = False
        self.showing_spacebar = False
        self.holding_down_shift = False
        self.hovered_over_reply_1 = False
        self.hovered_over_reply_2 = False
        self.should_show_popup = False
        self.showing_popups = False
        self.counter = 30
        self.num_2 = 0
        self.num_3 = 12
        self.ticks = 0
        self.speed = 4
        self.speed_2 = 1
        self.coin_score = 0
        self.message_stage = 1
        self.rep1_left = 0
        self.rep1_right = 0
        self.rep2_left = 0
        self.rep2_right = 0
        self.friend_num = 0
        self.animation_speed = 3
        self.title_num = 1
        self.checkpoint_level = 0
        self.start_loc = [1, 5]
        self.restart_loc = [88, 8]
        self.checkpoint_loc = [0, 0]
        self.health_img = None
        self.background_img = background_img
        self.has_mouse = False
        self.restart_ticks = 0
        self.restart_animation_speed = 5
        self.restart_image_index = 0
    
    # Start the game
    def new_game(self):
        self.player = pygame.sprite.GroupSingle()
        self.hero = Player(self, player_idle_rt_img)
        self.player.add(self.hero)
        self.background_img = background_img
        self.stage = START
        self.level = 2
        self.typewriter_event = pygame.USEREVENT+1
        self.text_surf = None
        self.start_level()
        play_music(theme_music)
    
    # Add all the sprites to their respective groups to add to the screen
    def start_level(self):
        self.platforms = pygame.sprite.Group()
        self.goals = pygame.sprite.Group()
        self.interactables = pygame.sprite.Group()
        self.foregrounds = pygame.sprite.Group()
        self.backgrounds = pygame.sprite.Group()
        self.messages = pygame.sprite.Group()
        self.floating_bridge = pygame.sprite.Group()
        self.blocks = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        self.death_blocks = pygame.sprite.Group()
        self.bridges = pygame.sprite.Group()
        self.ladders = pygame.sprite.Group()
        self.moveables = pygame.sprite.Group()
        self.dead_enemies = pygame.sprite.Group()

        if self.level == 1:
            play_music(cave_music)
            self.background_img = background_cave_img
        else:
            if self.level == 2:
                play_music(theme_music)
            self.background_img = background_img
        self.enemies = pygame.sprite.Group()
        self.player_bullets = pygame.sprite.Group()
        with open(levels[self.level - 1]) as f:
            data = json.load(f)
        self.world_width = data['width'] * GRID_SIZE
        self.world_height = data['height'] * GRID_SIZE
        self.gravity = data['gravity']
        loc = data['start']
        self.start_loc = data['start']
        self.restart_loc = data['restart']
        self.hero.move_to(loc)
        self.checkpoint_loc = [0, 0]
        
        if "grass_top_middle" in data:
            for loc in data['grass_top_middle']:
                self.platforms.add( Platform(self, grass_top_middle_img, loc) )
        
        if "grass_top_right_ledge" in data:
            for loc in data['grass_top_right_ledge']:
                self.platforms.add( Platform(self, grass_top_right_ledge_img, loc) )

        if "grass_top_left_ledge" in data:
            for loc in data['grass_top_left_ledge']:
                self.platforms.add( Platform(self, grass_top_left_ledge_img, loc) )
        
        if "grass_top_right" in data:
            for loc in data["grass_top_right"]:
                self.platforms.add( Platform(self, grass_top_right_img, loc) )
                
        if "grass_top_left" in data:
            for loc in data["grass_top_left"]:
                self.platforms.add( Platform(self, grass_top_left_img, loc) )

        if "grass_inside_right" in data:
            for loc in data["grass_inside_right"]:
                self.platforms.add( Platform(self, grass_inside_right_img, loc) )
                
        if "grass_inside_left" in data:
            for loc in data["grass_inside_left"]:
                self.platforms.add( Platform(self, grass_inside_left_img, loc) )

        if "dirt_inside_right" in data:
            for loc in data["dirt_inside_right"]:
                self.platforms.add( Platform(self, dirt_inside_right_img, loc) )
                
        if "dirt_inside_left" in data:
            for loc in data["dirt_inside_left"]:
                self.platforms.add( Platform(self, dirt_inside_left_img, loc) )

        if "grass_corner_right" in data:
            for loc in data["grass_corner_right"]:
                self.platforms.add( Platform(self, grass_corner_right_img, loc) )
                
        if "grass_corner_left" in data:
            for loc in data["grass_corner_left"]:
                self.platforms.add( Platform(self, grass_corner_left_img, loc) )

        if "grass_dirt_corner_right" in data:
            for loc in data["grass_dirt_corner_right"]:
                self.platforms.add( Platform(self, grass_dirt_corner_right_img, loc) )
                
        if "grass_dirt_corner_left" in data:
            for loc in data["grass_dirt_corner_left"]:
                self.platforms.add( Platform(self, grass_dirt_corner_left_img, loc) )

        if "grass_middle_right" in data:
            for loc in data["grass_middle_right"]:
                self.platforms.add( Platform(self, grass_middle_right_img, loc) )

        if "grass_middle_left" in data:
            for loc in data["grass_middle_left"]:
                self.platforms.add( Platform(self, grass_middle_left_img, loc) )

        if "dirt_middle_right" in data:
            for loc in data["dirt_middle_right"]:
                self.platforms.add( Platform(self, dirt_middle_right_img, loc) )

        if "dirt_middle_left" in data:
            for loc in data["dirt_middle_left"]:
                self.platforms.add( Platform(self, dirt_middle_left_img, loc) )

        if "dirt_middle" in data:
            for loc in data['dirt_middle']:
                self.platforms.add( Platform(self, dirt_middle_img, loc) )
        
        if 'rock_top_middle' in data:
            for loc in data['rock_top_middle']:
                self.platforms.add( Platform(self, rock_top_middle_img, loc) )
        
        if 'rock_top_left' in data:
            for loc in data['rock_top_left']:
                self.platforms.add( Platform(self, rock_top_left_img, loc) )

        if 'rock_top_right' in data:
            for loc in data['rock_top_right']:
                self.platforms.add( Platform(self, rock_top_right_img, loc) )

        if "rock_middle" in data:
            for loc in data['rock_middle']:
                self.platforms.add( Platform( self, rock_middle_img, loc) )
        
        if "rock_top_right_ledge" in data:
            for loc in data['rock_top_right_ledge']:
                self.platforms.add( Platform( self, rock_top_right_ledge_img, loc) )

        if "rock_top_left_ledge" in data:
            for loc in data['rock_top_left_ledge']:
                self.platforms.add( Platform( self, rock_top_left_ledge_img, loc) )
        
        if "lava_top" in data:
            for n, loc in enumerate(data['lava_top']):
                self.items.add( Lava(self, lava_top_imgs, loc))

        if "lava_middle" in data:
            for n, loc in enumerate(data['lava_middle']):
                self.items.add( Lava(self, lava_middle_imgs, loc))

        if "water_top" in data:
            for n, loc in enumerate(data['water_top']):
                self.items.add( Lava(self, water_top_imgs, loc))

        if "water_middle" in data:
            for n, loc in enumerate(data['water_middle']):
                self.items.add( Lava(self, water_middle_imgs, loc))

        if "grasses" in data:
            for loc in data['grasses']:
                rand = random.randint(0, 5)
                if rand == 5:
                    img = grasses_1_imgs
                elif rand == 4:
                    img = grasses_2_imgs
                elif rand == 3:
                    img = grasses_1_imgs
                elif rand == 2:
                    img = grasses_2_imgs
                else:
                    img = grasses_1_imgs
                self.foregrounds.add( AnimatedWalkThru(self, img, loc) )
        
        if "message" in data:
            for sign in data['message']:
                self.messages.add( Sign(self, sign_img, sign['loc'], sign['num']) )
        
        if "arrow_right" in data:
            for loc in data['arrow_right']:
                self.backgrounds.add( WalkThru( self, arrow_right_img, loc) )

        if "arrow_left" in data:
            for loc in data['arrow_left']:
                self.backgrounds.add( WalkThru( self, arrow_left_img, loc) )

        if "bouncy" in data:
            for loc in data['bouncy']:
                self.blocks.add( Bouncy(self, bouncy_img, loc) )
        
        if "floating_bridge" in data:
            for loc in data['floating_bridge']:
                self.floating_bridge.add( FloatingBridge(self, bridge_img, loc) )
        
        if "dirt_secret" in data:
            for loc in data['dirt_secret']:
                self.foregrounds.add( WalkThru(self, dirt_secret_img, loc) )
        
        if "box" in data:
            for loc in data['box']:
                rand = random.randint(1, 3)
                img = load_image('assets/images/tiles/box_' + str(rand) + '.png')
                self.platforms.add( Platform(self, img, loc) )
        
        if "exit_sign" in data:
            for loc in data['exit_sign']:
                self.foregrounds.add( WalkThru(self, exit_sign_img, loc) )
        
        # Load interactables/items/friends

        if "goal" in data:
            for n, loc in enumerate(data['goal']):
                if n == 0 or n == 3 or n == 6 or n == 9:
                    image = goal_img
                else:
                    image = goalpole_img
                self.goals.add( Goal(self, image, loc) )

        if "ladder" in data:
            for n, loc in enumerate(data['ladder']):
                if n == 0:
                    image = ladder_top_img
                else:
                    image = ladder_img
                self.ladders.add( Ladder(self, image, loc) )
        
        if "gun" in data:
            for loc in data['gun']:
                self.items.add( Gun(self, gun_imgs, loc) )

        if "torch" in data:
            for loc in data['torch']:
                self.items.add( Torch(self, torch_imgs, loc) )

        if "coin" in data:
            for loc in data['coin']:
                self.items.add( Coin(self, blank_img, loc['loc'], loc['type']) )
        
        if "health" in data:
            for loc in data['health']:
                self.items.add( Health(self, health_img, loc) )
        
        if "wings" in data:
            for loc in data['wings']:
                self.items.add( Wings(self, wings_imgs, loc) )

        if "door" in data:
            for door in data['door']:
                self.interactables.add( Door(self, door_open_img, door['loc'], door['color'], door['destination'], door['function'], door['code']) )
                
        if "death_block" in data:
            for loc in data['death_block']:
                self.death_blocks.add( DeathBlock(self, blank_img, loc) )
        
        if "spike" in data:
            for loc in data['spike']:
                self.items.add( Spike(self, spike_img, loc) )
        
        if "key" in data:
            for loc in data['key']:
                self.items.add( Key(self, key_yellow_img, loc['loc'], loc['code'], loc['color']) )
        
        if "lever" in data:
            for lever in data['lever']:
                x, y, pos, number = lever
                self.interactables.add( Lever(self, lever_img, [x, y], pos, number) )
        
        if "bridge" in data:
            for bridge in data['bridge']:
                x, y, number, way = bridge
                bridge = Bridge(self, bridge_img, [x, y], number, way)
                self.platforms.add(bridge)
                self.bridges.add(bridge)
                self.backgrounds.add(bridge)
        
        if "friend" in data:
            for friend in data['friend']:
                x, y, num = friend
                self.interactables.add( Friend(self, friend_1_img, [x, y], num))
        
        if "lockbox" in data:
            for box in data['lockbox']:
                self.interactables.add( LockBox(self, lockbox_img, box['loc'], box['color'], box['function'], box['code']) )
                
        """if "friend" in data:
            for friend in data['friend']:
                x, y, friend_num = friend
                if friend_num == 1:
                    img = friend_1_img
                elif friend_num == 2:
                    img = friend_2_img
                elif friend_num == 3:
                    img = friend_3_img
                elif friend_num == 4:
                    img = friend_4_img
                elif friend_num == 5:
                    img = friend_5_img
                self.friends.add( Friend(self, img, [x, y], friend_num) )"""

        if "house" in data:
            for house in data['house']:
                x, y, number = house
                if number == 1:
                    self.backgrounds.add( WalkThru(self, house_1_bottom_left_img, [x-1, y]) )
                    self.backgrounds.add( WalkThru(self, house_1_bottom_middle_img, [x, y]) )
                    self.backgrounds.add( WalkThru(self, house_1_bottom_middle_img, [x+1, y]) )
                    self.backgrounds.add( WalkThru(self, house_1_bottom_right_img, [x+3, y]) )
                    self.backgrounds.add( WalkThru(self, house_1_top_left_img, [x-1, y-1]) )
                    self.backgrounds.add( WalkThru(self, house_1_top_middle_img, [x, y-1]) )
                    self.backgrounds.add( WalkThru(self, window_1_img, [x, y-0.6]) )
                    self.backgrounds.add( WalkThru(self, house_1_top_middle_img, [x+1, y-1]) )
                    self.backgrounds.add( WalkThru(self, house_1_top_middle_img, [x+2, y-1]) )
                    self.backgrounds.add( WalkThru(self, door_1_img, [x+2, y-0.5]) )
                    self.backgrounds.add( WalkThru(self, house_1_top_right_img, [x+3, y-1]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_left_img, [x-2, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x-1, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+1, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+2, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+3, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_right_img, [x+4, y-2]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_left_img, [x-2, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x-1, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+1, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+2, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_img, [x+3, y-3]) )
                    self.backgrounds.add( WalkThru(self, house_1_roof_right_img, [x+4, y-3]) )

        # Load enemies
        if "bat" in data:
            for loc in data['bat']:
                x, y, min_x, max_x = loc
                self.enemies.add( Bat(self, bat_imgs_rt, [x, y], min_x, max_x) )

        if "bee" in data:
            for loc in data['bee']:
                x, y, min_x, max_x = loc
                self.enemies.add( Bee(self, bee_imgs_rt, [x, y], min_x, max_x) )

        if "slime" in data:
            for loc in data['slime']:
                self.enemies.add( Slime(self, slime1_imgs_rt, loc) )

        if "spider" in data:
            for loc in data['spider']:
                self.enemies.add( Spider(self, spider_imgs_rt, loc) )
        
        if "ghost" in data:
            for loc in data['ghost']:
                self.enemies.add( Ghost(self, ghost_imgs_rt, loc) )

        if "gear" in data:
            for loc in data['gear']:
                self.enemies.add( Gear(self, gear_imgs_rt, loc) )

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites_except_player = pygame.sprite.Group()
        self.all_sprites.add(self.backgrounds, self.messages, self.interactables, self.ladders, self.blocks, self.player, self.enemies, self.platforms, self.goals, self.items, self.floating_bridge, self.player_bullets, self.foregrounds, self.death_blocks)
        self.all_sprites_except_player.add(self.enemies, self.platforms, self.floating_bridge)
    

    # Show title screen
    def show_title_screen(self):
        '''
        if self.ticks % self.animation_speed == 0 and self.title_num < 14:
            self.title_num += 1

        screen.blit(load_image('assets/images/other/start_screen_' + str(self.title_num) + '.png'), (0, 0))
        self.ticks += 1
        '''

        title_screen = load_image('assets/images/other/start_screen.png').convert_alpha()
        alpha = min(self.ticks, 255)
        title_screen.set_alpha(alpha)
        screen.blit(title_screen, [0,0])
        self.ticks += 4
    

    # Show win screen
    def show_win_screen(self):
        if self.random1 == 1:
            screen.blit(win_screen_1_img, (0, 0))
        elif self.random1 == 2:
            screen.blit(win_screen_2_img, (0, 0))
        elif self.random1 == 3:
            screen.blit(win_screen_3_img, (0, 0))
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2 - 116
        screen.blit(text, rect)
        text = FONT_Spacegrotesk_menu_screens.render("Your score is: " + str(self.hero.score), True, white)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2
        rect.top = HEIGHT // 2
        screen.blit(text, rect)
        
        
    # Show lose screen
    def show_lose_screen(self):
        if self.random1 == 1:
            screen.blit(lose_screen_1_img, (0, 0))
        elif self.random1 == 2:
            screen.blit(lose_screen_2_img, (0, 0))
        elif self.random1 == 3:
            screen.blit(lose_screen_3_img, (0, 0))
        text = FONT_Pressstart2P_3.render("Your score is: " + str(self.hero.score), True, blue)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2 + 10
        rect.top = HEIGHT // 2 - 62
        screen.blit(text, rect)
    
    
    # Show pause screen
    def show_pause_screen(self):
        if self.random1 == 1:
            screen.blit(pause_screen_1_img, (0, 0))
        elif self.random1 == 2:
            screen.blit(pause_screen_2_img, (0, 0))
        elif self.random1 == 3:
            screen.blit(pause_screen_3_img, (0, 0))
        text = FONT_Pressstart2P_3.render("Your score is: " + str(self.hero.score), True, blue)
        rect = text.get_rect()
        rect.centerx = WIDTH // 2 + 10
        rect.top = HEIGHT // 2 - 82
        screen.blit(text, rect)
    

    # Show start_menu
    def show_start_menu(self):
        screen.blit(start_menu_img, (0, 0))
    
    
    # Show instructions 
    def show_instructions(self):
        screen.blit(instructions_img, (0, 0))
    
    
    # Still experimental
    def typewriter(self, message):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == self.typewriter_event:
                text_len += 1
                if text_len > len(message):
                    text_len = 0
                self.text_surf = None if text_len == 0 else FONT_SM.render(message[:text_len], True, (255, 255, 128))
        if self.text_surf:
            screen.blit(self.text_surf, self.text_surf.get_rect(midleft = screen.get_rect().midleft).move(40, 0))
        pygame.display.flip()
    
    
    # Create checkpoint 
    def create_checkpoint(self):
        self.checkpoint_level = self.level
        self.checkpoint_loc = [self.hero.rect.x / GRID_SIZE, self.hero.rect.y / GRID_SIZE]

    # Load messages for talking to 'friends' or interacting with signs
    def show_messages(self):
        if self.hero.hitting_message():
            if self.level == 1:
                screen.blit(self.display_img, (390, 75))
            else:
                screen.blit(self.display_img, (390, 25))
        elif self.drawing_message:
            if self.friend_num == 1:
                if self.message_stage == 1:
                    rect = speech_img.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img, (rect))
                    pygame.draw.rect(screen, dark_gray, [325, 512, 125, 5])
                    screen.blit(use_mouse_img, (727, 482))
                    name = FONT_Comfortaa.render("Bumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 260
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Hey Jumpy, I just wandered too far. Sorry..", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Where's Dumpy..?", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Where's Dumpy..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Where's Dumpy..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 2:
                    rect = speech_img_2.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img_2, (rect))
                    pygame.draw.rect(screen, dark_gray, [275, 512, 125, 5])
                    screen.blit(use_mouse_img, (835, 482))
                    name = FONT_Comfortaa.render("Bumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 310
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("He's not too far ahead, shouldn't be too hard to find.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Thanks.", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Thanks.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Thanks.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 3:
                    rect = speech_img_2.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img_2, (rect))
                    pygame.draw.rect(screen, dark_gray, [275, 512, 125, 5])
                    screen.blit(use_mouse_img, (835, 482))
                    name = FONT_Comfortaa.render("Bumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 310
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Here, take this! I have a feeling you'll need it.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Thanks!", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Thanks!", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Thanks!", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Thanks!", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Thanks!", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Thanks!", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
            elif self.friend_num == 2:
                if self.message_stage == 1:
                    rect = speech_img_2.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img_2, (rect))
                    pygame.draw.rect(screen, dark_gray, [275, 512, 125, 5])
                    screen.blit(use_mouse_img, (835, 482))
                    name = FONT_Comfortaa.render("Dumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 310
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Hey, just needed a good quiet place for a few minutes.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("For what..?", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("For what..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("For what..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 2:
                    rect = speech_img.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img, (rect))
                    pygame.draw.rect(screen, dark_gray, [325, 512, 125, 5])
                    screen.blit(use_mouse_img, (727, 482))
                    name = FONT_Comfortaa.render("Dumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 260
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("What do you think? Look at my name.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Ew Dumpy, stop.", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Where's Lumpy?", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Ew Dumpy, stop.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Where's Lumpy?", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Ew Dumpy, stop.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Where's Lumpy?", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 3:
                    rect = speech_img.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img, (rect))
                    pygame.draw.rect(screen, dark_gray, [325, 512, 125, 5])
                    screen.blit(use_mouse_img, (727, 482))
                    name = FONT_Comfortaa.render("Dumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 260
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Lumpy is ahead. He's not feeling so good..", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render(".. Okay.", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render(".. Okay.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render(".. Okay.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 150
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 175
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
            elif self.friend_num == 3:
                if self.message_stage == 1:
                    rect = speech_img.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img, (rect))
                    pygame.draw.rect(screen, dark_gray, [325, 512, 125, 5])
                    screen.blit(use_mouse_img, (727, 482))
                    name = FONT_Comfortaa.render("Lumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 260
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Hey.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("What's that door for..?", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("What's that door for..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("What's that door for..?", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 2:
                    rect = speech_img_2.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img_2, (rect))
                    pygame.draw.rect(screen, dark_gray, [275, 512, 125, 5])
                    screen.blit(use_mouse_img, (835, 482))
                    name = FONT_Comfortaa.render("Lumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 310
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Beware, some say it's only pure evil inside..", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Hmm...", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 180
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Sounds like fun tbh, thx.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 155
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Hmm...", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 180
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Sounds like fun tbh, thx.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 155
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Hmm...", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 180
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Sounds like fun tbh, thx.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 155
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
                elif self.message_stage == 3:
                    rect = speech_img.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 120
                    screen.blit(speech_img, (rect))
                    pygame.draw.rect(screen, dark_gray, [325, 512, 125, 5])
                    screen.blit(use_mouse_img, (727, 482))
                    name = FONT_Comfortaa.render("Lumpy", True, dark_gray)
                    rect = name.get_rect()
                    rect.centerx = WIDTH // 2 - 260
                    rect.top = HEIGHT // 2 + 125
                    screen.blit(name, rect)
                    message_1 = FONT_Spacegrotesk.render("Good luck Jumpy.", True, white)
                    rect = message_1.get_rect()
                    rect.centerx = WIDTH // 2
                    rect.top = HEIGHT // 2 + 170
                    screen.blit(message_1, rect)
                    if self.hovered_over_reply_1:
                        reply_1 = FONT_Pressstart2P.render("Thank you.", True, blue)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    elif self.hovered_over_reply_2:
                        reply_1 = FONT_Pressstart2P.render("Thank you.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, blue)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        screen.blit(reply_2, rect)
                    else:
                        reply_1 = FONT_Pressstart2P.render("Thank you.", True, white)
                        rect = reply_1.get_rect()
                        rect.centerx = WIDTH // 2 - 120
                        rect.top = HEIGHT // 2 + 230
                        self.rep1_left = rect.left
                        self.rep1_right = rect.right
                        screen.blit(reply_1, rect)
                        reply_2 = FONT_Pressstart2P.render("Okay, cya.", True, white)
                        rect = reply_2.get_rect()
                        rect.centerx = WIDTH // 2 + 205
                        rect.top = HEIGHT // 2 + 230
                        self.rep2_left = rect.left
                        self.rep2_right = rect.right
                        screen.blit(reply_2, rect)
            elif self.friend_num == 4:
                self.show_store()
            elif self.friend_num == 5:
                pass
    
    
    # Show stuff to display for help and other things.
    def show_stuff(self):
        offset_x, offset_y = self.get_offsets()
        mx, my = pygame.mouse.get_pos()
        # Show the score gain when you pick up a coin. 
        if self.showing_popups:
            if self.counter > 0:
                self.counter -= 1
                self.ticks += 1
                if self.ticks % self.speed == 0:
                    self.num_3 -= 1
                if self.ticks % self.speed_2 == 0:
                    self.num_2 += 1
                counter = pygame.font.Font('assets/fonts/PressStart2P.ttf', self.num_3).render("+ " + str(self.coin_score), True, blue)
                rect = counter.get_rect()
                rect.bottom = self.hero.rect.top - offset_y - 15 - self.num_2
                rect.centerx = self.hero.rect.centerx - offset_x
                screen.blit(counter, rect)
        # Show the spacebar images during the first level.
        if self.showing_spacebar:
            screen.blit(spacebar_img, (self.hero.rect.x - 5 - offset_x, self.hero.rect.bottom + 10 - offset_y))
        # Make the screen darker when you're in the cave level for suspense.
        if self.level == 1:
            if self.hero.has_torch_equipped:
                img = cave_overlay_img_2
            else:
                img = cave_overlay_img
            rect = img.get_rect()
            rect.centerx = self.hero.rect.centerx - offset_x
            rect.centery = self.hero.rect.centery - offset_y
            screen.blit(img, rect)
        # Show restarting aura after you die.
        if self.hero.restarting and not self.restart_image_index >= len(player_restarting_imgs) - 1:
            self.restart_ticks += 1
            if self.restart_ticks % self.restart_animation_speed == 0:
                self.restart_image_index += 1
            images = player_restarting_imgs
            img = images[self.restart_image_index]
            rect = img.get_rect()
            rect.centerx = self.hero.rect.centerx - offset_x
            rect.centery = self.hero.rect.centery - offset_y
            screen.blit(img, rect)
        else:
            self.hero.restarting = False
            self.restart_ticks = 0
            self.restart_image_index = 0
        # Show cursor
        if self.has_mouse:
            pygame.mouse.set_visible(False)
            img = cursor_img
            rect = cursor_img.get_rect()
            rect.centerx = mx
            rect.centery = my
            screen.blit(img, (rect))
        else:
            pygame.mouse.set_visible(True)
        
        # Show HUD
        self.show_health()
        if self.hero.has_gun:
            screen.blit(gun_icon, (10, 10))
            if self.level == 1:
                color = white
            else:
                color = dark_gray
            text = FONT_Pressstart2P_2.render("X: " + str(self.hero.bullet_count), True, color)
            rect = text.get_rect()
            rect.top = 25
            rect.left = 64
            screen.blit(text, rect)
        if self.hero.has_torch:
            screen.blit(torch_icon, (10, 50))
        if "111" in self.hero.keys:
            if self.hero.has_gun and self.hero.has_torch:
                screen.blit(key_yellow_img, (5, 90))
            elif self.hero.has_gun:
                screen.blit(key_yellow_img, (5, 50))
            else:
                screen.blit(key_yellow_img, (5, 10))
        if "222" in self.hero.keys:
            if self.hero.has_gun and self.hero.has_torch:
                screen.blit(key_blue_img, (5, 150))
            elif self.hero.has_gun:
                screen.blit(key_blue_img, (5, 100))
            else:
                screen.blit(key_blue_img, (5, 50))

        # Make everything darker so it looks better
        screen.blit(overlay_img, (0, 0))

    

    # Show health above the player 
    def show_health(self):
        offset_x, offset_y = self.get_offsets()
        if self.hero.health > 4:
            self.hero.health = 4
        elif self.hero.health < 0:
            self.hero.health = 0
        else:
            self.health_img = load_image('assets/images/characters/player/health_' + str(self.hero.health) + '.png')
        screen.blit(self.health_img, (self.hero.rect.x - offset_x, self.hero.rect.top - 20 - offset_y))
    

    # Play creepy chords in scary level
    def play_creepy_music(self):
        if self.level == 1:
            rand = random.randint(0, 10000)
            if rand == 1000:
                creepy_chord_snd.play()
    

    # Function to help reduce any lag
    def in_area(self, sprite1, sprite2):
        dx = abs(sprite1.rect.centerx - sprite2.rect.centerx)
        dy = abs(sprite1.rect.centery - sprite2.rect.centery)

        return dx < 1 * WIDTH and dy < 1 * HEIGHT
    

    def acquired_friend_1(self):
        pass
    

    # Key event handling
    def process_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEMOTION:
                if self.drawing_message:
                    mx, my = pygame.mouse.get_pos()
                    hovered_1 = self.rep1_left <= mx <= self.rep1_right and 572 <= my <= 607
                    hovered_2 = self.rep2_left <= mx <= self.rep2_right and 572 <= my <= 607
                    if hovered_1:
                        self.hovered_over_reply_1 = True
                        self.hovered_over_reply_2 = False
                    elif hovered_2:
                        self.hovered_over_reply_2 = True
                        self.hovered_over_reply_1 = False
                    else:
                        self.hovered_over_reply_1 = False
                        self.hovered_over_reply_2 = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                if self.stage == MENU:
                    mx, my = pygame.mouse.get_pos()
                    if 530 <= mx <= 595 and 204 <= my <= 232:
                        self.has_mouse = True
                    elif 927 <= mx <= 976 and 204 <= my <= 232:
                        self.has_mouse = False
                elif self.stage == PLAYING:
                    if self.has_mouse:
                        self.hero.shoot()
                    if self.drawing_message:
                        if self.rep1_left <= mx <= self.rep1_right and 572 <= my <= 607:
                            if self.friend_num == 1:
                                if self.message_stage == 3:
                                    self.drawing_message = False
                                    self.acquired_friend_1()
                                    self.hero.has_gun = True
                                    self.hero.has_gun_equipped = True
                                    self.hero.bullet_count = 10
                                    self.hero.gun_counter = 1000
                                else:
                                    self.message_stage += 1
                            elif self.friend_num == 2:
                                if self.message_stage == 4:
                                    self.drawing_message = False
                                else:
                                    self.message_stage += 1
                            elif self.friend_num == 3:
                                self.message_stage += 1
                        elif self.rep2_left <= mx <= self.rep2_right and 572 <= my <= 607:
                            if self.friend_num == 1:
                                if self.message_stage == 1:
                                    self.message_stage = 3
                                elif self.message_stage == 2:
                                    self.message_stage += 1
                                elif self.message_stage == 3:
                                    self.hero.has_gun = True
                                    self.hero.has_gun_equipped = True
                                    self.hero.bullet_count = 10
                                    self.hero.gun_counter = 1000
                                    self.drawing_message = False
                            elif self.friend_num == 2:
                                if self.message_stage == 2:
                                    self.message_stage += 1
                                else:
                                    self.drawing_message = False
                            elif self.friend_num == 3:
                                self.drawing_message = False
            elif event.type == pygame.KEYDOWN:
                if self.hero.on_ladder:
                    if event.key == pygame.K_w:
                        self.hero.vy = -6
                    elif event.key == pygame.K_s:
                        self.hero.vy = 6
                    elif event.key == pygame.K_UP:
                        self.hero.vy = -6
                    elif event.key == pygame.K_DOWN:
                        self.hero.vy = 6
                else:
                    if event.key == pygame.K_g:
                        self.grid_on = not self.grid_on
                    if self.stage == START:
                        if event.key == pygame.K_RETURN:
                            self.stage = MENU
                    elif self.stage == PLAYING:
                        if event.key == pygame.K_p:
                            self.stage = PAUSED
                            self.random1 = random.randint(1, 3)
                            pause_music() 
                        elif event.key == pygame.K_m:
                            if pygame.mixer.music.get_busy():
                                pause_music()
                            else:
                                unpause_music()
                        elif event.key == pygame.K_s:
                            if self.holding_down_shift:
                                self.create_checkpoint()
                                self.drawing_message = False
                            if not self.has_mouse:
                                if self.hero.has_gun_equipped:
                                    self.hero.shoot()
                                    self.drawing_message = False
                        elif event.key == pygame.K_w or event.key == pygame.K_UP:
                            self.hero.jump()
                            self.drawing_message = False
                        elif event.key == pygame.K_SPACE:
                            hits = pygame.sprite.spritecollide(self.hero, self.interactables, False)
                            for interactable in hits:
                                interactable.interact()
                                self.message_stage = 1
                        elif event.key == pygame.K_1:
                            if self.hero.has_gun:
                                self.hero.has_gun_equipped = True
                                self.hero.has_torch_equipped = False
                        elif event.key == pygame.K_2:
                            if self.hero.has_torch:
                                self.hero.has_torch_equipped = True
                                self.hero.has_gun_equipped = False
                        # For Testing Purposes
                        elif event.key == pygame.K_n:
                            self.gravity = 0.3
                        elif event.key == pygame.K_l:
                            self.level += 1
                            self.start_level()
                        elif event.key == pygame.K_k:
                            self.level -= 1
                            self.start_level()
                        elif event.key == pygame.K_b:
                            self.hero.health = 4
                            self.hero.has_gun = True
                            self.hero.has_gun_equipped = True
                            self.hero.bullet_count = 500
                            self.hero.has_torch = True
                            self.hero.has_wings = True                            
                    elif self.stage == WIN or self.stage == LOSE:
                        if event.key == pygame.K_RETURN:
                            self.restart()
                    elif self.stage == PAUSED:
                        if event.key == pygame.K_i:
                            self.stage = INSTRUCTIONS
                        elif event.key == pygame.K_RETURN:
                            self.stage = PLAYING
                            unpause_music()
                    elif self.stage == INSTRUCTIONS:
                        if event.key == pygame.K_RETURN:
                            self.stage = PAUSED
                    elif self.stage == MENU:
                        if event.key == pygame.K_RETURN:
                            self.stage = PLAYING
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_LSHIFT] or pressed[pygame.K_RSHIFT]:
            self.holding_down_shift = True
        elif pressed[pygame.K_LEFT] or pressed[pygame.K_a]:
            self.hero.move_left()
            self.drawing_message = False
        elif pressed[pygame.K_d] or pressed[pygame.K_RIGHT]:
            self.hero.move_right()
            self.drawing_message = False
        else:
            self.hero.stop()
            self.holding_down_shift = False
    

    # Advance levels
    def advance(self):
        if self.hero.at_end or self.hero.at_beginning:
            if self.hero.at_end:
                if self.level == 5:
                    rand = random.randint(6, 10)
                    self.level = rand
                else:
                    self.level += 1
            elif self.hero.at_beginning:
                self.level -= 1
            self.start_level()
            if self.hero.at_beginning:
                self.hero.move_to(self.restart_loc)


    # Restart at beginning of level after you die
    def restart(self):
        if self.checkpoint_level == 0:
            self.hero.move_to(self.start_loc)
        else:
            self.hero.move_to(self.checkpoint_loc)
        self.stage = PLAYING
        self.hero.health = 4
        self.hero.vy = 0
        self.hero.vx = 0
        if self.level == 1:
            play_music(cave_music)
        else:
            play_music(theme_music)
        self.hero.restarting = True

            

    # Game updates everything  every frame such as sprite drawings and dying
    def update(self):
        if self.stage == PLAYING:

            for enemy in self.enemies:
                pass
            self.play_creepy_music()

            for sprite in self.all_sprites:
                if (self.in_area(sprite, self.hero)):
                    sprite.update()
            if self.hero.reached_goal():
                if self.level < len(levels):
                    self.level += 1
                    self.start_level()
                else:
                    self.stage = WIN
                    self.random1 = random.randint(1, 3)
            elif not self.hero.is_alive():
                self.stage = LOSE
                self.random1 = random.randint(1, 3)
                pause_music()
    

    # Get offsets for scrolling
    def get_offsets(self):
        if self.hero.rect.centerx < WIDTH // 2:
            offset_x = 0
        elif self.hero.rect.centerx > self.world_width - WIDTH // 2:
            offset_x = self.world_width - WIDTH
        else:
            offset_x = self.hero.rect.centerx - WIDTH // 2
            
        if self.hero.rect.centery < HEIGHT // 2:
            offset_y = 0
        elif self.hero.rect.centery > self.world_height - HEIGHT // 2:
            offset_y = self.world_height - HEIGHT
        else:
            offset_y = self.hero.rect.centery - HEIGHT // 2
        
        if self.has_mouse:
            mx, my = pygame.mouse.get_pos()
            x = -mx + 640
            y = -my + 320 
            offset_x -= x // 15
            offset_y -= y // 15
        return offset_x, offset_y
    

    # Draw everything
    def render(self):
        offset_x, offset_y = self.get_offsets()
        bg_offset_x = -1 * (0.75 * offset_x % self.background_img.get_width())

        screen.blit(self.background_img, [bg_offset_x, 0 * -offset_y])
        screen.blit(self.background_img, [bg_offset_x + self.background_img.get_width(), 0 * -offset_y])

        screen.blit(background_dirt_img, [bg_offset_x, 0 * -offset_y + self.background_img.get_height()])
        screen.blit(background_dirt_img, [bg_offset_x + self.background_img.get_width(), 0 * -offset_y + self.background_img.get_height()])


        for sprite in self.all_sprites:
            if self.in_area(sprite, self.hero):
                screen.blit(sprite.image, [sprite.rect.x - offset_x, sprite.rect.y - offset_y])
                    
        if self.stage == START:
            self.show_title_screen()
        elif self.stage == WIN:
            self.show_win_screen()
        elif self.stage == LOSE:
            self.show_lose_screen()
        elif self.stage == PAUSED:
            self.show_pause_screen()
        elif self.stage == INSTRUCTIONS:
            self.show_instructions()
        elif self.stage == MENU:
            self.show_start_menu()
        
        # Draw grid
        if self.grid_on:
            if self.level == 1:
                draw_grid(screen, WIDTH, HEIGHT, GRID_SIZE, offset_x, offset_y, color=white)
            else:
                draw_grid(screen, WIDTH, HEIGHT, GRID_SIZE, offset_x, offset_y, color=black)

        self.show_messages()
        self.show_stuff()
        for coin in self.items:
            if coin.name == "coin":
                coin.show_counters()


    # Update sprites
    def play(self):
        while self.running:
            self.process_input()
            self.update()
            self.render()
            pygame.display.update()
            clock.tick(FPS)

# Actually start the game
if __name__ == "__main__":
   g = Game()
   g.play()
   pygame.quit()   
