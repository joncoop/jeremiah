# Imports
import pygame
from utilities import *

# Window settings
GRID_SIZE = 58
WIDTH = 20 * GRID_SIZE # 1160
HEIGHT = 12 * GRID_SIZE # 638
TITLE = "The Lost"
FPS = 60

# Make the game window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)
clock = pygame.time.Clock()

# Define colors
sky_blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (44, 197, 246)
dark_gray = (26, 26, 26)


# Fonts
FONT_Comfortaa_Title = pygame.font.Font('assets/fonts/Comfortaa.ttf', 96)
FONT_Comfortaa = pygame.font.Font('assets/fonts/Comfortaa.ttf', 27)
FONT_Spacegrotesk_Title = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 60)
FONT_Spacegrotesk_menu_screens = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 26)
FONT_Spacegrotesk = pygame.font.Font('assets/fonts/SpaceGrotesk.ttf', 28)
FONT_Pressstart2P = pygame.font.Font('assets/fonts/PressStart2P.ttf', 17)
FONT_Pressstart2P_2 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 19)
FONT_Pressstart2P_3 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 32)
FONT_Pressstart2P_4 = pygame.font.Font('assets/fonts/PressStart2P.ttf', 9)
FONT_LG = pygame.font.Font(None, 64)
FONT_MD = pygame.font.Font(None, 32)
FONT_SM = pygame.font.Font(None, 24)


# Load images

# ----- TILE IMAGES ----- #

background_img = load_image('assets/images/backgrounds/background_main.png')
background_dirt_img = load_image('assets/images/backgrounds/background_dirt.png')
background_cave_img = load_image('assets/images/backgrounds/background_cave.png')
cave_overlay_img = load_image('assets/images/other/background_cave_overlay.png')
cave_overlay_img_2 = load_image('assets/images/other/background_cave_overlay_2.png')

grass_top_middle_img = load_image('assets/images/tiles/grass_top_middle.png')
grass_top_left_img = load_image('assets/images/tiles/grass_top_left.png')
grass_top_right_img = load_image('assets/images/tiles/grass_top_right.png')
grass_corner_left_img = load_image('assets/images/tiles/grass_corner_left.png')
grass_corner_right_img = load_image('assets/images/tiles/grass_corner_right.png')
grass_dirt_corner_left_img = load_image('assets/images/tiles/grass_dirt_corner_left.png')
grass_dirt_corner_right_img = load_image('assets/images/tiles/grass_dirt_corner_right.png')
grass_inside_left_img = load_image('assets/images/tiles/grass_inside_left.png')
grass_inside_right_img = load_image('assets/images/tiles/grass_inside_right.png')
grass_middle_right_img = load_image('assets/images/tiles/grass_middle_right.png')
grass_middle_left_img = load_image('assets/images/tiles/grass_middle_left.png')
dirt_inside_left_img = load_image('assets/images/tiles/dirt_inside_left.png')
dirt_inside_right_img = load_image('assets/images/tiles/dirt_inside_right.png')
dirt_middle_right_img = load_image('assets/images/tiles/dirt_middle_right.png')
dirt_middle_left_img = load_image('assets/images/tiles/dirt_middle_left.png')
grass_top_right_ledge_img = load_image('assets/images/tiles/grass_top_right_ledge.png')
grass_top_left_ledge_img = load_image('assets/images/tiles/grass_top_left_ledge.png')
dirt_middle_img = load_image('assets/images/tiles/dirt_middle.png')
arrow_right_img = load_image('assets/images/tiles/arrow_right.png')
arrow_left_img = load_image('assets/images/tiles/arrow_left.png')
grasses_img = load_image('assets/images/tiles/grasses.png')
grasses_2_img = load_image('assets/images/tiles/grasses_2.png')
grasses_1_imgs = [load_image('assets/images/tiles/grasses_1_1.png'),
                  load_image('assets/images/tiles/grasses_1_2.png'),
                  load_image('assets/images/tiles/grasses_1_3.png'),
                  load_image('assets/images/tiles/grasses_1_2.png'),
                  load_image('assets/images/tiles/grasses_1_2.png')]
grasses_2_imgs = [load_image('assets/images/tiles/grasses_2_1.png'),
                  load_image('assets/images/tiles/grasses_2_2.png'),
                  load_image('assets/images/tiles/grasses_2_3.png'),
                  load_image('assets/images/tiles/grasses_2_2.png'),
                  load_image('assets/images/tiles/grasses_2_2.png')]
blank_img = load_image('assets/images/tiles/blank.png')
blank_imgs = [load_image('assets/images/tiles/blank.png')]
rock_top_middle_img = load_image('assets/images/tiles/rock_top_middle.png')
rock_top_left_img = load_image('assets/images/tiles/rock_top_left.png')
rock_top_right_img = load_image('assets/images/tiles/rock_top_right.png')
rock_middle_img = load_image('assets/images/tiles/rock_middle.png')
rock_top_right_ledge_img = load_image('assets/images/tiles/rock_top_right_ledge.png')
rock_top_left_ledge_img = load_image('assets/images/tiles/rock_top_left_ledge.png')
dirt_secret_img = load_image('assets/images/tiles/dirt_secret.png')
spike_img = load_image('assets/images/tiles/spike.png')
lava_top_img = load_image('assets/images/tiles/lava_top_1.png')
lava_top_imgs = [load_image('assets/images/tiles/lava_top_1.png'),
                 load_image('assets/images/tiles/lava_top_2.png'),
                 load_image('assets/images/tiles/lava_top_3.png'),
                 load_image('assets/images/tiles/lava_top_4.png')]
lava_middle_imgs = [load_image('assets/images/tiles/lava_middle_1.png'),
                 load_image('assets/images/tiles/lava_middle_2.png'),
                 load_image('assets/images/tiles/lava_middle_3.png'),
                 load_image('assets/images/tiles/lava_middle_4.png')]
water_top_imgs = [load_image('assets/images/tiles/water_top_1.png'),
                 load_image('assets/images/tiles/water_top_2.png'),
                 load_image('assets/images/tiles/water_top_3.png'),
                 load_image('assets/images/tiles/water_top_4.png')]
water_middle_imgs = [load_image('assets/images/tiles/water_middle_1.png'),
                 load_image('assets/images/tiles/water_middle_2.png'),
                 load_image('assets/images/tiles/water_middle_3.png'),
                 load_image('assets/images/tiles/water_middle_4.png')]

sign_img = load_image('assets/images/tiles/sign.png')
bouncy_img = load_image('assets/images/tiles/bouncy_1.png')
bouncy_2_img = load_image('assets/images/tiles/bouncy_2.png')
bridge_img = load_image('assets/images/tiles/bridge.png')
exit_sign_img = load_image('assets/images/tiles/exit_sign.png')
door_open_img = load_image('assets/images/tiles/door_open.png')
door_1_img = load_image('assets/images/tiles/door_1.png')
door_locked_green_img = load_image('assets/images/tiles/door_locked_green.png')
door_locked_blue_img = load_image('assets/images/tiles/door_locked_blue.png')
door_locked_orange_img = load_image('assets/images/tiles/door_locked_orange.png')
door_locked_yellow_img = load_image('assets/images/tiles/door_locked_yellow.png')
house_1_middle_img = load_image('assets/images/tiles/house_1_middle.png')
house_1_top_middle_img = load_image('assets/images/tiles/house_1_top_middle.png')
house_1_left_img = load_image('assets/images/tiles/house_1_left.png')
house_1_right_img = flip_image_x(house_1_left_img)
house_1_top_left_img = load_image('assets/images/tiles/house_1_top_left.png')
house_1_top_right_img = load_image('assets/images/tiles/house_1_top_right.png')
house_1_bottom_right_img = load_image('assets/images/tiles/house_1_bottom_right.png')
house_1_bottom_middle_img = load_image('assets/images/tiles/house_1_bottom_middle.png')
house_1_bottom_left_img = load_image('assets/images/tiles/house_1_bottom_left.png')
window_1_img = load_image('assets/images/tiles/window_1.png')
window_2_img = load_image('assets/images/tiles/window_2.png')
house_1_roof_left_img = load_image('assets/images/tiles/house_1_roof_left.png')
house_1_roof_right_img = load_image('assets/images/tiles/house_1_roof_right.png')
house_1_roof_img = load_image('assets/images/tiles/house_1_roof.png')
wire_top_img = load_image('assets/images/tiles/wire_top.png')
wire_img = load_image('assets/images/tiles/wire.png')
metal_wall_img = load_image('assets/images/tiles/metal_gate.png')

# ----- ITEM IMAGES ----- #

key_blue_img = load_image('assets/images/items/key_blue.png')
key_orange_img = load_image('assets/images/items/key_orange.png')
key_yellow_img = load_image('assets/images/items/key_yellow.png')
key_green_img = load_image('assets/images/items/key_green.png')
lockbox_img = load_image('assets/images/tiles/lockbox.png')
lockbox_yellow_img = load_image('assets/images/tiles/lockbox_yellow.png')
lockbox_green_img = load_image('assets/images/tiles/lockbox_green.png')
lockbox_blue_img = load_image('assets/images/tiles/lockbox_blue.png')
lockbox_orange_img = load_image('assets/images/tiles/lockbox_orange.png')
gun_imgs = [load_image('assets/images/items/gun_1.png'),
            load_image('assets/images/items/gun_2.png'),
            load_image('assets/images/items/gun_3.png')]
torch_imgs = [load_image('assets/images/items/torch_1.png'),
              load_image('assets/images/items/torch_2.png'),
              load_image('assets/images/items/torch_3.png')]
torch_icon = load_image('assets/images/items/torch_1.png')
wings_imgs = [load_image('assets/images/items/wings_1.png'),
              load_image('assets/images/items/wings_2.png'),
              load_image('assets/images/items/wings_3.png')]
goal_img = [load_image('assets/images/tiles/flag_1.png'),
            load_image('assets/images/tiles/flag_2.png')]
goalpole_img = [load_image('assets/images/tiles/flagpole.png')]
coin_gold_img = load_image('assets/images/items/coin_gold.png')
coin_silver_img = load_image('assets/images/items/coin_silver.png')
coin_bronze_img = load_image('assets/images/items/coin_bronze.png')
lever_left_img = load_image('assets/images/tiles/lever_left.png')
lever_right_img = load_image('assets/images/tiles/lever_right.png')
lever_img = load_image('assets/images/tiles/lever.png')
instructions_img = load_image('assets/images/other/instructions.png')
health_img = load_image('assets/images/items/heart.png')
ladder_top_img = load_image('assets/images/tiles/ladder_top.png')
ladder_img = load_image('assets/images/tiles/ladder.png')

# ----- PLAYER/FRIEND IMAGES ----- #

player_idle_rt_img = [load_image('assets/images/characters/player/idle.png')]
player_idle_lt_img = [flip_image_x(img) for img in player_idle_rt_img]
player_walk_rt_imgs = [load_image('assets/images/characters/player/walk_1.png'),
                          load_image('assets/images/characters/player/walk_2.png')]
player_walk_lt_imgs = [flip_image_x(img) for img in player_walk_rt_imgs]
player_jump_rt_imgs = [load_image('assets/images/characters/player/jump.png')]
player_jump_lt_imgs = [flip_image_x(img) for img in player_jump_rt_imgs]
player_idle_rt_gun_img = [load_image('assets/images/characters/player/idle_gun.png')]
player_idle_lt_gun_img = [flip_image_x(img) for img in player_idle_rt_gun_img]
player_walk_rt_gun_imgs = [load_image('assets/images/characters/player/walk_1_gun.png'),
                           load_image('assets/images/characters/player/walk_2_gun.png')]
player_walk_lt_gun_imgs = [flip_image_x(img) for img in player_walk_rt_gun_imgs]
player_jump_rt_gun_imgs = [load_image('assets/images/characters/player/jump_gun.png')]
player_jump_lt_gun_imgs = [flip_image_x(img) for img in player_jump_rt_gun_imgs]
player_idle_rt_torch_img = [load_image('assets/images/characters/player/idle_torch.png')]
player_idle_lt_torch_img = [flip_image_x(img) for img in player_idle_rt_torch_img]
player_walk_rt_torch_imgs = [load_image('assets/images/characters/player/walk_1_torch.png'),
                           load_image('assets/images/characters/player/walk_2_torch.png')]
player_walk_lt_torch_imgs = [flip_image_x(img) for img in player_walk_rt_torch_imgs]
player_jump_rt_torch_imgs = [load_image('assets/images/characters/player/jump_torch.png')]
player_jump_lt_torch_imgs = [flip_image_x(img) for img in player_jump_rt_torch_imgs]
player_idle_rt_wings_img = [load_image('assets/images/characters/player/idle_wings.png')]
player_idle_lt_wings_img = [flip_image_x(img) for img in player_idle_rt_wings_img]
player_walk_rt_wings_imgs = [load_image('assets/images/characters/player/walk_1_wings.png'),
                          load_image('assets/images/characters/player/walk_2_wings.png')]
player_walk_lt_wings_imgs = [flip_image_x(img) for img in player_walk_rt_wings_imgs]
player_jump_rt_wings_imgs = [load_image('assets/images/characters/player/jump_wings.png')]
player_jump_lt_wings_imgs = [flip_image_x(img) for img in player_jump_rt_wings_imgs]
player_idle_rt_gun_and_wings_imgs = [load_image('assets/images/characters/player/idle_gun_and_wings.png')]
player_idle_lt_gun_and_wings_img = [flip_image_x(img) for img in player_idle_rt_gun_and_wings_imgs]
player_walk_rt_gun_and_wings_imgs = [load_image('assets/images/characters/player/walk_1_gun_and_wings.png'),
                          load_image('assets/images/characters/player/walk_2_gun_and_wings.png')]
player_walk_lt_gun_and_wings_imgs = [flip_image_x(img) for img in player_walk_rt_gun_and_wings_imgs]
player_jump_rt_gun_and_wings_imgs = [load_image('assets/images/characters/player/jump_gun_and_wings.png')]
player_jump_lt_gun_and_wings_imgs = [flip_image_x(img) for img in player_jump_rt_gun_and_wings_imgs]
player_idle_rt_torch_and_wings_imgs = [load_image('assets/images/characters/player/idle_torch_and_wings.png')]
player_idle_lt_torch_and_wings_img = [flip_image_x(img) for img in player_idle_rt_torch_and_wings_imgs]
player_walk_rt_torch_and_wings_imgs = [load_image('assets/images/characters/player/walk_1_torch_and_wings.png'),
                          load_image('assets/images/characters/player/walk_2_torch_and_wings.png')]
player_walk_lt_torch_and_wings_imgs = [flip_image_x(img) for img in player_walk_rt_torch_and_wings_imgs]
player_jump_rt_torch_and_wings_imgs = [load_image('assets/images/characters/player/jump_torch_and_wings.png')]
player_jump_lt_torch_and_wings_imgs = [flip_image_x(img) for img in player_jump_rt_torch_and_wings_imgs]
player_bullet_img = load_image('assets/images/characters/player/bullet.png')
player_bullet_flash_img = load_image('assets/images/characters/player/bullet_flash.png')
player_restarting_imgs = [load_image('assets/images/characters/player/revive_1.png'),
                          load_image('assets/images/characters/player/revive_2.png'),
                          load_image('assets/images/characters/player/revive_3.png'),
                          load_image('assets/images/characters/player/revive_4.png'),
                          load_image('assets/images/characters/player/revive_5.png'),
                          load_image('assets/images/characters/player/revive_6.png'),
                          load_image('assets/images/characters/player/revive_7.png'),
                          load_image('assets/images/characters/player/revive_8.png'),
                          load_image('assets/images/characters/player/revive_9.png'),
                          load_image('assets/images/characters/player/revive_10.png'),
                          load_image('assets/images/characters/player/revive_1.png'),
                          load_image('assets/images/characters/player/revive_2.png'),
                          load_image('assets/images/characters/player/revive_3.png'),
                          load_image('assets/images/characters/player/revive_4.png'),
                          load_image('assets/images/characters/player/revive_5.png'),
                          load_image('assets/images/characters/player/revive_6.png'),
                          load_image('assets/images/characters/player/revive_7.png'),
                          load_image('assets/images/characters/player/revive_8.png'),
                          load_image('assets/images/characters/player/revive_9.png'),
                          load_image('assets/images/characters/player/revive_10.png'),
                          load_image('assets/images/characters/player/revive_1.png'),
                          load_image('assets/images/characters/player/revive_2.png'),
                          load_image('assets/images/characters/player/revive_3.png'),
                          load_image('assets/images/characters/player/revive_4.png'),
                          load_image('assets/images/characters/player/revive_5.png'),
                          load_image('assets/images/characters/player/revive_6.png'),
                          load_image('assets/images/characters/player/revive_7.png'),
                          load_image('assets/images/characters/player/revive_8.png'),
                          load_image('assets/images/characters/player/revive_9.png'),
                          load_image('assets/images/characters/player/revive_10.png'),
                          load_image('assets/images/characters/player/revive_1.png'),
                          load_image('assets/images/characters/player/revive_2.png'),
                          load_image('assets/images/characters/player/revive_3.png'),
                          load_image('assets/images/characters/player/revive_4.png'),
                          load_image('assets/images/characters/player/revive_5.png'),
                          load_image('assets/images/characters/player/revive_6.png'),
                          load_image('assets/images/characters/player/revive_7.png'),
                          load_image('assets/images/characters/player/revive_8.png')]

friend_1_img = load_image('assets/images/characters/friends/friend_1.png')

# ----- OTHER IMAGES ----- #

spacebar_img = load_image('assets/images/other/spacebar.png')
speech_img = load_image('assets/images/other/speech_bubble.png')
speech_img_2 = load_image('assets/images/other/speech_bubble_2.png')
use_mouse_img = load_image('assets/images/other/use_mouse.png')
gun_icon = load_image('assets/images/other/gun_icon.png')
start_menu_img = load_image('assets/images/other/menu_screen.png')
start_screen_img = load_image('assets/images/other/start_screen.png')
win_screen_1_img = load_image('assets/images/other/win_screen_1.png')
win_screen_2_img = load_image('assets/images/other/win_screen_2.png')
win_screen_3_img = load_image('assets/images/other/win_screen_3.png')
lose_screen_1_img = load_image('assets/images/other/lose_screen_1.png')
lose_screen_2_img = load_image('assets/images/other/lose_screen_2.png')
lose_screen_3_img = load_image('assets/images/other/lose_screen_3.png')
pause_screen_1_img = load_image('assets/images/other/pause_screen_1.png')
pause_screen_2_img = load_image('assets/images/other/pause_screen_2.png')
pause_screen_3_img = load_image('assets/images/other/pause_screen_3.png')
shot_imgs = [load_image('assets/images/other/shot_1.png'),
             load_image('assets/images/other/shot_2.png'),
             load_image('assets/images/other/shot_3.png')]
shot_big_imgs = [load_image('assets/images/other/shot_big_1.png'),
             load_image('assets/images/other/shot_big_2.png'),
             load_image('assets/images/other/shot_big_3.png')]
cursor_img = load_image('assets/images/other/cursor.png')
overlay_img = load_image('assets/images/other/overlay_1.png')

# ----- ENEMY IMAGES ----- #

bat_imgs_lt = [load_image('assets/images/characters/enemies/bat_1.png'),
              load_image('assets/images/characters/enemies/bat_2.png')]
bat_imgs_rt = [flip_image_x(img) for img in bat_imgs_lt]
bat_imgs_dead = [load_image('assets/images/characters/enemies/bat_die.png')]

bee_imgs_lt = [load_image('assets/images/characters/enemies/bee_1.png'),
              load_image('assets/images/characters/enemies/bee_2.png')]
bee_imgs_rt = [flip_image_x(img) for img in bee_imgs_lt]
bee_imgs_dead = [load_image('assets/images/characters/enemies/bee_die.png')]

slime1_imgs_lt = [load_image('assets/images/characters/enemies/slime1_1.png'),
                 load_image('assets/images/characters/enemies/slime1_2.png')]
slime1_imgs_rt = [flip_image_x(img) for img in slime1_imgs_lt]
slime_imgs_dead = [load_image('assets/images/characters/enemies/slime_die.png')]

spider_imgs_lt = [load_image('assets/images/characters/enemies/spider_1.png'),
                  load_image('assets/images/characters/enemies/spider_2.png'),
                  load_image('assets/images/characters/enemies/spider_3.png')]
spider_imgs_rt = [flip_image_x(img) for img in spider_imgs_lt]
spider_imgs_dead = [load_image('assets/images/characters/enemies/spider_die.png')]

ghost_imgs_lt = [load_image('assets/images/characters/enemies/ghost.png'),
                 load_image('assets/images/characters/enemies/ghost_2.png')]
ghost_imgs_rt = [flip_image_x(img) for img in ghost_imgs_lt]
ghost_close_imgs_lt = [load_image('assets/images/characters/enemies/ghost_close.png'),
                       load_image('assets/images/characters/enemies/ghost_close_2.png')]
ghost_close_imgs_rt = [flip_image_x(img) for img in ghost_close_imgs_lt]
ghost_imgs_dead = [load_image('assets/images/characters/enemies/ghost_die.png')]

gear_imgs_lt = [load_image('assets/images/characters/enemies/gear.png'),
                load_image('assets/images/characters/enemies/gear_2.png')]
gear_imgs_rt = [flip_image_x(img) for img in gear_imgs_lt]

# Load sounds
gun_snd = load_sound('assets/sounds/gun_shot.ogg', 0.25)
pickup_snd = load_sound('assets/sounds/pickup_item.ogg')
opendoor_snd = load_sound('assets/sounds/door_open.ogg')
creepy_chord_snd = load_sound('assets/sounds/creepy_chord.ogg')

# Load music
theme_music = ('assets/music/yesterbreeze.ogg')
cave_music = ('assets/music/creep.ogg')

# Levels
levels = ['assets/levels/dungeon.json',
          'assets/levels/world-1.json',
          'assets/levels/world-2.json',
          'assets/levels/world-3.json',
          'assets/levels/world-4.json',
          'assets/levels/world-5.json']

# Other constants and settings
START = 0
PLAYING = 1
PAUSED = 2
WIN = 3
LOSE = 4
INSTRUCTIONS = 5
PLAYING_TUTORIAL = 6
MENU = 7

def display_darkened(self, image):
    dark = pygame.Surface((image.get_width(), image.get_height()), flags=pygame.SRCALPHA)
    dark.fill((50, 50, 50, 0))
    return dark