from config import Resources, Settings
from threading import Thread
from time import sleep

class Character:        
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        
class Enemy(Character):
    run = True
    game_over = False
    speed = 4
    
    def __init__(self, player, difficulty):
        self.player = player
        
        if difficulty == 1:
            self.speed = 2
        elif difficulty == 3:
            self.speed = 6
        elif difficulty == 4:
            self.speed = 10

        TPT = Thread(target=self.TrackPlayer, args=())
        TPT.daemon = True
        TPT.start()
    
    def TrackPlayer(self):
        while self.run:
            x_pos = self.player.rect.x
            y_pos = self.player.rect.y
            
            if x_pos > self.rect.x:
                self.rect.x += self.speed
            elif x_pos < self.rect.x:
                self.rect.x -= self.speed
                
            if y_pos > self.rect.y:
                self.rect.y += self.speed
            elif y_pos < self.rect.y:
                self.rect.y -= self.speed
                
            if abs(self.rect.x - x_pos) < 15 and abs(self.rect.y - y_pos)  < 15:
                self.game_over = True
                
            sleep(0.3)
            
    def stop(self):
        self.run = False

class MainPlayer(Character):
    def __init__(self):
        self.image = Resources.mp_img
        self.rect = self.image.get_rect()
        self.rect.x = Settings.resolution_x//2 - 15  # go to x
        self.rect.y = Settings.resolution_y//2 - 30  # go to y
        
    def move(self, direction):
        if direction == 'UP':
            self.rect.y -= 5
        elif direction == 'RIGHT':
            self.rect.x += 5
        elif direction == 'DOWN':
            self.rect.y += 5
        else:
            self.rect.x -= 5
        
class Zombie(Enemy):
    def __init__(self, player, difficulty):
        self.image = Resources.ene1_img
        self.rect = self.image.get_rect()
        self.rect.x = 100  # go to x
        self.rect.y = 100  # go to y
        super().__init__(player, difficulty)
        
class Witch(Enemy):
    def __init__(self, player, difficulty):
        self.image = Resources.ene2_img
        self.rect = self.image.get_rect()
        self.rect.x = 120  # go to x
        self.rect.y = 530  # go to y
        super().__init__(player, difficulty)
        
class Bat(Enemy):
    def __init__(self, player, difficulty):
        self.image = Resources.ene3_img
        self.rect = self.image.get_rect()
        self.rect.x = 450  # go to x
        self.rect.y = 120  # go to y
        super().__init__(player, difficulty)