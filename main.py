import pygame

# Initial setup
ico_img = pygame.image.load('resources/icon.png')   # Loading game icon 
bg_img = pygame.image.load("resources/background.jpg")  # Loading game background

pygame.init()
pygame.display.set_caption('Kodland Zombie Game')   # Setting game title 
pygame.display.set_icon(ico_img)                    # Setting game icon

screen = pygame.display.set_mode((722, 600))
clock = pygame.time.Clock()
running_state = True

while running_state:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running_state = False

    screen.blit(bg_img, (0, 0))

    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()