# game setup
WIDTH = 1440
HEIGTH = 860
FPS = 60
TILESIZE = 64

# WORLD_MAP = [
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', 'p', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
#     ['x', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x'],
#     ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'c', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', 'x', 'x', 'x', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'i', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
#     ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
# ]

# ui
BAR_HEIGHT = 22
HEALTH_BAR_WIDTH = 180
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 69
UI_FONT = '../assets/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'white'

# lvl up menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

weapon_list = {
    'sword': {'cooldown': 100, 'damage': 15, 'icon': '../assets/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30, 'icon': '../assets/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20, 'icon': '../assets/weapons/axe/full.png'},
    'rapier': {'cooldown': 50, 'damage': 8, 'icon': '../assets/weapons/rapier/full.png'},
    'sai': {'cooldown': 80, 'damage': 10, 'icon': '../assets/weapons/sai/full.png'}
}
magic_list = {
    'heal': {'power': 10, 'cost': 10, 'icon': '../assets/splash-animation/heal/heal.png'},
    'flame': {'power': 25, 'cost': 20, 'icon': '../assets/splash-animation/flame/fire.png'},
    'ice-spike': {'power': 20, 'cost': 15, 'icon': '../assets/splash-animation/ice_spell/IceRock.png'},
}
monster_list = {
    'squid': {'health': 100, 'xp': 100, 'damage': 10, 'attack_type': 'slash',
              'attack_sound': '../assets/audio/attack/slash.wav', 'speed': 3, 'def': 3, 'hitbox': 80,
              'aggro_range': 360, 'attack_cd': 69},
    'raccoon': {'health': 350, 'xp': 250, 'damage': 42, 'attack_type': 'claw',
                'attack_sound': '../assets/audio/attack/claw.wav', 'speed': 2, 'def': 3, 'hitbox': 120,
                'aggro_range': 400, 'attack_cd': 420},
    'spirit': {'health': 100, 'xp': 110, 'damage': 8, 'attack_type': 'thunder',
               'attack_sound': '../assets/audio/attack/fireball.wav', 'speed': 4, 'def': 3, 'hitbox': 60,
               'aggro_range': 350, 'attack_cd': 410},
    'bamboo': {'health': 77, 'xp': 120, 'damage': 6, 'attack_type': 'leaf_attack',
               'attack_sound': '../assets/audio/attack/slash.wav', 'speed': 3, 'def': 3, 'hitbox': 50,
               'aggro_range': 300, 'attack_cd': 333},
    'cyclops': {'health': 180, 'xp': 220, 'damage': 7, 'attack_type': 'seed_bullet',
               'attack_sound': '../assets/audio/attack/slash.wav', 'speed': 2.7, 'def': 9, 'hitbox': 45,
               'aggro_range': 333, 'attack_cd': 200}}
# must add ghost custom type
