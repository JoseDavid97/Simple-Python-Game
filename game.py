import pygame, pygame_menu, sys
from config import *
from characters import *
from time import sleep

pygame.init()

class Game:
    difficulty = 2
    resources = Resources
    custom_fonts = CustomFonts
    settings = Settings
    loop_states = LoopStates()
    text_colors = TextColors
    
    def run(self):
        
        pygame.display.set_caption('Kodland Zombie Game')   # Setting game title 
        pygame.display.set_icon(self.resources.ico_img)                    # Setting game icon

        self.screen = pygame.display.set_mode((self.settings.resolution_x, self.settings.resolution_y))
        self.clock = pygame.time.Clock()
        
        menu_theme = pygame_menu.themes.THEME_DEFAULT.copy()
        
        main_menu = pygame_menu.Menu('Kodland Game', self.settings.menu_res_x, self.settings.menu_res_y, theme = menu_theme)
        main_menu.add.button('Jugar', self.play_game)
        main_menu.add.dropselect('Dificultad :', [('Fácil', 1), ('Normal', 2), ('Dificil', 3), ('Imposible', 4)], onchange=self.set_difficulty, default = 1)
        main_menu.add.button('Instrucciones', self.show_instructions)
        main_menu.add.button('Salir', pygame_menu.events.EXIT)
        
        main_menu.mainloop(self.screen, self.main_background)
        
    def main_background(self):
        self.resources.bg_menu.draw(self.screen)
        
    def set_difficulty(self, _, difficulty):
        self.difficulty = difficulty
                    
    def play_game(self):
        self.loop_states.change_state('play')
        
        player = MainPlayer()   # spawn player
        enemies = [Zombie(player, self.difficulty), Witch(player, self.difficulty), Bat(player, self.difficulty)]
        
        while self.loop_states.play:
            self.check_events(player)
            self.screen.blit(self.resources.bg_img, (0, 0))
            
            player.draw(self.screen)
            for enemy in enemies:
                enemy.draw(self.screen)
                
                if enemy.game_over:
                    self.loop_states.change_state('game_over')
            
            pygame.display.flip()
            
            self.clock.tick(60)
            
        for enemy in enemies:
            enemy.stop()
            
        if self.loop_states.game_over:
            self.game_over()
            
    def game_over(self):
        title_render = self.custom_fonts.inst_title.render('Oops, te alcanzó un mounstruo', True, self.text_colors.white)
        title_center_support_x = self.settings.resolution_x//2 - title_render.get_width()//2 
        title_center_support_y = self.settings.resolution_y//2
        
        seconds_to_menu = 10
        while self.loop_states.game_over:
            self.check_events()
            self.screen.blit(self.resources.bg_img, (0, 0))
            self.screen.blit(title_render, (title_center_support_x, title_center_support_y))
            
            text_render = self.custom_fonts.inst_text.render(f"Volviendo al menu en {seconds_to_menu} segundos", True, self.text_colors.white)
            text_center_support_x = self.settings.resolution_x//2 - text_render.get_width()//2 
            self.screen.blit(text_render, (text_center_support_x, title_center_support_y+40))
            
            pygame.display.flip()
            
            self.clock.tick(60)
            
            seconds_to_menu -= 1
            
            if seconds_to_menu == 0:
                self.loop_states.change_state('menu')
            
            sleep(1)
                        
    def show_instructions(self):
        self.loop_states.change_state('intructions')
        
        title_render = self.custom_fonts.inst_title.render('Bienvenido a Kodland Zombie Game (KZM)', True, self.text_colors.white)
        title_center_support = self.settings.resolution_x//2 - title_render.get_width()//2
        
        title_l1 = self.custom_fonts.inst_title_l1.render('Acerca del juego', True, self.text_colors.light_blue)
        text_render_s1 = self.custom_fonts.inst_text.render('KZM es un ejemplo de un juego sencillo escrito en Python y la libreria', True, self.text_colors.white)
        text_render_s2 = self.custom_fonts.inst_text.render('PyGame. KZM se creó con el fin de motivar a los jovenes a descubir lo', True, self.text_colors.white)
        text_render_s3 = self.custom_fonts.inst_text.render('interesante que resulta ser el aprendizaje de la programación.', True, self.text_colors.white)
        
        title_l2 = self.custom_fonts.inst_title_l1.render('Como Jugar', True, self.text_colors.light_blue)
        text_render_s4 = self.custom_fonts.inst_text.render('* Debes utilzar las flechas de tu teclado para escapar de los enemigos', True, self.text_colors.white)
        text_render_s5 = self.custom_fonts.inst_text.render('* Presiona repetidamente las flechas para moverte, entre más rapido mejor !!', True, self.text_colors.white)
        text_render_s6 = self.custom_fonts.inst_text.render('* Si eres alcanzado por cualquiera de los enemigos el juego terminará', True, self.text_colors.white)
        text_render_s7 = self.custom_fonts.inst_text.render('* La velocidad de los enemigos dependerá de la dificultad que escojas', True, self.text_colors.white)
        
        while self.loop_states.intructions:
            self.check_events()
            self.screen.blit(self.resources.bg_img, (0, 0))
            
            self.screen.blit(title_render, (title_center_support, 50))
            
            self.screen.blit(title_l1, (50, 100))
            self.screen.blit(text_render_s1, (80, 140))
            self.screen.blit(text_render_s2, (80, 160))
            self.screen.blit(text_render_s3, (80, 180))
            
            self.screen.blit(title_l2, (50, 220))
            self.screen.blit(text_render_s4, (80, 260))
            self.screen.blit(text_render_s5, (80, 300))
            self.screen.blit(text_render_s6, (80, 340))
            self.screen.blit(text_render_s7, (80, 380))
            
            pygame.display.flip()
            
            self.clock.tick(60)

    def check_events(self, Player = None):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.loop_states.change_state('menu')
                if Player: 
                    if event.key == pygame.K_UP:
                        Player.move('UP')
                    elif event.key == pygame.K_RIGHT:
                        Player.move('RIGHT')
                    elif event.key == pygame.K_DOWN:
                        Player.move('DOWN')
                    elif event.key == pygame.K_LEFT:
                        Player.move('LEFT')