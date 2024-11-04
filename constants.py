from os import path

img_dir = path.join(path.dirname(__file__), 'src/img')
snd_dir = path.join(path.dirname(__file__), 'src/snd')

# screen parameters
WIDTH = 500
HEIGHT = 600
BUTTON_WIDTH = 170
BUTTON_HEIGHT = 50
FPS = 60

add_speed = 0

# colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)

meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_med1.png', 'meteorBrown_med3.png',
               'meteorBrown_small1.png', 'meteorBrown_small2.png', 'meteorBrown_tiny1.png']
