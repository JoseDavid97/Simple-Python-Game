import pygame_menu
from pygame.image import load as load_image
from pygame.font import SysFont, init as font_init

class Resources:
    ico_img = load_image('resources/icon.png')   # Loading game icon 
    bg_img = load_image("resources/background.jpg")  # Loading game background
    mp_img = load_image("resources/main_player.png")
    ene1_img = load_image("resources/zombie.png")
    ene2_img = load_image("resources/witch.png")
    ene3_img = load_image("resources/bat.png")
    bg_menu = pygame_menu.BaseImage(image_path="resources/background.jpg")
    
class LoopStates:
    
    def __init__(self):
        self.play = False
        self.intructions = False
        self.game_over = False
    
    def change_state(self, state):
        
        if state == 'play':
            self.play = True
            self.intructions = False
            self.game_over = False
        elif state == 'intructions':
            self.play = False
            self.intructions = True
            self.game_over = False
        elif state == 'game_over':
            self.play = False
            self.intructions = False
            self.game_over = True
        else:
            self.play = False
            self.intructions = False
            self.game_over = False

font_init()
class CustomFonts:
    inst_title = SysFont("Arial", 30)
    inst_title_l1 = SysFont('Arial', 24)
    inst_text = SysFont("Arial", 20)
    
class TextColors:
    white = (255, 255, 255)
    light_blue = (95, 186, 255)
    
class Settings:
    resolution_x = 722
    resolution_y = 600
    
    menu_res_x = 500
    menu_res_y = 400